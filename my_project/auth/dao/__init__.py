from .orders.client_dao import ClientDAO
from .orders.sensor_dao import SensorDAO
from .orders.sprinkler_location_dao import SprinklerLocationDAO
from .orders.sprinkler_nozzles_dao import SprinklerNozzlesDAO
from .orders.pump_dao import PumpDAO
from .orders.pump_water_usage_dao import PumpWaterUsageDAO
from .orders.sprinkler_usage_dao import SprinklerUsageDAO
from .orders.client_location_dao import ClientLocationDAO
from .orders.sprinkler_status_dao import SprinklerStatusDAO
from .orders.pump_status_dao import PumpStatusDAO

client_dao = ClientDAO()
sensor_dao = SensorDAO()
sprinkler_location_dao = SprinklerLocationDAO()
sprinkler_nozzles_dao = SprinklerNozzlesDAO()
pump_dao = PumpDAO()
pump_water_usage_dao = PumpWaterUsageDAO()
sprinkler_usage_dao = SprinklerUsageDAO()
client_location_dao = ClientLocationDAO()
sprinkler_status_dao = SprinklerStatusDAO()
pump_status_dao = PumpStatusDAO()


