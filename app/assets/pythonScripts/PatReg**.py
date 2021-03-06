import  matplotlib
import numpy as np
import  matplotlib.pyplot as plt
import  matplotlib.ticker as mticker
import matplotlib.dates as mdates
import datetime
import MySQLdb
from pandas import DataFrame
import pandas as pd
import pandas.io.sql as psql
import time
import datetime

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')

cursor = mydb.cursor()
sql='SELECT price_close,price_date,stock_tickers FROM stock_historic_data'
price = psql.read_sql(sql, mydb)

#########GLOBAL VAR####################33

##date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack=True ,
##                         delimiter=',',
##                         converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
##
##                     
#######################################################
def percentChange(startPoint, currentPoint):
    try:
        x = (float(currentPoint-startPoint)/abs(startPoint)) * 100
        if x == 0.0:
            return 0.0000000001
        else:
            return x
    except:
        return 0.0000000001
#####################################################################
    
def patternStorage():
    x = len(numpyMatrix)-60
    print x
    y = 30
    while y <x: 
        pattern=[]
        p1 = percentChange(numpyMatrix[y-30],numpyMatrix[y-29])
        p2 = percentChange(numpyMatrix[y-30],numpyMatrix[y-28])
        p3 = percentChange(numpyMatrix[y-30],numpyMatrix[y-27])
        p4 = percentChange(numpyMatrix[y-30],numpyMatrix[y-26])
        p5 = percentChange(numpyMatrix[y-30],numpyMatrix[y-25])
        p6 = percentChange(numpyMatrix[y-30],numpyMatrix[y-24])
        p7 = percentChange(numpyMatrix[y-30],numpyMatrix[y-23])
        p8 = percentChange(numpyMatrix[y-30],numpyMatrix[y-22])
        p9 = percentChange(numpyMatrix[y-30],numpyMatrix[y-21])
        p10 = percentChange(numpyMatrix[y-30],numpyMatrix[y-20])

        p11 = percentChange(numpyMatrix[y-30],numpyMatrix[y-19])
        p12 = percentChange(numpyMatrix[y-30],numpyMatrix[y-18])
        p13 = percentChange(numpyMatrix[y-30],numpyMatrix[y-17])
        p14 = percentChange(numpyMatrix[y-30],numpyMatrix[y-16])
        p15 = percentChange(numpyMatrix[y-30],numpyMatrix[y-15])
        p16 = percentChange(numpyMatrix[y-30],numpyMatrix[y-14])
        p17 = percentChange(numpyMatrix[y-30],numpyMatrix[y-13])
        p18 = percentChange(numpyMatrix[y-30],numpyMatrix[y-12])
        p19 = percentChange(numpyMatrix[y-30],numpyMatrix[y-11])
        p20 = percentChange(numpyMatrix[y-30],numpyMatrix[y-10])

        p21 = percentChange(numpyMatrix[y-30],numpyMatrix[y-9])
        p22 = percentChange(numpyMatrix[y-30],numpyMatrix[y-8])
        p23 = percentChange(numpyMatrix[y-30],numpyMatrix[y-7])
        p24 = percentChange(numpyMatrix[y-30],numpyMatrix[y-6])
        p25 = percentChange(numpyMatrix[y-30],numpyMatrix[y-5])
        p26 = percentChange(numpyMatrix[y-30],numpyMatrix[y-4])
        p27 = percentChange(numpyMatrix[y-30],numpyMatrix[y-3])
        p28 = percentChange(numpyMatrix[y-30],numpyMatrix[y-2])
        p29 = percentChange(numpyMatrix[y-30],numpyMatrix[y-1])
        p30 = percentChange(numpyMatrix[y-30],numpyMatrix[y])

        outcomeRange = numpyresult[y+20:y+30]
        currentPoint = numpyresult[y]
        print ' this is current point' , currentPoint
        print ' the date ', numpydate[y]
        
        try:
            avgOutcome=reduce(lambda x,y: x+y, outcomeRange)/len(outcomeRange)
        except Exception,e:
            print str(e)
            avgOutcome=0

        futureOutcome = percentChange(currentPoint,avgOutcome)

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)
        
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        y+=1

