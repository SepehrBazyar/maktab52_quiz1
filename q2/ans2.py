# Written by: Sepehr Bazyar
# jalali datetime: date ad datetime to converting
from jdatetime import date, datetime
# for highlighting input and output functions
from typing import Counter, Generator, Literal
import argparse

if __name__ == '__main__':  # run just when run this program not import at other program
    parser = argparse.ArgumentParser(description="<Guess Number Game>")
    parser.add_argument('-s', '--start_date', metavar='START', action='store', type=str,
                        help='Start of Point Number(Lower Bound)')  # int number for start default value is 0
    parser.add_argument('-e', '--end_date', metavar='END', action='store', type=str,
                        help='End of Point Number(Upper Bound)')  # int number for end default value is 100
    parser.add_argument('-w', '--week_date', metavar='TIMES', action='store', type=int,
                        help='Times of Game(Round for Guess Number)')  # int number for round default value is 5
    args = parser.parse_args()


# fixing weekday date
def normalize(day: date, w_day: Literal[0, 1, 2, 3, 4, 5, 6]) -> date:
    counter = day
    while counter.weekday() != w_day:  # maximum 6 day to fixing
        try:  # next day
            counter = date(counter.year, counter.month, counter.day + 1)
        except:
            try:  # next month(first day of next month)
                counter = date(counter.year, counter.month + 1, 1)
            except:  # next year(first day of first month new year)
                counter = date(counter.year + 1, 1, 1)
    return counter


class WeekdayGen:
    def __init__(self, s_day: str, e_day: str, w_day: Literal[0, 1, 2, 3, 4, 5, 6]) -> Generator:
        # parse datetime from the string
        self.start = datetime.strptime(s_day, "%Y/%m/%d").date()
        # convert to date for remove time
        self.end = datetime.strptime(e_day, "%Y/%m/%d").date()
        # find starting day that right weekday
        self.counter = normalize(self.start, w_day)
        self.w_day = w_day

    def __iter__(self):
        self.counter = normalize(date(self.counter.year, self.counter.month,
                                      self.counter.day - 1), self.w_day)
        return self

    def __next__(self):
        if self.counter <= self.end:  # less than for date object is correct comparison
            try:  # 7 day later this week day in next week
                counter = date(self.counter.year,
                               self.counter.month, self.counter.day + 7)
            except:
                try:  # next month(because maybe 31 or 30 day can't use % operation)
                    counter = normalize(
                        date(self.counter.year, self.counter.month + 1, 1), self.w_day)
                except:
                    counter = normalize(
                        date(self.counter.year + 1, 1, 1), self.w_day)
            return self.counter.strftime("%d %B %Y")
        raise StopIteration("ended!")


for item in WeekdayGen(args.start_date, args.end_date, args.week_date):
    print(item)
