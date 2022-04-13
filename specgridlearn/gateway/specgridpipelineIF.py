from base.interface.gateway.baseprocessIF import ProcessIF
from .specgridloaderIF import BoszLoaderIF
from .specgridparamIF import SpecGridParamIF
from specgridlearn.crust.pipeline.specgridpipeline import SpecGridPipeline


class SpecGridPipelineIF(ProcessIF):
    def __init__(self) -> None:
        super().__init__()
        self.Object   = None
        self.Loader   = BoszLoaderIF()
        self.Param    = SpecGridParamIF()
        self.Pipeline = SpecGridPipeline()
        self.Storer   = None

    def interact_on_Object(self, Object):
        self.Pipeline.run(self.PARAM, Object)

        