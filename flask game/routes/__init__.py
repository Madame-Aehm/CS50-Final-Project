from flask import Flask


def register_blueprints(app: Flask) -> None:
    """
    Register all feature blueprints on the given Flask app.
    """
    from routes.police import police_bp
    from routes.bakery import bakery_bp
    from routes.bank import bank_bp
    from routes.phone import phone_bp
    from routes.airport import airport_bp

    app.register_blueprint(police_bp)
    app.register_blueprint(bakery_bp)
    app.register_blueprint(bank_bp)
    app.register_blueprint(phone_bp)
    app.register_blueprint(airport_bp)

