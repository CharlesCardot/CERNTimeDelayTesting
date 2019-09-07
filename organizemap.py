import pprint
import csv
pprinter = pprint.PrettyPrinter(indent=4)


channelpadmapQS1P12 = []
channelpadmapQS1P34 = []
channelpadmapQS2P12 = []
channelpadmapQS2P34 = []
channelpadmapQS3P12 = []
channelpadmapQS3P34 = []
channelpadmapQL1P12 = []
channelpadmapQL1P34 = []
channelpadmapQL2P12 = []
channelpadmapQL2P34 = []
channelpadmapQL3P12 = []
channelpadmapQL3P34 = []

padchannelmapping = []

finalarg = []


#QS1P12
with open ('PadTrackLengthsQS1P12.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQS1P12.append(temp)
#pprint.pprint(channelpadmapQS1P12)

#QS1P34
with open ('PadTrackLengthsQS1P34.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQS1P34.append(temp)
#pprint.pprint(channelpadmapQS1P34)

#QS2P12
with open ('PadTrackLengthsQS2P12.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQS2P12.append(temp)
#pprint.pprint(channelpadmapQS2P12)

#QS2P34*
with open ('PadTrackLengthsQS2P34.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQS2P34.append(temp)
#pprint.pprint(channelpadmapQS2P34)

#QS3P12
with open ('PadTrackLengthsQS3P12.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQS3P12.append(temp)
#pprint.pprint(channelpadmapQS3P12)

#QS3P34
with open ('PadTrackLengthsQS3P34.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQS3P34.append(temp)
#pprint.pprint(channelpadmapQS3P34)

#QL1P12
with open ('PadTrackLengthsQL1P12.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQL1P12.append(temp)
#pprint.pprint(channelpadmapQL1P12)

#QL1P34
with open ('PadTrackLengthsQL1P34.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQL1P34.append(temp)
#pprint.pprint(channelpadmapQL1P34)

#QL2P12
with open ('PadTrackLengthsQL2P12.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQL2P12.append(temp)
#pprint.pprint(channelpadmapQL2P12)

#QL2P34
with open ('PadTrackLengthsQL2P34.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQL2P34.append(temp)
#pprint.pprint(channelpadmapQL2P34)

#QL3P12
with open ('PadTrackLengthsQL3P12.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQL3P12.append(temp)
#pprint.pprint(channelpadmapQL3P12)

#QL3P34
with open ('PadTrackLengthsQL3P34.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        channelpadmapQL3P34.append(temp)
#pprint.pprint(channelpadmapQL3P34)

with open ('PadChannelMapping.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        padchannelmapping.append(temp)
#pprint.pprint(padchannelmapping)
#pprint.pprint(padchannelmapping[169])

#43, 62

channelpadmapQS1P12.pop(0)
channelpadmapQS1P34.pop(0)
channelpadmapQS2P12.pop(0)
channelpadmapQS2P34.pop(0)
channelpadmapQS3P12.pop(0)
channelpadmapQS3P34.pop(0)
channelpadmapQL1P12.pop(0)
channelpadmapQL1P34.pop(0)
channelpadmapQL2P12.pop(0)
channelpadmapQL2P34.pop(0)
channelpadmapQL3P12.pop(0)
channelpadmapQL3P34.pop(0)
#pprint.pprint(channelpadmapQL2P12)

arg1 = []
arg2 = []

for x in channelpadmapQS1P12:
    tempchan = x[0]
    timeestimate = 1000000000*(float(x[2])/1000)/193788819.9
    timeestimate = str(timeestimate)
    j = 169
    while j < 237:
        if(padchannelmapping[j][5] == tempchan):
            entry = "QS1P1 Pad P1 GFZ Channel: " + padchannelmapping[j][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg1.append(entry)
        j = j+1
    a = 157
    while a < 260:
        if(padchannelmapping[a][6] == tempchan):   
            entry = "QS1P2 Pad P1 GFZ Channel: " + padchannelmapping[a][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg2.append(entry)
        a = a+1

#pprint.pprint(arg1)
#pprint.pprint(arg2)
finalarg.append(arg1)
finalarg.append(arg2)
arg1 = []
arg2 = []

for x in channelpadmapQS1P34:
    firstcolumn = 7
    secondcolumn = 8
    tempchan = x[0]
    timeestimate = 1000000000*(float(x[2])/1000)/193788819.9
    timeestimate = str(timeestimate)
    j = 127
    while j < 260:
        if(padchannelmapping[j][firstcolumn] == tempchan):
            entry = "QS1P3 Pad " + padchannelmapping[j][2] + " GFZ Channel: " + padchannelmapping[j][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg1.append(entry)
        j = j+1
    a = 127
    while a < 260:
        if(padchannelmapping[a][secondcolumn] == tempchan):   
            entry = "QS1P4 Pad " + padchannelmapping[j][2] + " GFZ Channel: " + padchannelmapping[a][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg2.append(entry)
        a = a+1

#pprint.pprint(arg1)
#pprint.pprint(arg2)
finalarg.append(arg1)
finalarg.append(arg2)
arg1 = []
arg2 = []

for x in channelpadmapQS2P12:
    firstcolumn = 15
    secondcolumn = 16
    tempchan = x[0]
    timeestimate = 1000000000*(float(x[2])/1000)/193788819.9
    timeestimate = str(timeestimate)
    j = 127
    while j < 260:
        if(padchannelmapping[j][firstcolumn] == tempchan):
            entry = "QS2P1 Pad " + padchannelmapping[j][2] + " GFZ Channel: " + padchannelmapping[j][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg1.append(entry)
        j = j+1
    a = 127
    while a < 260:
        if(padchannelmapping[a][secondcolumn] == tempchan):   
            entry = "QS2P2 Pad " + padchannelmapping[a][2] + " GFZ Channel: " + padchannelmapping[a][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg2.append(entry)
        a = a+1

#pprint.pprint(arg1)
#pprint.pprint(arg2)
finalarg.append(arg1)
finalarg.append(arg2)
arg1 = []
arg2 = []

for x in channelpadmapQS2P34:
    firstcolumn = 17
    secondcolumn = 18
    tempchan = x[0]
    timeestimate = 1000000000*(float(x[2])/1000)/193788819.9
    timeestimate = str(timeestimate)
    j = 127
    while j < 260:
        if(padchannelmapping[j][firstcolumn] == tempchan):
            entry = "QS2P3 Pad " + padchannelmapping[j][2] + " GFZ Channel: " + padchannelmapping[j][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg1.append(entry)
        j = j+1
    a = 127
    while a < 260:
        if(padchannelmapping[a][secondcolumn] == tempchan):   
            entry = "QS2P4 Pad " + padchannelmapping[a][2] + " GFZ Channel: " + padchannelmapping[a][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg2.append(entry)
        a = a+1

#pprint.pprint(arg1)
#pprint.pprint(arg2)
finalarg.append(arg1)
finalarg.append(arg2)
arg1 = []
arg2 = []

for x in channelpadmapQS3P12:
    firstcolumn = 25
    secondcolumn = 26
    tempchan = x[0]
    timeestimate = 1000000000*(float(x[2])/1000)/193788819.9
    timeestimate = str(timeestimate) 
    j = 127
    while j < 260:
        if(padchannelmapping[j][firstcolumn] == tempchan):
            entry = "QS3P1 Pad " + padchannelmapping[j][2] + " GFZ Channel: " + padchannelmapping[j][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg1.append(entry)
        j = j+1
    a = 127
    while a < 260:
        if(padchannelmapping[a][secondcolumn] == tempchan):   
            entry = "QS3P2 Pad " + padchannelmapping[a][2] + " GFZ Channel: " + padchannelmapping[a][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg2.append(entry)
        a = a+1

#pprint.pprint(arg1)
#pprint.pprint(arg2)
finalarg.append(arg1)
finalarg.append(arg2)
arg1 = []
arg2 = []

for x in channelpadmapQS3P34:
    firstcolumn = 27
    secondcolumn = 28
    tempchan = x[0]
    timeestimate = 1000000000*(float(x[2])/1000)/193788819.9
    timeestimate = str(timeestimate) 
    j = 127
    while j < 260:
        if(padchannelmapping[j][firstcolumn] == tempchan):
            entry = "QS3P3 Pad " + padchannelmapping[j][2] + " GFZ Channel: " + padchannelmapping[j][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg1.append(entry)
        j = j+1
    a = 127
    while a < 260:
        if(padchannelmapping[a][secondcolumn] == tempchan):   
            entry = "QS3P4 Pad " + padchannelmapping[a][2] + " GFZ Channel: " + padchannelmapping[a][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
            arg2.append(entry)
        a = a+1

#pprint.pprint(arg1)
#pprint.pprint(arg2)
finalarg.append(arg1)
finalarg.append(arg2)
arg1 = []
arg2 = []
#pprint.pprint(finalarg)

def easy(name, firstcolumn, secondcolcumn, arr):
    arg1 = []
    arg2 = []
    for x in arr:
        tempchan = x[0]
        print(x)
        timeestimate = 1000000000*(float(x[2])/1000)/193788819.9
        timeestimate = str(timeestimate)
        j = 127
        while j < 260:
            if(padchannelmapping[j][firstcolumn] == tempchan):
                entry = name + " Pad " + padchannelmapping[j][2] + " GFZ Channel: " + padchannelmapping[j][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
                arg1.append(entry)
            j = j+1
        a = 127
        while a < 260:
            if(padchannelmapping[a][secondcolumn] == tempchan):   
                entry = name + " Pad " + padchannelmapping[a][2] + " GFZ Channel: " + padchannelmapping[a][3] + " Actual Channel: " + tempchan + " Trace Length: " + x[2] + " Time estimate: " + timeestimate
                arg2.append(entry)
            a = a+1
    finalarg.append(arg1)
    finalarg.append(arg2)

easy("QL1P1",35,36,channelpadmapQL1P12)
easy("QL1P2",35,36,channelpadmapQL1P12)
easy("QL1P3",37,38,channelpadmapQL1P34)
easy("QL1P4",37,38,channelpadmapQL1P34)

#print(" ")
#print(channelpadmapQL2P12)

easy("QL2P1",45,46,channelpadmapQL2P12)
easy("QL2P2",45,46,channelpadmapQL2P12)
easy("QL2P3",47,48,channelpadmapQL2P34)
easy("QL2P4",47,48,channelpadmapQL2P34)


easy("QL3P1",55,56,channelpadmapQL3P12)
easy("QL3P2",55,56,channelpadmapQL3P12)
easy("QL3P3",57,58,channelpadmapQL3P34)
easy("QL3P4",57,58,channelpadmapQL3P34)



newarg = []

for smolarg in finalarg:
    for x in smolarg:
        newarg.append(x + "\n")

file1 = open("DetectorTimeEstimatesSmallPivot.txt", "a+")
filebuffer = ["a line \n", "another line \n"]
#file1.writelines(newarg)

file1.close()


