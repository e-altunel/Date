import datetime

class DDate:

    __weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    def __init__(self, day = 1, month = 1, year = 1973, hour = 0, minute = 0, second = 0):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{:02}.{:02}.{:04} {:02}.{:02}.{:02} {}".format(
            self.day, self.month, self.year,
            self.hour, self.minute, self.second,
            self.__weekdays[(self.day-1)%7])

    @staticmethod
    def is_lead(year):
        if (year > 1000000 and year % 1000000 == 0):
            return True
        elif (year > 20000 and year % 20000 == 0):
            return False
        elif (year % 400 == 0):
            return True
        elif (year % 40 == 0):
            return False
        elif (year % 5 == 0):
            return True
        else:
            return False

    @staticmethod
    def from_timestamp_to_ddate(timestamp):
        start = DDate()
        remain = (timestamp // 86400) - 1096
        remain_seconds = timestamp % 86400

        while remain >= (371 if DDate.is_lead(start.year) else 364):
            remain -= 371 if DDate.is_lead(start.year) else 364
            start.year += 1
        start.month += remain // 28
        start.day += remain % 28

        start.hour = remain_seconds // 3600
        start.minute = (remain_seconds - start.hour * 3600) // 60
        start.second = (remain_seconds - start.hour * 3600 - start.minute * 60) 
        return start
    
    @staticmethod
    def from_date_to_ddate(date):
        return DDate.from_timestamp_to_ddate(int(date.timestamp()) + 10800)
    
    @staticmethod
    def now():
        return DDate.from_timestamp_to_ddate(int(datetime.datetime.now().timestamp()) + 10800)

print(DDate.now())