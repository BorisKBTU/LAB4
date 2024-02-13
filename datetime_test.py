import datetime
import random


class Date_time(datetime.date):
    @staticmethod
    def print_5_days():
        current_date = Date_time.today()
        print(f'Current date: {current_date}')
        difference = datetime.timedelta(days=5)
        print(f'Minus five days: {current_date - difference}')

    @staticmethod
    def print_days():
        current_date = Date_time.today()
        print(f'Yesterday was: {current_date - datetime.timedelta(days=1)}')
        print(f'Current date: {current_date}')
        print(f'Tomorrow: {current_date - datetime.timedelta(days=-1)}')

    @staticmethod
    def drop_milliseconds():
        print(f'Time: {datetime.datetime.now().time()}')
        print(f'Time without milliseconds: {datetime.datetime.now().time().strftime("%H:%M:%S")}')

    @staticmethod
    def difference_date(date1, date2):
        print(date1)
        print(date2)
        print(f'Difference in dates: {abs((date2 - date1).total_seconds())}')


date_obj = Date_time
date_obj.print_5_days()
print('-' * 60)
date_obj.print_days()
print('-' * 60)
date_obj.drop_milliseconds()
print('-' * 60)
year1, month1, day1 = random.randint(0, 2024), random.randint(1, 12), random.randint(0, 28)
year2, month2, day2 = random.randint(0, 2024), random.randint(1, 12), random.randint(0, 28)
date_obj.difference_date(date1=datetime.date(year1, month1, day1), date2=datetime.date(year2, month2, day2))
