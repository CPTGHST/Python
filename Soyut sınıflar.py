from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def alan(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

    def message(self):
        print("Hello Neo")

class square(shape):
    def __init__(self,edge):
        self.edge = edge

    def alan(self):
        return self.edge * self.edge

    def perimeter(self):
        return 4 * self.edge

square = square(3)
print(square.alan(),square.perimeter())
square.message()

