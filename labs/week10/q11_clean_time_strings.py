# Q11: strip square brackets from the time column
import pandas as pd

logFilename = "labs/week10/data/access.log.demo"
colNames = ('ip','dash1','userId','time','url','status code',
            'size of response','referer','user agent','dunno')

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

# a quick, readable way: strip the first char '[' and trailing ']'
df['time'] = df['time'].str.strip('[]')

print(df['time'].head(3))
