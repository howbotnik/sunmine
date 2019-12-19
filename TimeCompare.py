import datetime
import logging

def isTimeInRange(upperTime, lowerTime):
    upper = convertTo24Hours(upperTime)
    lower = convertTo24Hours(lowerTime)
    now = datetime.datetime.now()
    outcome = False

    if now.time().replace(microsecond=0) < upper.time() and now.time().replace(microsecond=0) > lower.time():
        outcome = True
    else:
        outcome = False
    return outcome

def convertTo24Hours(time):
    convertedTime = datetime.datetime.strptime(time, "%I:%M:%S %p")
    return convertedTime
