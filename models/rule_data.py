from dataclasses import dataclass

from models.corridor_type import CorridorType
from models.movement_type import MovementType
from models.device_type import DeviceType

@dataclass
class RuleData:
	floor_number: int
	corridor_type: CorridorType
	corridor_id: int
	timestamp: str
	movement: MovementType
	device_type: DeviceType
	device_id: int
