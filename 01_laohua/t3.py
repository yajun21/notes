import yfinance as yf
import mplfinance as mpf
import matplotlib.animation as animation
import pandas as pd
import pandas_ta as ta

ticker = 'AAPL'
start = '2021-12-01'
interval = '2m'

data = yf.download(tickers=ticker, start=start, period='1d', interval=interval)
col = mpf.make_marketcolors(up='#ff8500', down='#1b90a7', inherit=True)
sty = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=col)

data.ta.vwap(append=True)
data.ta.bbands(lenght=10, append=True)
# print(data)

bbu_col = [col for col in data.columns if 'BBU' in col][0]
bbl_col = [col for col in data.columns if 'BBL' in col][0]


# _add = [mpf.make_addplot(data['VWAP_D']),
#        mpf.make_addplot(data[bbu_col]),
#        mpf.make_addplot(data[bbl_col])]
#
# kwargs = dict(type='candle', volume=True, style=sty, addplot=_add)
# mpf.plot(data, **kwargs)
#

class Filter():
    def __init__(self):
        self.sig = None

    def update(self, bars):
        data = bars.iloc[-1]
        if data['Close'] > data[bbu_col]:
            self.sig = 'down'
            print("ddddddddddddd")
        elif data['Close'] < data[bbl_col]:
            self.sig = 'up'
            print("ddddddddddddd")
        else:
            self.sig = None


f = Filter()
sig = []
for i in range(data.shape[0]):
    f.update(data.iloc[:(i + 1)])
    sig.append(f.sig)

data['sig'] = sig
data['up'] = data['Low'] - 0.1
data.loc[data['sig'] != 'up', 'up'] = float('nan')
data['down'] = data['High'] + 0.1
data.loc[data['sig'] != 'down', 'down'] = float('nan')

warmup = 10
kwargs = dict(type='candle', volume=True, style=sty, title=ticker + " " + interval + '' + start)

fig, axes = mpf.plot(data.iloc[0:warmup], returnfig=True, **kwargs)
ax1 = axes[0]
ax2 = axes[2]


def animate(i):
    _data = data.iloc[0:(warmup + i)]
    add = [mpf.make_addplot(_data['VWAP_D'], ax=ax1),
           mpf.make_addplot(_data[bbu_col], ax=ax1),
           mpf.make_addplot(_data[bbl_col], ax=ax1),
           mpf.make_addplot(_data['up'], type='scatter', marker='^', color='yellow', markersize=200, ax=ax1),
           mpf.make_addplot(_data['down'], type='scatter', marker='v', color='yellow', markersize=200, ax=ax1),
           ]
    ax1.clear()
    ax2.clear()
    _kwargs = dict(type='candle', style=sty, addplot=add)
    mpf.plot(_data, ax=ax1, volume=ax2, returnfig=True, **_kwargs)


ani = animation.FuncAnimation(fig, animate, interval=10)
mpf.show()
