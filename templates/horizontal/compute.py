from webdaq.models import TestConfigModel
from webdaq.models import MeasurementModel, ResultModel
from webdaq.computebase import ComputeBase


class Compute(ComputeBase):

    def __init__(self, model:TestConfigModel):
        self.testConfigModel = model
    
    def Compute(self, measurements:dict, systemdata:dict=None) -> dict:
        
        return {"result":122.5,"totalscans":systemdata["totalscans"]}

    def UpdateTestConfigModel(self, model:TestConfigModel):
        self.testConfigModel = model