import pandas as pd

import downloader as d
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib as mpl

if __name__ == '__main__':
    data_f = d.get_data()
    l = len(data_f)


    #print(data_f)
    data_visualization = pd.DataFrame({'time': [], 'value': [], 'color': []})
    for i in range(l):

        volume = data_f.iloc[i]['volume']
        delta_candle = data_f.iloc[i]['close']-data_f.iloc[i]['open']
        big_cat_or_consensus = delta_candle/volume
        bcoc = float(big_cat_or_consensus)
        r = round(bcoc, 10)
        print(str(data_f.iloc[i]['time'])+'   '+'{:.10f}'.format(r))
        c = ''
        if r >= 0 :
            c = 'green'
        else :
            c = 'red'

        data_visualization.loc[len(data_visualization.index)] = [r, data_f.iloc[i]['time'], c]

    #print(data_visualization)

    plt.title('consensus')


    plt.scatter(data_visualization["value"], data_visualization["time"],c = data_visualization["color"])

    plt.show()

