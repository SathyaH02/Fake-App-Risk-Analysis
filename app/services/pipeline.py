from app.services.ingestion import load_apps
from app.services.features import name_similarity, detect_brand
from app.services.integrator import integrate
from app.services.scoring import classify

_apps_cache = []

# =========================
# DASHBOARD / BATCH MODE
# =========================
def run_pipeline():
    global _apps_cache
    _apps_cache = []

    for app in load_apps():
        # Dataset apps already have brand
        sim = name_similarity(app["name"], app["brand"])

        score = integrate({
            "name_similarity": sim
        })

        risk = classify(score)

        app["score"] = round(score, 2)
        app["risk"] = risk

        if risk != "Low Risk":
            _apps_cache.append(app)


def get_flagged_apps():
    if not _apps_cache:
        run_pipeline()
    return _apps_cache


def get_app_by_package(package):
    for app in _apps_cache:
        if app["package"] == package:
            return app
    return None


# =========================
# SINGLE PLAY STORE SCAN
# =========================
def analyze_single_app(package_name):
    from app.services.ingestion import fetch_playstore_app

    app = fetch_playstore_app(package_name)

    detected_brand = detect_brand(app["name"])
    features = {}

    # Name deception only if brand detected
    if detected_brand:
        features["name_similarity"] = name_similarity(
            app["name"], detected_brand
        )
    else:
        features["name_similarity"] = 0.0

    # Generic developer email risk
    email = app.get("developer_email", "")
    features["email_risk"] = (
        0.2 if email.endswith(("gmail.com", "outlook.com", "yahoo.com")) else 0.0
    )

    score = integrate(features)
    risk = classify(score)

    app["detected_brand"] = detected_brand or "Unknown"
    app["score"] = round(score, 2)
    app["risk"] = risk

    return app
