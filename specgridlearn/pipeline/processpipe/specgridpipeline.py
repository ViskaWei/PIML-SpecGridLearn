from ast import Pass
from base.interface.gateway.baseprocessIF import ProcessIF
from base.pipeline.basepipeline import BasePipeline
from spec.interface.gateway.specprocessIF import StellarSpecProcessIF
# from grid.interface.gateway.gridprocessIF import GridProcessIF


class SpecGridLearnPipeline(BasePipeline):
        def __init__(self):
                pass



        def run(self, PARAM) -> None:
                PIF = StellarSpecProcessIF()
                PIF.interact(PARAM["SPEC"])

                
