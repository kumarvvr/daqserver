from typing import List
from webdaq.models import TestConfigModel
from webdaq.models import MeasurementModel, ResultModel
from webdaq.computebase import ComputeBase


class Compute(ComputeBase):

    def __init__(self, model:TestConfigModel):
        self.testConfigModel = model
    
    def Compute(self, measurements:dict, systemdata:dict=None) -> List[dict]:
        computeresults = {"result":122.5,"percentflow":120.25,"totalscans":systemdata["totalscans"]}
        alerts = {}
        return [computeresults,alerts]

    def UpdateTestConfigModel(self, model:TestConfigModel):
        self.testConfigModel = model