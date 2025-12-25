from flask import Blueprint, render_template, request
from app.services.pipeline import analyze_single_app
from app.services.utils import extract_package
from google_play_scraper import search

scan_bp = Blueprint("scan", __name__)

@scan_bp.route("/scan", methods=["GET", "POST"])
def scan():
    result = None
    error = None
    choices = None   # ✅ always defined

    if request.method == "POST":
        user_input = request.form.get("input_value", "").strip()

        if not user_input:
            error = "Please enter a Play Store app link or app name."
        else:
            # 1️⃣ Try extracting package directly
            package = extract_package(user_input)

            # 2️⃣ If not a package, search Play Store
            if not package:
                try:
                    results = search(user_input, n_hits=5)
                except Exception:
                    results = []

                choices = [
                    {
                        "name": r.get("title"),
                        "package": r.get("appId"),
                        "developer": r.get("developer")
                    }
                    for r in results if r.get("appId")
                ]

                if not choices:
                    error = (
                        "No matching app found. Please enter a full Play Store app link "
                        "or a more specific app name."
                    )
            else:
                # Package already known (URL or user selection)
                try:
                    result = analyze_single_app(package)
                except Exception:
                    error = (
                        "Unable to analyze this app at the moment. "
                        "Please try another one."
                    )

        # 3️⃣ If user needs to choose, return early
        if choices and not result and not error:
            return render_template(
                "scan.html",
                choices=choices
            )

    return render_template(
        "scan.html",
        result=result,
        error=error
    )
