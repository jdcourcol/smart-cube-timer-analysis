def add_rolling(df, n):
    sn = str(n)
    df['time' + sn] = df['time'].rolling(n).mean()
    df['f2l' + sn] = df['f2l'].rolling(n).mean()
    df['pllTime' + sn] = df['_pllTime'].rolling(n).mean()
    df['ollTime' + sn] = df['_ollTime'].rolling(n).mean()
    df['f2l' + sn + 'N'] = df['f2l' + sn] / df['time' + sn]
    df['pllTime' + sn + 'N'] = df['pllTime' + sn] / df['time' + sn]
    df['ollTime' + sn + 'N'] = df['ollTime' + sn] / df['time' + sn]


def plot_rolling(df, n):
    sn = str(n)
    df[['time' + sn, 'f2l' + sn, 'pllTime' + sn, 'ollTime' + sn]].plot()


def plot_rollingN(df, n):
    sn = str(n)
    df[['f2l' + sn + 'N', 'pllTime' + sn + 'N', 'ollTime' + sn + 'N']].plot()
