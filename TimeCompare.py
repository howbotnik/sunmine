import datetime

class TimeCompare:
    upperTime = None
    lowerTime = None
    now = datetime.datetime.now()

    def __init__(self, upperTime, lowerTime):
        self.upperTime = self.convertTo24Hours(upperTime)
        self.lowerTime = self.convertTo24Hours(lowerTime)

    def isTimeInRange(self):
        outcome = False
        if self.now.time().replace(microsecond=0) < self.upperTime.time() and self.now.time().replace(microsecond=0) > self.lowerTime.time():
            outcome = True
        else:
            outcome = False
        return outcome

    def convertTo24Hours(self, time):
        convertedTime = datetime.datetime.strptime(time, "%I:%M:%S %p")
        return convertedTime
