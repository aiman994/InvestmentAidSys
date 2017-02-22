import time
import datetime
import numpy as np
import matplotlib.pyplot as plt ,mpld3
import matplotlib.ticker as mticker
import matplotlib.dates as mdates


eachStock = 'AAPL'


def graphData(stock):

    plt.style.use("ggplot")

    try:
        stockFile = stock +'.txt'
        
        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',', unpack=True, converters={ 0: mdates.strpdate2num('%Y%m%d')})
        
        fig = plt.figure(facecolor='k')
        ax1 = plt.subplot(1,1,1)
        ax1.plot(date,openp)
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        '''ax1 = plt.plot( x="date")'''
     
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        
        mpld3.save_html(fig, "./mpld3demo.html")
        mpld3.fig_to_html(fig,template_type="general")
        mpld3.show()
        '''print mpld3.fig_to_html(fig,template_type="general")'''
    except Exception, e:
        print 'failed main loop',str(e)

    

graphData(eachStock)
