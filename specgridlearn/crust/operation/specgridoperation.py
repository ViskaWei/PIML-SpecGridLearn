
# from abc import ABC, abstractmethod
# from spec.center.crust.operation.specoperation import 

# class BaseSpecGridOperation(BaseOperation):
#     @abstractmethod
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid):
#         pass

# class CoordxifySpecGridOperation(BaseSpecGridOperation):
#     def perform(self, coord):
#         origin = coord.min(0)
#         OP = CoordxifyGridOperation(origin, Constants.PHYTICK)
#         return OP.perform(coord)

#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid):
#         if hasattr(SpecGrid, "box"):
#             origin = SpecGrid.box["min"]
#         else:
#             origin = SpecGrid.coord.min(0)

#         OP = CoordxifyGridOperation(origin, Constants.PHYTICK)
#         OP.perform_on_Grid(SpecGrid)


# class InterpSpecGridOperation(BaseModelOperation, BaseSpecGridOperation):
#     def set_model(self, model_type: str) -> InterpBuilderSpecGridModel:
#         if model_type == "RBF":
#             model = RBFInterpBuilderSpecGridModel()
#         elif model_type == "PCARBF":
#             model = PCARBFInterpBuilderSpecGridModel()
#         else:
#             raise ValueError("Unknown Interp model type: {}".format(model_type))
#         return model

#     def perform(self, data):
#         return self.model.apply(data)

#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.model.apply_on_SpecGrid(SpecGrid)

# class BoxSpecGridOperation(StellarBoxOperation, BaseSpecGridOperation):
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.perform_on_Box(SpecGrid)

# class SplitSpecGridOperation(SplitSpecOperation, BaseSpecGridOperation):
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.perform_on_Spec(SpecGrid)

# class TuneSpecGridOperation(TuneSpecOperation, BaseSpecGridOperation):
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.perform_on_Spec(SpecGrid)

# class LogSpecGridOperation(LogSpecOperation, BaseSpecGridOperation):
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.perform_on_Spec(SpecGrid)

# class SimulateSkySpecGridOperation(SimulateSkySpecOperation, BaseSpecGridOperation):
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.perform_on_Spec(SpecGrid)

# class MapSNRSpecGridOperation(MapSNRSpecOperation, BaseSpecGridOperation):
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.perform_on_Spec(SpecGrid)

# class AddPfsObsSpecGridOperation(AddPfsObsSpecOperation, BaseSpecGridOperation):
#     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
#         self.perform_on_Spec(SpecGrid)


# # class MakePrepNNSpecGridOperation(BaseSpecGridOperation):

# #     def perform_on_SpecGrid(self, SpecGrid: StellarSpecGrid) -> None:
# #         coordx_rng = SpecGrid.coordx_rng