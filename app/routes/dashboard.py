from flask import Blueprint, render_template
from app.services.pipeline import get_flagged_apps

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    apps = get_flagged_apps()
    return render_template("dashboard.html", apps=apps)
