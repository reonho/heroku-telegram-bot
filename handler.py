import json
from pprint import pprint

with open('bus_routes.json') as f:
    data = json.load(f)

with open('stops.json') as c:
    data2 = json.load(c)


class stopnum:
    def __init__(self, stop):
        self.stopc = stop

    def times(self, dayind):        
        ans = ""
        day = ["WD_LastBus","SAT_LastBus","SAT_LastBus"]

        for dics in data:
            if dics["BusStopCode"] == self.stopc:
                stop = "Stop "
                try:
                    stop = data2[dics["BusStopCode"]][2]
                except:
                    stop += stopc
                ans += dics["ServiceNo"] + " : " + dics[day[dayind]] + "\n"
        ans = stop + "\n" + ans
        return ans
   


