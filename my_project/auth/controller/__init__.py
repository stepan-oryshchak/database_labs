from .orders.client_controller import ClientController
from .orders.pump_status_controller import PumpStatusController
from .orders.sprinkler_status_controller import SprinklerStatusController
from .orders.client_location_controller import ClientLocationController
from .orders.sprinkler_usage_controller import SprinklerUsageController
from .orders.pump_water_usage_controller import PumpWaterUsageController
from .orders.sprinkler_nozzles_controller import SprinklerNozzlesController
from .orders.sprinkler_location_controller import SprinklerLocationController
from .orders.region_controller import RegionController
from .orders.sensor_controller import SensorController

client_controller = ClientController()
pump_status_controller = PumpStatusController()
sprinkler_status_controller = SprinklerStatusController()
client_location_controller = ClientLocationController()
sprinkler_usage_controller = SprinklerUsageController()
pump_water_usage_controller = PumpWaterUsageController()
sprinkler_nozzles_controller = SprinklerNozzlesController()
sprinkler_location_controller = SprinklerLocationController()
region_controller = RegionController()
sensor_controller = SensorController()
