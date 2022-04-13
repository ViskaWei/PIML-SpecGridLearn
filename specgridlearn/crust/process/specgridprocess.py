from abc import ABC, abstractmethod
from grid.center.crust.process.gridprocess import StellarGridProcess
from spec.center.crust.process.specprocess import StellarSpecProcess
from prepnn.center.crust.process.prepnnprocess import StellarPrepNNProcess

from ..data.specgrid import StellarSpecGrid


class BaseOnSpecGridProcess(ABC):
    @abstractmethod
    def finish(self, SpecGrid: StellarSpecGrid):
        pass

class StellarSpecOnSpecGridProcess(StellarSpecProcess):
    def set_process(self, PARAM):
        return super().set_process(PARAM["OP"], PARAM["MODEL"], PARAM["DATA"])

    def finish(self, SpecGrid: StellarSpecGrid):
        SpecGrid.value = SpecGrid.logflux

class StellarGridOnSpecGridProcess(StellarGridProcess):
    def set_process(self, PARAM):
        return super().set_process(PARAM["OP"], PARAM["MODEL"], None)

    def finish(self, SpecGrid: StellarSpecGrid):
        SpecGrid.noiser = lambda x: SpecGrid.Obs.get_log_sigma(x, log=1)
        SpecGrid.dim    = SpecGrid.coord_dim
        SpecGrid.train  = {}
        SpecGrid.test   = {}

class StellarPrepNNSpecGridProcess(StellarPrepNNProcess):
    def set_process(self, PARAM):
        return super().set_process(PARAM["OP"], None, None)

    def finish(self, SpecGrid: StellarSpecGrid):
        pass
