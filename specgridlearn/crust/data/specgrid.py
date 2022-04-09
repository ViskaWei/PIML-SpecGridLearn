import numpy as np
from spec.center.crust.data.basespec import StellarSpec
from grid.center.crust.data.basegrid import StellarGrid

class StellarSpecGrid(StellarSpec, StellarGrid):
    def __init__(self, wave, flux, para):
        super(StellarSpec, self).__init__(wave, flux)
        super(StellarGrid, self).__init__(para, None)

        assert self.num_spec == self.coord.shape[0]

    def get_coord_logflux(self, coord_i):
        idx = self.get_coord_idx(coord_i)
        if hasattr(self, 'logflux'):
            return self.logflux[idx]
        else:
            return np.log(self.flux[idx])