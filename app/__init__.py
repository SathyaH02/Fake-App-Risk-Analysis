from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.dashboard import dashboard_bp
    from app.routes.scan import scan_bp
    from app.routes.app_detail import detail_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(scan_bp)
    app.register_blueprint(detail_bp)

    return app
