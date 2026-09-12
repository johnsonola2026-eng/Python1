import random
import time
def getrandomdate(start_date,end_date):
    print("printing random date between,start date and end date")
    randomGenerator=random.random()
    dateformat="%m/%d/%Y"
    startTime=time.mktime(time.strptime(start_date,dateformat))
    endTime=time.mktime(time.strptime(end_date,dateformat))
    randomTime=startTime+(randomGenerator*(endTime-startTime))
    randomDate=time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
print("random date=",getrandomdate("1/1/2016","12/12/2018"))