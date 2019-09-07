# NSW sTGC Wedge Time Delay Measurements

# Introduction
This project contains all of the python scripts, excel documents, and text files 
for generating a mapping between the detector components of the sTGC Wedges and the time delay
associated with the trace length of each component. All predictions about time delay are based
off of the given trace length of the wire and the estimated velocity of propagation of the signal
through the wire. I will also explain how to perform the time delay testing using a Time Domain Reflectometer
as well some of the quirky aspects of the sTGC wedges.

# Contents
* All of the excel files named **PadTrackLengths######.csv** contain pad channels for that particular ###### section 
of the wedge matched with the corresponding trace lengths.
* **PadChannelMapping.csv** maps contains information about pads, strips, and wires, contrary to what the name 
suggests. It has the mapping between the pad, strip, or wire channels to the corresponding GFZ channels.
* **organizemap.py** is a python script that uses the info from all the **PadTrackLengths######.csv** files and the 
PadChannelMapping.csv file to match trace length to GFZ channel. It also multiplies the trace lengths by the 
predicted velocity of propagation of the signal in the wire to get an estimate for the time delay.
* **GFZPhysicalChannelMapping.xlsx** gives you a diagram for where all the GFZ channels are physically located 
on the GFZ connector. This is very useful to have when performing actual *Time Delay (TD)* measurements.
* **DetectorTimeEstimatesSmallPivot.csv** is the output file created by organizemap.py with all the info about
part of the detector, GFZ channel, trace length, and estimated time delay
* **ABtracklengthLRmapping.csv** has 8 groups of 2 columns, for a total of 16, with the trace lengths for a given 
pin in the adapter boards. The order is 75L, 75R, 120L, 120R, 42L, 42R, 70L, 70R.
* **Adapterboardtracecode.py** essentially does the same thing as **organizemap.py** but for the adapterboard part.
It takes in the mapping from GFZ channel to adapter pin and matches it with the trace length for that given
pin, and also calculates the predicted time delay for that trace length.
* AdapterBoardTimeEstimatesSmallPivot.txt is the output file from **Adapterboardtracecode.py**
* **DetectorAndAdapterCombined.py** uses **AdapterBoardTimeEstimatesSmallPivot.csv** and **DetectorTimeEstimatesSmallPivot.csv**
and combines their information to create DetectorAndABTotalTimeDelaysSmallPivot.txt which has the total 
trace length (from both detector and adapter board) and the total time delay, as well as all the identifying
information for the location for this channel on the wedge. 
* **CERN REU Technical Essay.pdf** is a written report detailing the process for measuring the time delay as well
as some conclusions about how to predict the time delay for each part of the wedge. Please pay attention to 
QS3 section of the report, and note that in **organizemap.py** and **Adapterboardtracecode.py** the prediction values
being calculated are using the velocity of propagation from the coaxial cable and will need to be given a 
scaling factor for each quadruplate layer section before you are able to get the true time delay.
* **Installation and Upgrades for the Front End Electronics of the ATLAS New Small Wheel.pdf** is a presentation
which goes over the same information as the Technical essay 
* **MeasuredValuesCalc.py** takes in data from **MeasuredTDValues.csv** (which are measured time delay values for select
sections of the wedge) and creates plots comparing the predicted vs measure time delay, calcualtes the scaling
factor, all of which can be found in the Plots folder.

# Important Notes
* I highly recommend that you first read the CERN REU Technical Essay before continuing if you do not already have 
some experience with the time delay measurements on the sTGC wedges, because the presentation will give you a lot 
of background knowledge that will help you better understand this README and the python code. 
* The DetectorAndABTotalTimeDelaysSmallPivot.txt file currently has a list of every GFZ that is connected to some pad
within the Pivot sTGC detector wedges, as well as a predicted time delay values for each of them. It does not contain
any info about the Confirm wedges, or the strips. Seeing as how these predicted time delay values are based off of a 
coaxial cable as a baseline measurement, these values need to be scaled by their unique scaling 
factorbefore then can be considered correct. We still need to get a mapping for the strips on the Pivot wedges, as
well as the strips *and* pads on the Confirm wedges.
* Measurements of the time delay are more complicated for the QS3 quadruplate, and will require you to measure the
systematic uncertainty that is associated with the larger pads found in the quadruplate.

# How to measure Time Delays
* 1. Aquire a Time Domain Reflectometer and testing cable which gives you both a signal and ground leads.
* 2. Print out, or get a digitial copy of the physical mapping for the GFZ pins.
* 3. Go up to the wedge, identify the correct quadruplate, layer, and adapter board that you want
to be measuring, and then peel back the protective tape on the GFZ connector.
* 4. Turn on the TDR and plug in your testing cable and adjust the settings so that you can see the inital pulse as well
as the reflection from the end of the cable.
* 5. Adjust the image of the TDR as well as the two vertical markers so that you are measuring with the reflection created
by the end of the testing cable as your starting point. This ensures that you are not measuring any time delay that comes from 
your testing cable.
* 6. Take the end of your testing cable and connect one lead to the ground pin and one lead to whatever GFZ pin you are 
measuring. While doing this, have someone adjust the second vertical line to the highest peak or trough in the reflection 
pattern. This will be the point where the cable reaches an open end or a short. 
* 7. Record the measured time delay as it is displayed on the screen.
* *There are pictures to go along with each of these steps in the images folder*

# Developer
* Charles Cardot

# Acknowledgements
* Siyaun Sun
* Bobby Tse
* Bobby McGovern

 