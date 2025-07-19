import os
from pathlib import Path
from rich import print
from webdaq.services import TestService
import logging
from datetime import datetime
from pythonjsonlogger.json import JsonFormatter
from webdaq.models import TestConfigModel
from webdaq.utils import DateTimeNow

cwd = os.getcwd()

# Set the global logging settings
logger = logging.getLogger("BHELDAQ")
(year,month,day,hour,minute,second) = DateTimeNow()
logtimestamp = str(year)+str("_")+str(month)+str("_")+str(day)+str("_")+str(hour)+str("_")+str(minute)+str("_")+str(second)
logfilename = "applog_"+logtimestamp+".log"
logpath = Path(cwd) /"logs"/logfilename
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',filename=logpath, encoding='utf-8', level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
logHandler = logging.StreamHandler()
formatter = JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


logger.debug("~-~"*20)
logger.info(" "*10+"TEST STARTED on "+str(datetime.now())+" "*10)
logger.debug("~-~"*20)



configFilePath = Path(cwd) / "config.json"
errorcorrectParametersFilePath = Path(cwd) / "errorcorrect.json"


service = TestService(configFilePath=configFilePath,
                     errorcorrectParameterFilePath=errorcorrectParametersFilePath,
                     simulationMode=True)

service.ConnectAndConfigureHardware()

configModel = service.GetTestConfig()
recordsdbfilename = configModel.machine.pumpnumber+"_"+configModel.machine.testreference+".records.db"
scansdbfilename = configModel.machine.pumpnumber+"_"+configModel.machine.testreference+".scans.db"
recordsdbfilepath = Path(cwd) / "data" / recordsdbfilename
scansdbfilepath = Path(cwd) / "data" / scansdbfilename

service.SetDataPaths(recordsdbfilepath=recordsdbfilepath,scansdbfilepath=scansdbfilepath)

logger.info(service.GetTestConfig())

service.StartTest()

for i in range(100):
    print("Scan "+str(i))
    (cm, cr, cecm, cecr, mavg, ravg, mecavg, recavg, reccount, currentscan, totalscans) = service.Process()
    if(currentscan == 1):
        service.RecordTestData()

service.StopTest()

print("Number of recorded data : "+str(service.GetRecordedDataCount()))

    

