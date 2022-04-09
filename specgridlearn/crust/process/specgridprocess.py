

from abc import ABC, abstractmethod
from grid.center.crust.process.gridprocess import StellarGridProcess
from spec.center.crust.process.specprocess import StellarSpecProcess
from ..data.specgrid import StellarSpecGrid


class BaseOnSpecGridProcess(ABC):
    @abstractmethod
    def finish(self, SpecGrid: StellarSpecGrid):
        pass

class StellarSpecOnSpecGridProcess(StellarSpecProcess):
    def set_process(self, PARAM):
        return super().set_process(PARAM["OP"], PARAM["MODEL"], PARAM["DATA"])

    def finish(self, SpecGrid: StellarSpecGrid):
        SpecGrid.value = SpecGrid.flux

class StellarGridOnSpecGridProcess(StellarGridProcess):
    def set_process(self, PARAM):
        return super().set_process(PARAM["OP"], PARAM["MODEL"], PARAM["DATA"])

    def finish(self, SpecGrid: StellarSpecGrid):
        pass