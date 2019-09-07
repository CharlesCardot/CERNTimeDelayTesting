import pprint
import csv
pprinter = pprint.PrettyPrinter(indent=4)




def GFZtracleng(INTracleng, INGFZ):
    #print("reached")
    temp = []
    for x in INTracleng:
        #print(temp)
        #print("reached")
        INnumx = x[0]
        #print(INnumx)
        for y in INGFZ:
            INnumy = y[1]
            #print(INnumy)
            if (int(INnumy)==int(INnumx)):
                temp.append([y[0],x[1]])
    
    return temp




channelpadmapQS1P1 = []
channelpadmapQS1P2 = []
channelpadmapQS1P3 = []
channelpadmapQS1P4 = []

channelpadmapQS2P1 = []
channelpadmapQS2P2 = []
channelpadmapQS2P3 = []
channelpadmapQS2P4 = []

channelpadmapQS3P1 = []
channelpadmapQS3P2 = []
channelpadmapQS3P3 = []
channelpadmapQS3P4 = []

channelpadmapQL1P1 = []
channelpadmapQL1P2 = []
channelpadmapQL1P3 = []
channelpadmapQL1P4 = []

channelpadmapQL2P1 = []
channelpadmapQL2P2 = []
channelpadmapQL2P3 = []
channelpadmapQL2P4 = []

channelpadmapQL3P1 = []
channelpadmapQL3P2 = []
channelpadmapQL3P3 = []
channelpadmapQL3P4 = []

TrackLengths = []

