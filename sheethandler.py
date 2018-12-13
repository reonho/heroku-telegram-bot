import csv
import datetime


class sheethandler:
    def __init__(self):
        with open("sheet1.csv", encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
        self.data = data

    def time(self, station):
        text = None 
        weekno = datetime.datetime.today().weekday()
        if weekno == 6:
            filt = "Sunday"
        elif weekno == 5:
            filt = "Saturday"
        else:
            filt = "Weekdays"
        for row in self.data:
            stat,first1, first2, last1, last2, day, dir1, dir2 = row
            if day != filt:
                continue
            if station.lower() in stat.lower():
                text = stat + " : " + "\n" + "Towards " + dir1 + " - " + last1 + "\n" + "Towards " + dir2 + " - " + last2

        return text

