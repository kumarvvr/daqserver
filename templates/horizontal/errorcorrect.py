from webdaq.utils import PollingFileWatcher
from webdaq.models import TestConfigModel, MeasurementModel, ResultModel
from webdaq.errorcorrectbase import ErrorCorrectorBase
from pathlib import Path
import json
from rich import print
from extmethods import ecextmethod
import logging

class ErrorCorrector(ErrorCorrectorBase):

    def __init__(self, testConfigModel:TestConfigModel,ecparameters:dict):
        self.logger = logging.getLogger("BHELDAQ")

        self.testConfigModel = testConfigModel
        self.ecparameters = ecparameters
        self.logger.info("EC Parameters given are")
        self.logger.info(ecparameters)

    def ErrorCorrect(self, measurements:dict,systemdata:dict=None)-> dict:
        measurements["flow"] = 99999
        measurements["errorcorrectinclusion"] = 127
        return measurements
    
    def UpdateConfiguration(self, updatedConfig):
        # Update the internal configuration when the config is updated
        self.testConfigModel = updatedConfig
        self.__SetInternalsFromConfig()

    def UpdateErrorCorrectParameters(self, parameters):
        self.ecparameters = parameters
        self.__SetInternalsFromErrorCorrectParameters()

    def __SetInternalsFromErrorCorrectParameters(self):
        pass

    def __SetInternalsFromConfig(self):
        pass
        