##################################################################################            
def currentPattern():
    print numpydate[-1]
    
    cp1 = percentChange(numpyMatrix [-31],numpyMatrix [-30])
    cp2 = percentChange(numpyMatrix [-31],numpyMatrix [-29])
    cp3 = percentChange(numpyMatrix [-31],numpyMatrix [-28])
    cp4 = percentChange(numpyMatrix [-31],numpyMatrix [-27])
    cp5 = percentChange(numpyMatrix [-31],numpyMatrix [-26])
    cp6 = percentChange(numpyMatrix [-31],numpyMatrix [-25])
    cp7 = percentChange(numpyMatrix [-31],numpyMatrix [-24])
    cp8 = percentChange(numpyMatrix [-31],numpyMatrix [-23])
    cp9 = percentChange(numpyMatrix [-31],numpyMatrix [-22])
    cp10 = percentChange(numpyMatrix [-31],numpyMatrix [-21])

    cp11 = percentChange(numpyMatrix [-31],numpyMatrix [-20])
    cp12 = percentChange(numpyMatrix [-31],numpyMatrix [-19])
    cp13 = percentChange(numpyMatrix [-31],numpyMatrix [-18])
    cp14 = percentChange(numpyMatrix [-31],numpyMatrix [-17])
    cp15 = percentChange(numpyMatrix [-31],numpyMatrix [-16])
    cp16 = percentChange(numpyMatrix [-31],numpyMatrix [-15])
    cp17 = percentChange(numpyMatrix [-31],numpyMatrix [-14])
    cp18 = percentChange(numpyMatrix [-31],numpyMatrix [-13])
    cp19 = percentChange(numpyMatrix [-31],numpyMatrix [-12])
    cp20 = percentChange(numpyMatrix [-31],numpyMatrix [-11])

    cp21 = percentChange(numpyMatrix [-31],numpyMatrix [-10])
    cp22 = percentChange(numpyMatrix [-31],numpyMatrix [-9])
    cp23 = percentChange(numpyMatrix [-31],numpyMatrix [-8])
    cp24 = percentChange(numpyMatrix [-31],numpyMatrix [-7])
    cp25 = percentChange(numpyMatrix [-31],numpyMatrix [-6])
    cp26 = percentChange(numpyMatrix [-31],numpyMatrix [-5])
    cp27 = percentChange(numpyMatrix [-31],numpyMatrix [-4])
    cp28 = percentChange(numpyMatrix [-31],numpyMatrix [-3])
    cp29 = percentChange(numpyMatrix [-31],numpyMatrix [-2])
    cp30 = percentChange(numpyMatrix [-31],numpyMatrix [-1])

    patterntoReg.append(cp1)
    patterntoReg.append(cp2)
    patterntoReg.append(cp3)
    patterntoReg.append(cp4)
    patterntoReg.append(cp5)
    patterntoReg.append(cp6)
    patterntoReg.append(cp7)
    patterntoReg.append(cp8)
    patterntoReg.append(cp9)
    patterntoReg.append(cp10)
    
    patterntoReg.append(cp11)
    patterntoReg.append(cp12)
    patterntoReg.append(cp13)
    patterntoReg.append(cp14)
    patterntoReg.append(cp15)
    patterntoReg.append(cp16)
    patterntoReg.append(cp17)
    patterntoReg.append(cp18)
    patterntoReg.append(cp19)
    patterntoReg.append(cp20)
    
    patterntoReg.append(cp21)
    patterntoReg.append(cp22)
    patterntoReg.append(cp23)
    patterntoReg.append(cp24)
    patterntoReg.append(cp25)
    patterntoReg.append(cp26)
    patterntoReg.append(cp27)
    patterntoReg.append(cp28)
    patterntoReg.append(cp29)
    patterntoReg.append(cp30)

    x=31
    while x>0:
        datearray.append(numpydate[-x])
        x-=1
