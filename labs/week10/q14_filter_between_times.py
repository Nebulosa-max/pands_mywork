# Q14: get events between two datetimes
import pandas as pd

logFilename = "labs/week10/data/access.log.demo"
colNames = ('ip','dash1','userId','time','url','status code',
            'size of response','referer','user agent','dunno')

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)
df['time'] = pd.to_datetime(df['time'].str.strip('[]'), format='%d/%b/%Y:%H:%M:%S')

start_date = pd.Timestamp('2021-02-15 23:00:00')
end_date   = pd.Timestamp('2021-02-15 23:59:59')

between = df[(df['time'] > start_date) & (df['time'] < end_date)]
print(between.head())
print("\nCount in window:", len(between))