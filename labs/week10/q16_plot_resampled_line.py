# Q16: plot the 30-min mean series
import pandas as pd
import matplotlib.pyplot as plt

logFilename = "labs/week10/data/access.log.demo"
colNames = ('ip','dash1','userId','time','url','status code',
            'size of response','referer','user agent','dunno')

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)
df['time'] = pd.to_datetime(df['time'].str.strip('[]'), format='%d/%b/%Y:%H:%M:%S')
df = df.set_index('time')

downloadSamples = df['size of response'].resample('30Min').mean(numeric_only=True)

ax = downloadSamples.plot()
ax.set_title('Mean download size every 30 minutes')
ax.set_xlabel('time')
ax.set_ylabel('size of response (mean)')

plt.tight_layout()
plt.savefig('q16_download_samples.png')
plt.show()