
TOKUGAWA = 0
MEIJI = 1
MODERN = 2

AVG_WALKING_SPEED = 3.5
AVG_MEIJI_TRAIN = 40
AVG_MODERN_TRAIN = 150

speeds = [AVG_WALKING_SPEED, AVG_MEIJI_TRAIN, AVG_MODERN_TRAIN]

def milesPerTimePeriod(time, timePeriod):
    return round((time / 60) * speeds[timePeriod])

def minutesPerTimePeriod(miles, timePeriod):
    speed = speeds[timePeriod]
    return round((miles / speed) * 60)

def minutesToMore(minutes):
    hours = minutes // 60
    min = minutes % 60
    days = hours // 24
    hrs = hours % 24
    return days, hrs, min

    
# roads are a dictionary of 2-tuple string keys (0 is start, 1 is destination) value is distance in miles
def buildGraphFromRoadLengths(roads, timePeriod):
    result = {}
    for start,end in roads:
        time = minutesPerTimePeriod(roads[(start,end)], timePeriod)
        if start not in result:
            result[start] = {}
        if end not in result:
            result[end] = {}
        result[start][end] = time
        result[end][start] = time
    return result

# printTime(12003)

# fiveRoads = {("Kyoto", "Edo"):307, ("Kyoto", "Shimosuwa"):180,("Shimosuwa", "Edo"):134,("Edo", "Utsunomiya"):62,("Utsunomiya", "Nikko"):25,("Utsunomiya", "Shirakawa"):62}
# roadTimes = [buildGraphFromRoadLengths(fiveRoads, TOKUGAWA)]
# x = buildGraphFromRoadLengths(fiveRoads, TOKUGAWA)
# print(x)

# https://denniskawaharada.wordpress.com/edo-period-roads/ 5 roads

# https://www.oldtokyo.com/5000-mile-celebration-imperial-government-railway-1909/ Imperial Government Railway, 1909

# https://en.wikipedia.org/wiki/Shinkansen shinkansen