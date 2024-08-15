#定义命令模式的接口。
from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass