



from base.interface.gateway.baseprocessIF import ProcessIF
from specgridlearn.gateway.specgridloaderIF import BoszLoaderIF


class SpecGridProcessIF(ProcessIF):
    def __init__(self) -> None:
        super().__init__()
        self.Loader   = BoszLoaderIF()
        self.Process  = StellarSpecProcess()
        self.Storer   = None