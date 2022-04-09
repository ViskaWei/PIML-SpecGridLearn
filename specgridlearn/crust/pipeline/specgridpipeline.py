from base.center.crust.basepipeline import BasePipeline
from specgridlearn.crust.process.specgridprocess import StellarSpecOnSpecGridProcess, StellarGridOnSpecGridProcess

class SpecGridPipeline(BasePipeline):
        def __init__(self):
                self.process_list = [StellarSpecOnSpecGridProcess(), StellarGridOnSpecGridProcess()]
                self.param_list = ["SPEC", "GRID"]

        def run(self, PARAM, Object) -> None:
                for ii, process in enumerate(self.process_list):
                        process.set_process(PARAM[self.param_list[ii]])
                        process.start(Object)
                        process.finish(Object)
                                        




                
