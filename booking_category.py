from abc import ABC, abstractmethod

class BookingCategory(ABC):
    def __init__(self, multiplier: float):
        self._multiplier = multiplier

    @abstractmethod
    def get_multiplier(self) -> float:
        pass


class EconomyClass(BookingCategory):
    def __init__(self):
        super().__init__(1.0)

    def get_multiplier(self) -> float:
        return self._multiplier


class BusinessClass(BookingCategory):
    def __init__(self):
        super().__init__(1.5)

    def get_multiplier(self) -> float:
        return self._multiplier


class FirstClass(BookingCategory):
    def __init__(self):
        super().__init__(2.0)

    def get_multiplier(self) -> float:
        return self._multiplier
