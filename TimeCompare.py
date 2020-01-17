import datetime


class TimeCompare:
    upperTime = None
    lowerTime = None

    def __init__(self, upper_time, lower_time):
        self.upperTime = self.convert_to_24_hours(upper_time)
        self.lowerTime = self.convert_to_24_hours(lower_time)

    @staticmethod
    def is_time_in_range(upper, lower, now):
        outcome = False
        if upper.time() > now.time().replace(microsecond=0) > lower.time():
            outcome = True
        else:
            outcome = False
        return outcome

    @staticmethod
    def convert_to_24_hours(time):
        converted_time = datetime.datetime.strptime(time, "%I:%M:%S %p")
        return converted_time

    def get_upper_time(self):
        return self.upperTime

    def get_lower_time(self):
        return self.lowerTime
