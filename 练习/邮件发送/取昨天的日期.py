import datetime

def getYesterday():
    today = datetime.date.today()
    yesterday = (today - datetime.timedelta(days=1)).strftime('%Y%m%d')
    print(yesterday)
    return yesterday

getYesterday()