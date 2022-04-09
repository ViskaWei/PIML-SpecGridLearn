from base.pipeline.basepipeline import BasePipeline
from specgridlearn.crust.process.specgridprocess import StellarSpecOnSpecGridProcess, StellarGridOnSpecGridProcess

class SpecGridLearnPipeline(BasePipeline):
        def __init__(self):
                self.Object = None
                self.process_list = [StellarSpecOnSpecGridProcess(), StellarGridOnSpecGridProcess()]
                self.param_list = ["SPEC", "GRID"]

        def run(self, PARAM) -> None:
                for ii, process in enumerate(self.process_list):
                        process.set_process(PARAM[self.param_list[ii]])
                        process.start(self.Object)
                        process.finish(self.Object)
                                        




                
