def add_rolling(df, n):
    sn = str(n)
    for c in ['time', '_crossTime', 'f2l', 'pllTime', 'ollTime']:
        c_rolling = c.strip('_') + sn
        df [c_rolling] = df[c].rolling(n).mean()
        df [c_rolling + 'N'] = df[c_rolling] / df ['time' + sn]


def plot_rolling(df, n):
    sn = str(n)
    df[['time' + sn, 'crossTime' + sn, 'f2l' + sn, 'pllTime' + sn, 'ollTime' + sn]].plot()


def plot_rollingN(df, n):
    sn = str(n)
    df[['f2l' + sn + 'N', 'crossTime' + sn + 'N', 'pllTime' + sn + 'N', 'ollTime' + sn + 'N']].plot()
