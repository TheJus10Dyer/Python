# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:54:06 2022

@author: 500308
"""

import logging
import logging_loki
import numpy as np
import pygeohash as pgh
import time
import json

data = np.loadtxt('gpstestaker.txt')

logging_loki.emitter.LokiEmitter.level_tag = "level"
# assign to a variable named handler 

handler = logging_loki.LokiHandler(
    url="https://logs-prod3.grafana.net/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("229052", "eyJrIjoiYjMwMGNhMmQ3NzMxMDVkMjMwOTY3ZGIyYzZkZTYzZTI4ZDE1ZWIwNiIsIm4iOiJ0ZXN0IiwiaWQiOjY2MDg1Mn0="),
    version="1",
)
# create a new logger instance, name it whatever you want
logging.addLevelName(15, "TRACE")

def trace(self, message, *args, **kws):
   if self.isEnabledFor(15):
   # Yes, logger takes its '*args' as 'args'.
       self._log(15, message, args, **kws)

logging.Logger.trace = trace

while True:
    for i in range(0,len(data)):
        gh = pgh.encode(data[i,0],data[i,1])
        logger = logging.getLogger("my-logger")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        dic = {"long": data[i,0], "lat": data[i,1]}
        # now use the logging object's functions as you normally would
        logger.info(
           str(json.dumps(dic)),
          
           extra={"tags": {"level": "Lat"}},
        )
        print('done')
        time.sleep(.1)
#        logger.trace(
  #          float(data[i,1]),
  #          extra={"tags": {"service": "my-service"}},
     #   )
  #      logger.info(
   #        float(data[i,1]),
    ##      
      #     extra={"tags": {"level": "info1"}},
     #   )
       # logger.warning(
        #   'Lat,Long',
       #    extra={"tags": {"service": "my-service"}},
       # )
        # extra={"tags": {"service": "my-service", "one": "more thing"}}