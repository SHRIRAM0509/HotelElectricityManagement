from __future__ import annotations
from abc import abstractmethod, ABC
from datetime import datetime
from models.corridor import SubCorridor
from models.device_state import DeviceState
from models.device_type import DeviceType
from models.floor import Floor

from models.hotel import Hotel
from models.movement_type import MovementType

from models.rule_data import RuleData

class Rule(ABC):
	def __init__(self, data: RuleData, hotel: Hotel) -> None:
		self.rule_data = data
		self.hotel = hotel
	
	@abstractmethod
	def is_match(self) -> bool:
		pass
	
	@abstractmethod
	def on_match(self) -> None:
		pass

	def run(self) -> None:
		if self.is_match():
			self.on_match()

class DateUtil:
	# accepting date in ISO only for now
	def __init__(self, date: datetime) -> None:
		self.date = date

	def from_string(cls, date_str: str) -> DateUtil:
		return cls(datetime.fromisoformat(date_str))
		
	def at_hour(self, hour: int) -> DateUtil:
		return DateUtil(self.date.replace(hour=hour, minute=0, second=0, microsecond=0))

	def next_day(self) -> DateUtil:
		return DateUtil(self.date.replace(day=self.date.day+1))

	def is_between(self, before: datetime, after: datetime) -> bool:
		return before < self.date < after

class NightTimeSlotRule(Rule):
	START_HOUR = 18
	END_HOUR = 6
 
	def is_match(self) -> bool:
		timestamp = DateUtil(self.rule_data.timestamp)
		start = timestamp.at_hour(self.START_HOUR).date
		end = timestamp.at_hour(self.END_HOUR).next_day().date
		return timestamp.is_between(start, end)

	def on_match(self):
		pass

class MotionDetectedRule(Rule):
	MOVEMENT_TYPE = MovementType.MOVEMENT
	
	def is_match(self) -> bool:
		return self.rule_data.movement == self.MOVEMENT_TYPE

	def on_match(self):
		floor = self.hotel.get_floor(self.rule_data.floor_number)
		corridor = floor.get_corridor(self.rule_data.corridor_id)
		if isinstance(corridor, SubCorridor):
			corridor.set_state_for_same_device_type(DeviceType.LIGHT, DeviceState.ON)

class PowerConsumptionLimitRule(Rule):
	def is_match(self) -> bool:
		floor = self.hotel.get_floor(self.rule_data.floor_number)
		floor_limit = floor.power_consumption_limit
		floor_power_consumption = floor.power_consumption
		return floor_power_consumption > floor_limit
	
	def on_match(self) -> None:
		floor = self.hotel.get_floor(self.rule_data.floor_number)
		for corridor in floor.corridors:
			if isinstance(corridor, SubCorridor):
				corridor.set_state_for_same_device_type(DeviceType.AC, DeviceState.OFF)