##############################################################################
def patternReg():
    
    avgpchange=0
    patfound=0
    plotpatAr=[]
    
    for eachPattern in patternAr:
        sim1 = 100.00 - abs(percentChange(eachPattern[0], patterntoReg[0]))
        sim2 = 100.00 - abs(percentChange(eachPattern[1], patterntoReg[1]))
        sim3 = 100.00 - abs(percentChange(eachPattern[2], patterntoReg[2]))
        sim4 = 100.00 - abs(percentChange(eachPattern[3], patterntoReg[3]))
        sim5 = 100.00 - abs(percentChange(eachPattern[4], patterntoReg[4]))
        sim6 = 100.00 - abs(percentChange(eachPattern[5], patterntoReg[5]))
        sim7 = 100.00 - abs(percentChange(eachPattern[6], patterntoReg[6]))
        sim8 = 100.00 - abs(percentChange(eachPattern[7], patterntoReg[7]))
        sim9 = 100.00 - abs(percentChange(eachPattern[8], patterntoReg[8]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9], patterntoReg[9]))

        sim11 = 100.00 - abs(percentChange(eachPattern[10], patterntoReg[10]))
        sim12 = 100.00 - abs(percentChange(eachPattern[11], patterntoReg[11]))
        sim13 = 100.00 - abs(percentChange(eachPattern[12], patterntoReg[12]))
        sim14 = 100.00 - abs(percentChange(eachPattern[13], patterntoReg[13]))
        sim15 = 100.00 - abs(percentChange(eachPattern[14], patterntoReg[14]))
        sim16 = 100.00 - abs(percentChange(eachPattern[15], patterntoReg[15]))
        sim17 = 100.00 - abs(percentChange(eachPattern[16], patterntoReg[16]))
        sim18 = 100.00 - abs(percentChange(eachPattern[17], patterntoReg[17]))
        sim19 = 100.00 - abs(percentChange(eachPattern[18], patterntoReg[18]))
        sim20 = 100.00 - abs(percentChange(eachPattern[19], patterntoReg[19]))

        sim21 = 100.00 - abs(percentChange(eachPattern[20], patterntoReg[20]))
        sim22 = 100.00 - abs(percentChange(eachPattern[21], patterntoReg[21]))
        sim23 = 100.00 - abs(percentChange(eachPattern[22], patterntoReg[22]))
        sim24 = 100.00 - abs(percentChange(eachPattern[23], patterntoReg[23]))
        sim25 = 100.00 - abs(percentChange(eachPattern[24], patterntoReg[24]))
        sim26 = 100.00 - abs(percentChange(eachPattern[25], patterntoReg[25]))
        sim27 = 100.00 - abs(percentChange(eachPattern[26], patterntoReg[26]))
        sim28 = 100.00 - abs(percentChange(eachPattern[27], patterntoReg[27]))
        sim29 = 100.00 - abs(percentChange(eachPattern[28], patterntoReg[28]))
        sim30 = 100.00 - abs(percentChange(eachPattern[29], patterntoReg[29]))


        howSim = float(sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+
                       sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+
                       sim21+sim22+sim23+sim24+sim25+sim26+sim27+sim28+sim29+sim30)/30.00
        if howSim>20:
            patdex = patternAr.index(eachPattern)
            patfound = 1
            plotpatAr.append(eachPattern) 
            print ' performance  : ', performanceAr[patdex]
            avgpchange += performanceAr[patdex]
            print ' AVERAGE ', avgpchange

      
    now = datetime.date.today().strftime("%Y-%B-%d")
    xp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    if patfound==1:
        fig = plt.figure(figsize=(10,6))
        for eachPatt in plotpatAr:
            futurepoints = patternAr.index(eachPatt)
            if performanceAr[futurepoints] > patterntoReg[29]:
                pcolor ='#24bc00'
            else:
                pcolor = '#d40000'
            fig.suptitle(numpystock[0]+' as of '+now , fontsize=20)
            plt.plot(xp,eachPatt)
            plt.plot(xp,patterntoReg,c="#00ff00",linewidth=5)
            plt.scatter(35,performanceAr[futurepoints],c=pcolor, alpha=.3)  
        avgpercentchange= avgpchange/len(plotpatAr)
        print ' avg ',avgpercentchange
        if avgpercentchange> patterntoReg[29]:
            pcolor = '#39ff33'
        else:
            pcolor = '#ff3333'
        plt.scatter(40,avgpercentchange,c=pcolor)
        plt.plot(xp,patterntoReg, '#54fff7',linewidth=3)
        plt.grid(True)
        plt.show()
        print 'patfound 30'
    elif patfound==0:
        ifcompanyNew()
