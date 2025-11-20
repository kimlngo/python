import datetime

mytime = datetime.time(2,20)
today = datetime.date.today()
print(mytime)
print(today)
print(today.ctime())

timenow = datetime.datetime(2025,11,20,16,4,6)
print(timenow)
#change the date time
timenow = timenow.replace(year=2026)
print(f'timenow changed: {timenow}')

#date calculation
startDate = datetime.date(2025,11,20)
endDate = datetime.date(2026,2,17)
dateDelta = endDate - startDate
print(f'type of dateDelta: {type(dateDelta)}') #<class 'datetime.timedelta'>
print(f'How many days till CNY? {dateDelta.days}') #89

#Date time Calculation
end = datetime.datetime(2026,11,20,16,14,20)
start = datetime.datetime(2025,11,20,6,14,20)

dateTimeDelta = end - start
print(dateTimeDelta) #datetime.timedelta(days=365, seconds=36000)
print(dateTimeDelta.days) #365
print(dateTimeDelta.seconds) #36000