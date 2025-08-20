# Q15: resample mean 'size of response' every 30 minutes
import pandas as pd

logFilename = "labs/week10/data/access.log.demo"
colNames = ('ip','dash1','userId','time','url','status code',
            'size of response','referer','user agent','dunno')

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)
df['time'] = pd.to_datetime(df['time'].str.strip('[]'), format='%d/%b/%Y:%H:%M:%S')

# set datetime index so resample works
df = df.set_index('time')

downloadSamples = df['size of response'].resample('30Min').mean(numeric_only=True)
print(downloadSamples)