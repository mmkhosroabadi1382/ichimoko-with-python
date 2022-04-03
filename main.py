import matplotlib.pyplot as plt
import pandas_datareader.data as wb

assets = 'TSLA'
data = wb.DataReader('TSLA', 'yahoo', '2020-1-1')

high9 = data.High.rolling(9).max()
low9 = data.High.rolling(9).min()
high26 = data.High.rolling(26).max()
low26 = data.High.rolling(26).min()
high52 = data.High.rolling(52).max()
low52 = data.High.rolling(52).min()

data['tenken_sen'] = (high9 + low9)/2
data['kijun_sen'] = (high26 + low26)/2
data['senkou_A'] = ((data.tenken_sen + data.kijun_sen)/2).shift(26)
data['senkou_B'] = ((high9 + low9)/2).shift(26)
data['chikou'] = data.Close.shift(-26)
data = data.iloc[26:]

plt.plot(data.index, data['tenken_sen'], lw=0.7)
plt.plot(data.index, data['kijun_sen'], lw=0.7)
plt.plot(data.index, data['chikou'], lw=0.7)
plt.title("Ichimoko en:" + str(assets))
plt.ylabel("Precio")
komu = data['Adj Close'].plot(lw=1.5)
komu.fill_between(data.index, data.senkou_A, data.senkou_B, where=data.senkou_A >= data.senkou_B)
komu.fill_between(data.index, data.senkou_A, data.senkou_B, where=data.senkou_A < data.senkou_B)

plt.show()