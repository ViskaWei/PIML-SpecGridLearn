from base.center.crust.basepipeline import ProcessPipeline
from specgridlearn.crust.process.specgridprocess import StellarSpecOnSpecGridProcess,\
        StellarGridOnSpecGridProcess, StellarPrepNNSpecGridProcess

class SpecGridPipeline(ProcessPipeline):
        def __init__(self):
                self.process_list = [StellarSpecOnSpecGridProcess(), StellarGridOnSpecGridProcess(), StellarPrepNNSpecGridProcess()]


                                        




                
