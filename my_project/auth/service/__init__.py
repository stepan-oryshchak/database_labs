from .orders.client_location_service import ClientLocationDAO
from .orders.client_service import ClientDAO
from .orders.pump_service import PumpDAO
from .orders.pump_status_service import PumpStatusDAO
from .orders.pump_water_usage_service import PumpWaterUsageDAO
from .orders.sensor_service import SensorService
from .orders.sprinkler_location_service import SprinklerLocationDAO
from .orders.sprinkler_nozzles_service import SprinklerNozzlesDAO
from .orders.sprinkler_status_service import SprinklerStatusDAO
from .orders.sprinkler_usage_service import SprinklerUsageDAO


client_location_service = ClientLocationDAO()
client_service = ClientDAO()
pump_service = PumpDAO()
pump_status_service = PumpStatusDAO()
pump_water_usage_service = PumpWaterUsageDAO()
sensor_service = SensorService()
sprinkler_location_service = SprinklerLocationDAO()
sprinkler_nozzles_service = SprinklerNozzlesDAO()
sprinkler_status_service = SprinklerStatusDAO()
sprinkler_usage_service = SprinklerUsageDAO()

