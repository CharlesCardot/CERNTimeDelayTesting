import pprint
import re
import csv
import numpy as np
import plotly
import plotly.plotly as py 
import plotly.graph_objs as go 
import matplotlib
import matplotlib.pyplot as plt
import statistics
from numpy.polynomial.polynomial import polyfit
pprinter = pprint.PrettyPrinter(indent=4)

barg = []

with open ('MeasuredTDValues.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        barg.append(temp)

#Format: Identifier, GFZ Channel, Measured TD Value, Predicted TD Value, Scale, Predicted TD Value (After Boost)
#Filling arrays according to above format


def create(begin, end):
    arg = []
    x=0
    while x<4:
        y=begin
        temp=[]
        while y<end:
            temp.append(barg[y][x])
            y=y+1
        arg.append(temp)
        x=x+1

    #adding scale values
    x=begin
    temp = []
    while x < end:
        scale = float(barg[x][2])/float(barg[x][3])
        temp.append(scale)
        x=x+1

    #adding post boost values
    boost = []
    x=0
    while(x<len(arg[1])):
        boost.append(round(float(arg[3][x])*(statistics.mean(temp)), 1))
        x=x+1

    arg.append(temp)
    arg.append(boost)
    return arg

QS1P1ana = create(1,20)
QS1P2ana = create(20,32)
QS1P3ana = create(32,44)

QS2P1ana = create(44,56)
QS2P4ana = create(56,67)

QS3P1ana = create(67,82)
QS3P2ana = create(82,97)
QS3P3ana = create(97,114)
QS3P4ana = create(114,128)

total = []

total.append(QS1P1ana)
total.append(QS1P2ana)
total.append(QS1P3ana)

total.append(QS2P1ana)
total.append(QS2P4ana)

total.append(QS3P1ana)
total.append(QS3P2ana)
total.append(QS3P3ana)
total.append(QS3P4ana)

print(statistics.mean(QS1P1ana[4]))
print(statistics.mean(QS1P2ana[4]))
print(statistics.mean(QS1P3ana[4]))

print(statistics.mean(QS2P1ana[4]))
print(statistics.mean(QS2P4ana[4]))

print(statistics.mean(QS3P1ana[4]))
print(statistics.mean(QS3P2ana[4]))
print(statistics.mean(QS3P3ana[4]))
print(statistics.mean(QS3P4ana[4]))



def makebarplot(name, title, location):
    SMALL_SIZE = 5
    SmallMedium_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=SmallMedium_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SmallMedium_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SmallMedium_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SmallMedium_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


    #labels = GFZ
    labels = name[1]
    x = np.arange(len(labels))
    width = 0.35

    tempboost = []
    tempmeasured = []

    for y in name[5]:
        tempboost.append(float(y))

    for y in name[2]:
        tempmeasured.append(float(y))


    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, tempboost, width, label="Total Estimated After Calibration TD")
    rects2 = ax.bar(x + width/2, tempmeasured, width, label="Measured TD")

    ax.set_xlabel("GFZ Channels")
    ax.set_ylabel("Time Delay (ns)")
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    plt.savefig(location)

def makeratioplot(name, title, location):
    fig, ax = plt.subplots()
    x = name[1]
    y = name[4]
    ax.scatter(x, y, color='red', alpha=0.5)
    ax.set_xlabel("GFZ Channels")
    ax.set_ylabel("Predicted TD to Measured TD Scaling Ratio")
    ax.set_title(title)
    ax.grid(True)
    plt.savefig(location)

def compareMvP(name, title, location):
    fig, ax = plt.subplots()
    i = 0
    while i<len(name[1]):
        ax.text(float(name[3][i])-0.08, float(name[2][i])+0.05, name[1][i], fontsize=8)
        i=i+1
    y = [float(i) for i in name[2]]
    x = [float(i) for i in name[3]]
    labels = [str(i) for i in name[1]]
    ax.scatter(x,y, color='blue', alpha=0.5)
    ax.set_ylabel("Measured Time Delay Values")
    ax.set_xlabel("Predicted Time Delay Values")
    #plt.gca().set_aspect('equal', adjustable='box')
    ax.set_title(title)
    ax.grid(True)
    #ax.text(x+0.3. y+0.3, labels, fontsize=9)
    b, m = polyfit(x, y, 1)
    textstr = "b " + str(b.round(1)) + " m "+ str(m.round(1))
    #print(textstr)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
    plt.savefig(location)


for x in total:
    name = x[0][0]
    title1 = name + " Measured vs Predicted"
    title2 = name + " Time Delay Comparisons"
    title3 = name + " Scaling Ratio by Channel"
    address1 = "./Plots/" + name + "_MvP"
    address2 = "./Plots/" + name + "_TD_Compare"
    address3 = "./Plots/" + name + "_TD_ScalingRatios"
    compareMvP(x,title1,address1)
    makebarplot(x,title2,address2)
    makeratioplot(x,title3,address3)

