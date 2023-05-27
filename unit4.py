class unit4:
    def translate(self,sentence):
        words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
        trans = ' '.join(words.get(word, word) for word in sentence.split())
        return trans
    def is_prime(self,n):
        # Corner case
        if n <= 1:
            return False
        # Check from 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def first_prime_over(self,n):
        return next(num for num in range(n + 1, n + 2 * (n + 1)) if self.is_prime(num))

    def parse_ranges(self,str):
        ranges = (range_str.split('-') for range_str in str.split(','))
        final_numbers = (num for start, stop in ranges for num in range(int(start), int(stop) + 1))
        return final_numbers

    def get_fibo(self):
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def gen_secs(self):
        sec = 0
        while sec < 60:
            yield sec
            sec += 1

    def gen_minutes(self):
        minute = 0
        while minute < 60:
            yield minute
            minute += 1

    def gen_hours(self):
        hour = 0
        while hour < 24:
            yield hour
            hour += 1
    def gen_time(self):
        for hour in self.gen_hours():
            for minute in self.gen_minutes():
                for sec in self.gen_secs():
                    yield f"{hour:02d}:{minute:02d}:{sec:02d}"

    def gen_years(self,start=2019):
        year = start
        while True:
            yield year
            year += 1

    def gen_months(self):
        month = 1
        while month <= 12:
            yield month
            month += 1

    def gen_days(self,month, leap_year=True):
        if(leap_year):
            February=29
        else:
            February=28
        days_in_month = [
            31,  # January
             February,
            31,  # March
            30,  # April
             31,  # May
             30,  # June
             31,  # July
             31,  # August
            30,  # September
            31,  # October
             30,  # November
             31  # December
        ]
        yield days_in_month[month-1]

    def is_leap(self,year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def gen_date(self):
        months = self.gen_months()
        minutes = self.gen_minutes()
        years = self.gen_years()
        secs = self.gen_secs()
        for year in years:
               for month in months:
                   for day in range(1,next(self.gen_days(month, self.is_leap(year)))+1):
                       for hour in self.gen_hours():
                           for minute in minutes:
                               for sec in secs:
                                   yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{sec:02d}"



if __name__ == '__main__':
    unit = unit4()
    print(unit.translate("el gato esta en la casa"))
    print(unit.first_prime_over(1000000))
    print(list(unit.parse_ranges("0-0,4-8,20-21,43-45")))
    fibo_gen = unit.get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    #for gt in unit.gen_time():
    #    print(gt)
    gen_date_obj = unit.gen_date()

    for i in range(1,100000000000):
           da=next(gen_date_obj)
           if i%2 ==0:
               print(da)
