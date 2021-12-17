import yfinance as yf
import mplfinance as mpf
import matplotlib.animation as animation

ticker = 'AAPL'
start = '2021-12-13'
interval = '5m'

data = yf.download(tickers=ticker, start=start, period='1d', interval=interval)
print(data)

col = mpf.make_marketcolors(up='#ff8500', down='#1b90a7', inherit=True)
sty = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=col)

data['vwap'] =(((data['High'] + data['Low'])/ 2) * data['Volume']).cumsum() / data['Volume'].cumsum()
add = mpf.make_addplot(data['vwap'])

kwargs = dict(type='candle', volume=True, style=sty, mav=(6, 12), addplot=add)
#mpf.plot(data, **kwargs)

warmup=20
_add = mpf.make_addplot(data.iloc[0:warmup]['vwap'])
_kwargs = dict(type='candle', volume=True, style=sty, mav=(6,12), addplot=_add, title=ticker+ " " + interval + '' + start)

fig, axes = mpf.plot(data.iloc[0:warmup], returnfig=True, **_kwargs)
ax1 = axes[0]
ax2 = axes[2]

def animate(i):
    _data = data.iloc[0:(warmup+i)]
    _add = mpf.make_addplot(_data['vwap'], ax=ax1)
    ax1.clear()
    ax2.clear()
    _kwargs = dict(type='candle', style=sty, mav=(6,12), addplot=_add)
    mpf.plot(_data, ax=ax1, volume=ax2, returnfig=True, **_kwargs)

ani = animation.FuncAnimation(fig, animate, interval=100)
mpf.show()

