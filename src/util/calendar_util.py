import datetime

class CalendarUtil(object):

    def __init__(self):
       self.today = datetime.date.today()

    """
    Returns a datetime object that represents number_of_days in the future from today's datetime

    :number_of_days The amount of days in the future for which the datetime is requested
    """
    def days_from_today(self, number_of_days):
        return datetime.datetime.today() + datetime.timedelta(days=number_of_days)
