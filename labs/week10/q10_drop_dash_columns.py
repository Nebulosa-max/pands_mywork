# Q10: drop dash-only columns
import pandas as pd

logFilename = "labs/week10/data/access.log.demo"
colNames = ('ip','dash1','userId','time','url','status code',
            'size of response','referer','user agent','dunno')

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

# drop columns that are just '-' values
df.drop(columns=['dash1', 'userId'], inplace=True)

print(df.head())
print("\nColumns now:", df.columns.tolist())