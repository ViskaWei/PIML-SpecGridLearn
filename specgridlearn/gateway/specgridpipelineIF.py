from .specgridloaderIF import BoszLoaderIF
from .specgridparamIF import SpecGridParamIF
from specgridlearn.crust.pipeline.specgridpipeline import SpecGridPipeline


class SpecGridPipelineIF():
    def __init__(self) -> None:
        super().__init__()
        self.Object   = None
        self.Loader   = BoszLoaderIF()
        self.paramIF  = SpecGridParamIF()
        self.pipeline = SpecGridPipeline()
        self.Storer   = None

    def set_object(self, OBJECT_PARAM):
        self.Object = self.Loader.load(OBJECT_PARAM)
        
    def set_param(self, PARAM):
        self.PARAM = self.paramIF.set(PARAM)

    def interact(self, PARAM):
        self.set_object(PARAM["OBJECT"])
        self.set_param(PARAM)
        self.pipeline.run(self.PARAM, self.Object)

        