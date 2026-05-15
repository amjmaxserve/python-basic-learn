"""
buit-in modules

1) import math 

this module is for pre-built math functions in python

math.pow(2,4)

math.sqrt(16)

math.floor(5/2)

math.ceil(5/2)


2) from datetime import datetime, timezone

this modules imports times based presets where we can use it in our programs

now = datetime.now()

datetime.datetime(2018, 10, 7, 12, 27, 25, 527961)

obj.astimezone(timezone.utc)
"""

import os
import math
from datetime import datetime, timezone
import logging



print(math.pow(2,4))
print(math.sqrt(16))
print(math.floor(5/2))
print(math.ceil(5/1))

now = datetime.now()

print(now)



logger = logging.getLogger("MAIN")
print(logger)
logger.error("Error happen in the app")
#obj.astimezone(timezone.utc)