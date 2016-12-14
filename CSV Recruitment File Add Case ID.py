# change directory to directory with python files and data, bookmarked.
%cd -b pythonstemfiles

#import relevant modules for analysis.
import csv
import os

#open file with job description information in it, read into a reader file.
#convert reader file to a list of lists.
STEMFile = open('JobDescriptionExtract.csv')
STEMReader = csv.reader(STEMFile)
STEMData = list(STEMReader)

#add a column title for "CASE_ID" to the first row.
FIRSTROW = STEMData[0]
FIRSTROW.insert(0, 'CASE_ID')

#for all but first row in file, create variable CASE_ID from.
#the job number, campus id number, and the year of recruitment.
#insert the CASE_ID number at the beginning of each row.

for i in range (1, len(STEMData)):
  CASE_IDNUM = (STEMData [i][8] + "_" + STEMData[i][0] + "_" + STEMData[i][3])  
  CURRENTROW = STEMData[i]
  CURRENTROW.insert(0, CASE_IDNUM)

#next thing to do is to write the new STEMData structure to an external csv file.
#the goal is to write a general program that can do this with the next set of data too.

outputFILE = open('JobDescriptionsFile.csv', 'wb')

outputWRITER = csv.writer(outputFILE)

for i in range (0, len(STEMData)):
    outputWRITER.writerow(STEMData[i])

outputFILE.close()





