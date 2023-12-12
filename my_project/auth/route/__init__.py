from flask import Flask
from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    from .orders.sensor_route import sensor_bp
    from .orders.sprinkler_location_route import sprinkler_location_bp
    from .orders.sprinkler_nozzles_route import sprinkler_nozzles_bp
    from .orders.pump_route import pump_bp
    from .orders.pump_status_route import pump_status_bp
    from .orders.sprinkler_status_route import sprinkler_status_bp
    from .orders.sprinkler_usage_route import sprinkler_usage_bp
    from .orders.pump_water_usage_route import pump_water_usage_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(sensor_bp)
    app.register_blueprint(sprinkler_location_bp)
    app.register_blueprint(sprinkler_nozzles_bp)
    app.register_blueprint(pump_bp)
    app.register_blueprint(pump_status_bp)
    app.register_blueprint(sprinkler_status_bp)
    app.register_blueprint(sprinkler_usage_bp)
    app.register_blueprint(pump_water_usage_bp)
