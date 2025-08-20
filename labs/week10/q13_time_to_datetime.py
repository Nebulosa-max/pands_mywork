# Q13: convert time column to pandas datetime
import pandas as pd

logFilename = "labs/week10/data/access.log.demo"
colNames = ('ip','dash1','userId','time','url','status code',
            'size of response','referer','user agent','dunno')

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

# clean then convert using the given format: 15/Feb/2021:23:50:11
df['time'] = df['time'].str.strip('[]')
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

print(df[['time']].head())
print("\nDtypes now:\n", df.dtypes)