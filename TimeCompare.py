import datetime

class TimeCompare:
    upperTime = None
    lowerTime = None

    def __init__(self, upperTime, lowerTime):
        self.upperTime = self.convertTo24Hours(upperTime)
        self.lowerTime = self.convertTo24Hours(lowerTime)

    def isTimeInRange(self, upper, lower, now):
        outcome = False
        if now.time().replace(microsecond=0) < upper.time() and now.time().replace(microsecond=0) > lower.time():
            outcome = True
        else:
            outcome = False
        return outcome

    def convertTo24Hours(self, time):
        convertedTime = datetime.datetime.strptime(time, "%I:%M:%S %p")
        return convertedTime

    def getUpperTime(self):
        return self.upperTime

    def getLowerTime(self):
        return self.lowerTime