with open ('ABtracklengthLRmapping.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        TrackLengths.append(temp)
#pprint.pprint(TrackLengths)





def seperatearrays75(col1, col2):
    x = 0
    temp = []
    while x < 75:
        num = TrackLengths[x][col2]
        if(col1==3):
            num=str(float(num)*0.0254)
        temp.append([TrackLengths[x][col1], num])
        x=x+1
    return temp

def seperatearrays112(col1, col2):
    x = 0
    temp = []
    while x < 112:
        temp.append([TrackLengths[x][col1], TrackLengths[x][col2]])
        x=x+1
    return temp

def seperatearrays70(col1, col2):
    x=0
    temp = []
    while x < 70:
        num = TrackLengths[x][col2]
        temp.append([TrackLengths[x][col1], TrackLengths[x][col2]])
        x=x+1
    return temp

def seperatearrays42(col1, col2):
    x=0
    temp = []
    while x < 42:
        num = TrackLengths[x][col2]
        temp.append([TrackLengths[x][col1], TrackLengths[x][col2]])
        x=x+1
    return temp




x = 0
while x < 75:
    temp = [TrackLengths[x][0], TrackLengths[x][1]]
    if(x==0):
        channelpadmapQS1P2.append([1, TrackLengths[0][1]])
        x = x+1
    else:
        channelpadmapQS1P2.append(temp)
        x = x+1

#pprint.pprint(channelpadmapQS1P2)
#Connecting AB with Input & corresponding track length
channelpadmapQS1P1 = seperatearrays75(3,4)
channelpadmapQS1P4 = seperatearrays75(3,4)
channelpadmapQS1P3 = channelpadmapQS1P2

channelpadmapQS2P1 = seperatearrays75(3,4)
channelpadmapQS2P2 = channelpadmapQS1P2
channelpadmapQS2P3 = channelpadmapQS1P2
channelpadmapQS2P4 = seperatearrays75(3,4) 

channelpadmapQS3P1 = seperatearrays42(12,13)
channelpadmapQS3P2 = seperatearrays42(15,16)
channelpadmapQS3P3 = seperatearrays42(15,16)
channelpadmapQS3P4 = seperatearrays42(12,13)

channelpadmapQL1P1 = seperatearrays112(9,10)
channelpadmapQL1P2 = seperatearrays112(6,7)
channelpadmapQL1P3 = seperatearrays112(6,7)
channelpadmapQL1P4 = seperatearrays112(9,10)

channelpadmapQL2P1 = seperatearrays75(3,4)
channelpadmapQL2P2 = channelpadmapQS1P2
channelpadmapQL2P3 = channelpadmapQS1P2
channelpadmapQL2P4 = seperatearrays75(3,4)

channelpadmapQL3P1 = seperatearrays70(18,19)
channelpadmapQL3P2 = seperatearrays70(21,22)
channelpadmapQL3P3 = seperatearrays70(21,22)
channelpadmapQL3P4 = seperatearrays70(18,19)

#pprint.pprint(channelpadmapQL1P1)

#Creating PINChannel to GFZChannel mapping arrays
#Look at pdf on AdapterboardPad mapping on Twiki for reference
Left75 = []
x = 1;
while x<75:
    entry1 = "j" + str(x+23)
    Left75.append([entry1, x])
    x=x+1;
Left75.append(["j98", 0])

#pprint.pprint(Left75)

Right75 = []
x = 103;
while x>28:
    entry1 = "j" + str(x)
    Right75.append([entry1, 104-x])
    x=x-1

#pprint.pprint(Right75)

Left112 = []
x=0;
while x<112:
    entry1 = "j" + str(x)
    Left112.append([entry1, x+1])
    x=x+1

#pprint.pprint(Left112)

Right112 = []
x=0;
while x<104:
    entry1 = "j" + str(x)
    Right112.append([entry1, 103-x])
    x=x+1;
x=105
while x<113:
    entry1 = "j" + str(x-1)
    Right112.append([entry1, x])
    x=x+1;

#pprint.pprint(Right112)

Left42 = []
x=64;
while x<106:
    entry1 = "j" + str(x)
    Left42.append([entry1, x-63])
    x=x+1;

#pprint.pprint(Left42)

Right42 = []
x=105;
while x>(63):
    entry1 = "j" + str(x)
    Right42.append([entry1, 106-x])
    x=x-1;

#pprint.pprint(Right42)

Left70 = []
x=26;
while x<96:
    entry1 = "j" + str(x)
    Left70.append([entry1, x-25])
    x=x+1;

#pprint.pprint(Left70)

Right70 = []
x=103;
while x>33:
    entry1 = "j" + str(x)
    Right70.append([entry1, 1+103-x])
    x=x-1;

#pprint.pprint(Right70)

#somearg = GFZtracleng(channelpadmapQS1P2, Left75)

def full(name, temp):
    total = []
    for x in temp:
        timeestimate = 1000000000*(float(x[1])/1000)/193788819.9
        timeestimate = str(timeestimate)
        entry = name + " Pad P1 GFZ Channel: " + x[0] + " Trace Length: " + x[1] + " Time estimate: " + timeestimate
        total.append(entry)
    return total

finalarg = []

#Adding in the 75channel S1 and S2 configurations

finalarg.append(full("QS1P1", GFZtracleng(channelpadmapQS1P1, Right75)))
finalarg.append(full("QS1P2", GFZtracleng(channelpadmapQS1P2, Left75)))
finalarg.append(full("QS1P3", GFZtracleng(channelpadmapQS1P3, Left75)))
finalarg.append(full("QS1P4", GFZtracleng(channelpadmapQS1P4, Right75)))

finalarg.append(full("QS2P1", GFZtracleng(channelpadmapQS2P1, Right75)))
finalarg.append(full("QS2P2", GFZtracleng(channelpadmapQS2P2, Left75)))
finalarg.append(full("QS2P3", GFZtracleng(channelpadmapQS2P3, Left75)))
finalarg.append(full("QS2P4", GFZtracleng(channelpadmapQS2P4, Right75)))

#Adding in the 42channel S3 configuration
finalarg.append(full("QS3P1", GFZtracleng(channelpadmapQS3P1, Right42)))
finalarg.append(full("QS3P2", GFZtracleng(channelpadmapQS3P2, Left42)))
finalarg.append(full("QS3P3", GFZtracleng(channelpadmapQS3P3, Left42)))
finalarg.append(full("QS3P4", GFZtracleng(channelpadmapQS3P1, Right42)))

#Adding in the 75channel L2 configuration and 112channel L1 configuration 

finalarg.append(full("QL1P1", GFZtracleng(channelpadmapQL1P1, Right112)))
finalarg.append(full("QL1P2", GFZtracleng(channelpadmapQL1P2, Left112)))
finalarg.append(full("QL1P3", GFZtracleng(channelpadmapQL1P3, Left112)))
finalarg.append(full("QL1P4", GFZtracleng(channelpadmapQL1P4, Right112)))

finalarg.append(full("QL2P1", GFZtracleng(channelpadmapQL2P1, Right75)))
finalarg.append(full("QL2P2", GFZtracleng(channelpadmapQL2P2, Left75)))
finalarg.append(full("QL2P3", GFZtracleng(channelpadmapQL2P3, Left75)))
finalarg.append(full("QL2P4", GFZtracleng(channelpadmapQL2P1, Right75)))

#Adding in the 70channel L3 configuration
finalarg.append(full("QL3P1", GFZtracleng(channelpadmapQL3P1, Right70)))
finalarg.append(full("QL3P2", GFZtracleng(channelpadmapQL3P2, Left70)))
finalarg.append(full("QL3P3", GFZtracleng(channelpadmapQL3P3, Left70)))
finalarg.append(full("QL3P4", GFZtracleng(channelpadmapQL3P4, Right70)))


#pprint.pprint(finalarg)
newarg = []

for smolarg in finalarg:
    for x in smolarg:
        newarg.append(x + "\n")

file1 = open("AdapterBoardTimeEstimatesSmallPivot.txt", "a+")
filebuffer = ["a line \n", "another line \n"]
file1.writelines(newarg)

file1.close()



