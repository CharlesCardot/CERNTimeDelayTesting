import pprint
import csv
pprinter = pprint.PrettyPrinter(indent=4)

Adapterboard = []
Detector = []

with open ('AdapterBoardTimeEstimatesSmallPivot.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        Adapterboard.append(temp)


with open ('DetectorTimeEstimatesSmallPivot.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = []
        for item in row:
            temp.append(item)
        Detector.append(temp)

#for x in Adapterboard:
#    pprint.pprint(x[0] + " " + x[5])

#for x in Detector:
#    pprint.pprint(x[0] + " " + x[5])

finalarg = []

for x in Detector:
    namedetec = x[0]
    GFZdetec = x[5]
    for y in Adapterboard:
        nameadap = y[0]
        GFZadap = y[5]
        if (nameadap==namedetec and GFZadap==GFZdetec):
            tracedetec = x[11]
            traceadap = y[8]
            #print("tracedetec " + tracedetec)
            #print("traceadap " + traceadap)
            print(namedetec + " " + nameadap + " " + GFZadap + " " + GFZdetec)
            TotTrace = float(tracedetec)+float(traceadap)
            timedetec = x[14]
            timeadap = y[11]
            TotTime = float(timedetec)+float(timeadap)
            finalarg.append(namedetec + " Pad P1 GFZ Channel: " + GFZdetec + " Total Trace Length: " + str(TotTrace) + " Total Time Estimate: " + str(TotTime))

#pprint.pprint(finalarg) 

newarg = []

for smolarg in finalarg:
        newarg.append(smolarg + "\n")

file1 = open("DetectorAndABTotalTimeDelaysSmallPivot.txt", "a+")
filebuffer = ["a line \n", "another line \n"]
file1.writelines(newarg)

file1.close()