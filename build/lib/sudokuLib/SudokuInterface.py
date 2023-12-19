from abc import ABC, abstractmethod

class SudokuInterface(ABC):
    @abstractmethod
    def solve(self):
        pass
    
    @abstractmethod
    def toJSON(self):
        pass