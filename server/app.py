from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    from server.controllers.user_controller import user_bp
    from server.controllers.appearance_controller import appearance_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.auth_controller import auth_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(appearance_bp, url_prefix='/api/appearances')
    app.register_blueprint(episode_bp, url_prefix='/api/episodes')
    app.register_blueprint(guest_bp, url_prefix='/api/guests')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to Two Late Show !"})

    with app.app_context():
        print("Registered routes:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.endpoint}: {rule.rule} ({rule.methods})")

    return app