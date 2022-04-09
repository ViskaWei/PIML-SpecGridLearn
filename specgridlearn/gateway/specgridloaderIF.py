import os
from abc import ABC, abstractmethod
from base.interface.gateway.baseloaderIF import DataLoaderIF, DictLoaderIF, ObjectLoaderIF
from specgridlearn.crust.data.specgrid import StellarSpecGrid

class BoszLoaderIF(ObjectLoaderIF):
    """ class for loading Spec. """
    def set_param(self, PARAM):
        self.loader = DictLoaderIF(PARAM["BOSZ_PATH"])

    def load(self):
        flux = self.loader.load_arg("flux")
        wave = self.loader.load_arg("wave")
        para = self.loader.load_arg("para")
        return StellarSpecGrid(wave, flux, para)
