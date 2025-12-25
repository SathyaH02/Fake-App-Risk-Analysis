from flask import Blueprint, render_template
from app.services.pipeline import get_app_by_package

detail_bp = Blueprint("detail", __name__)

@detail_bp.route("/app/<package>")
def app_detail(package):
    app = get_app_by_package(package)
    return render_template("app_detail.html", app=app)