#############################################################################
def ifcompanyNew():
    patterntoReg=[]
    patternAr=[]
    performanceAr=[]
    
    x = len(numpyMatrix)-30
    print x
    y = 11
    
    while y <x:
        pattern=[]
        p1 = percentChange(numpyMatrix[y-10],numpyMatrix[y-9])
        p2 = percentChange(numpyMatrix[y-10],numpyMatrix[y-8])
        p3 = percentChange(numpyMatrix[y-10],numpyMatrix[y-7])
        p4 = percentChange(numpyMatrix[y-10],numpyMatrix[y-6])
        p5 = percentChange(numpyMatrix[y-10],numpyMatrix[y-5])
        p6 = percentChange(numpyMatrix[y-10],numpyMatrix[y-4])
        p7 = percentChange(numpyMatrix[y-10],numpyMatrix[y-3])
        p8 = percentChange(numpyMatrix[y-10],numpyMatrix[y-2])
        p9 = percentChange(numpyMatrix[y-10],numpyMatrix[y-1])
        p10 = percentChange(numpyMatrix[y-10],numpyMatrix[y])
        
        outcomeRange = numpyresult[y+20:y+30]
        currentPoint = numpyresult[y]
        print 'while'
        try:
            avgOutcome=reduce(lambda x,y: x+y, outcomeRange)/len(outcomeRange)
        except Exception,e:
            print str(e)
            avgOutcome=0

        futureOutcome = percentChange(currentPoint,avgOutcome)

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)
        print 'append past  pattern'
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        y+=1
    print ' curent pattern' , numpydate[-1]
    cp1 = percentChange(numpyMatrix [-11],numpyMatrix [-10])
    cp2 = percentChange(numpyMatrix [-11],numpyMatrix [-9])
    cp3 = percentChange(numpyMatrix [-11],numpyMatrix [-8])
    cp4 = percentChange(numpyMatrix [-11],numpyMatrix [-7])
    cp5 = percentChange(numpyMatrix [-11],numpyMatrix [-6])
    cp6 = percentChange(numpyMatrix [-11],numpyMatrix [-5])
    cp7 = percentChange(numpyMatrix [-11],numpyMatrix [-4])
    cp8 = percentChange(numpyMatrix [-11],numpyMatrix [-3])
    cp9 = percentChange(numpyMatrix [-11],numpyMatrix [-2])
    cp10 = percentChange(numpyMatrix [-11],numpyMatrix [-1])
    
    patterntoReg.append(cp1)
    patterntoReg.append(cp2)
    patterntoReg.append(cp3)
    patterntoReg.append(cp4)
    patterntoReg.append(cp5)
    patterntoReg.append(cp6)
    patterntoReg.append(cp7)
    patterntoReg.append(cp8)
    patterntoReg.append(cp9)
    patterntoReg.append(cp10)
    print 'append current pattern'
    avgpchange=0
    patfound=0
    plotpatAr=[]
    
    for eachPattern in patternAr:
        sim1 = 100.00 - abs(percentChange(eachPattern[0], patterntoReg[0]))
        sim2 = 100.00 - abs(percentChange(eachPattern[1], patterntoReg[1]))
        sim3 = 100.00 - abs(percentChange(eachPattern[2], patterntoReg[2]))
        sim4 = 100.00 - abs(percentChange(eachPattern[3], patterntoReg[3]))
        sim5 = 100.00 - abs(percentChange(eachPattern[4], patterntoReg[4]))
        sim6 = 100.00 - abs(percentChange(eachPattern[5], patterntoReg[5]))
        sim7 = 100.00 - abs(percentChange(eachPattern[6], patterntoReg[6]))
        sim8 = 100.00 - abs(percentChange(eachPattern[7], patterntoReg[7]))
        sim9 = 100.00 - abs(percentChange(eachPattern[8], patterntoReg[8]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9], patterntoReg[9]))

        howSim = float(sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10)/10.00
        
        if howSim>40:
            patdex = patternAr.index(eachPattern)
            patfound = 1
            plotpatAr.append(eachPattern) 
            print ' performance  : ', performanceAr[patdex]
            avgpchange += performanceAr[patdex]
            print ' AVERAGE ', avgpchange
            
      
    now = datetime.date.today().strftime("%Y-%B-%d")
    xp = [1,2,3,4,5,6,7,8,9,10]
    if patfound==1:
        print ' patfound'
        
        fig = plt.figure(figsize=(10,6))
        for eachPat in plotpatAr:
            futurepoints = patternAr.index(eachPat)
            if performanceAr[futurepoints] > patterntoReg[9]:
                pcolor = '#24bc00'
            else:
                pcolor = '#d40000'
            fig.suptitle(numpystock[0]+' as of '+now , fontsize=20)
            plt.plot(xp,eachPat)
            plt.plot(xp,patterntoReg,c="#00ff00",linewidth=5)
            plt.scatter(15,performanceAr[futurepoints],c=pcolor, alpha=.3)

           
        avgpercentchange= avgpchange/len(plotpatAr)
        print ' avg ',avgpercentchange
        if avgpercentchange> patterntoReg[9]:
                pcolor = '#39ff33'
        else:
            pcolor = '#ff3333'
        plt.scatter(20,avgpercentchange,c=pcolor)
        plt.plot(xp,patterntoReg, '#54fff7',linewidth=3)
        plt.grid(True)
        plt.show()
        
        
##############  MAIN   ################################################################3

close= pd.to_numeric(price['price_close'])
date =(price['price_date']).astype(str)
stock=(price['stock_tickers']).astype(str)
numpystock= np.array(stock)
numpydate=np.array(date)
numpyresult= np.array(close)
#############################3
dataLength = int(close.shape[0])
print " data length : " , dataLength

##towhat= dataLength
numpyMatrix=numpyresult
print ' numpyyy before to what', int(numpyMatrix.shape[0])
##numpyMatrix=numpyMatrix[:towhat]
##print int(numpyMatrix.shape[0])
datearray=[]

patternAr=[]
performanceAr=[]
patterntoReg=[]

patternStorage()
currentPattern()
patternReg()
##ifcompanyNew()


