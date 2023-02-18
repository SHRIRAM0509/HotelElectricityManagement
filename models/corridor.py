from typing import List
from models.device import Device
from models.device_does_not_exist_exception import DeviceDoesNotExistException
from models.device_state import DeviceState

class Corridor:
    def __init__(self, devices: List[Device]):
        # TODO: check if device id is unique
        self.devices = {device.id: device for device in devices}
        
    def __getitem__(self, key: int) -> Device:
        if key in self.devices:
            return self.devices[key]
        raise DeviceDoesNotExistException(key)

    def toggle_device_status(self, device_id: int) -> None:
        device: Device = self.__getitem__(device_id)
        device.toggle_state()
    
    def set_device_state(self, device_id: int, device_state: DeviceState) -> None:
        device = self.__getitem__(device_id)
        device.set_state(device_state)
