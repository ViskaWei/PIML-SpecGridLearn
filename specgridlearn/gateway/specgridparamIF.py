from base.interface.gateway.baseparamIF import MultiParamIF
from spec.interface.gateway.specparamIF import SpecParamIF
from grid.interface.gateway.gridparamIF import GridParamIF

class SpecGridParamIF(MultiParamIF):
    def __init__(self) -> None:
        super().__init__()
        self.paramIF_list = [SpecParamIF(), GridParamIF()]
