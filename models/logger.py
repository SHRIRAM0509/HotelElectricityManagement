from abc import abstractmethod, ABC

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass
    
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(message)
