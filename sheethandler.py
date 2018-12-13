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
        if len(station) < 3:
            return ""
        text = ""
        weekno = datetime.datetime.today().weekday()
        if weekno == 6:
            filt = "Sunday"
        elif weekno == 5:
            filt = "Saturday"
        else:
            filt = "Weekdays"
        res = {}
        for row in self.data:
            stat,first1, first2, last1, last2, day, dir1, dir2 = row
            if day != filt:
                continue
            elif station.lower() in stat.lower():
                if stat not in res:
                    res[stat] = "Towards " + dir1 + " - " + last1 + "\n" + "Towards " + dir2 + " - " + last2 + "\n"
                else:
                    res[stat] += "Towards " + dir1 + " - " + last1 + "\n" + "Towards " + dir2 + " - " + last2 + "\n"
        for pair in res.items():
            text += "\n" + pair[0] + " : \n" + pair[1]
        if text:
            return filt + "\n" +  text
        else:
            return text 

s1 = sheethandler()
print(s1.time("little india"))
