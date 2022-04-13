from base.interface.gateway.baseparamIF import MultiParamIF
from spec.interface.gateway.specparamIF import StellarSpecParamIF
from grid.interface.gateway.gridparamIF import StellarGridParamIF
from prepnn.interface.gateway.prepnnparamIF import StellarPrepNNParamIF

class SpecGridParamIF(MultiParamIF):
    def __init__(self) -> None:
        super().__init__()
        self.paramIF_list = [StellarSpecParamIF(), StellarGridParamIF(), StellarPrepNNParamIF()]
