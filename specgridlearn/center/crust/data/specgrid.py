
from spec.center.crust.data.spec import StellarSpec
from grid.center.crust.data.basegrid import StellarGrid

class SpecGrid(StellarSpec, StellarGrid):
    def __init__(self, wave, flux, para, pdx):
        super().__init__(wave, flux)