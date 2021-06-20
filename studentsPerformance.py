import pandas as pd 
import statistics
import csv
df= pd.read_csv("StudentsPerformance.csv")
mslist=df["math score"].tolist()
msmean=statistics.mean(mslist)
msmedian=statistics.median(mslist)
msmode=statistics.mode(mslist)
msStandardDeviation=statistics.stdev(mslist)
msfsds, msfsde= msmean - msStandardDeviation, msmean + msStandardDeviation
msssds, msssde= msmean - (2*msStandardDeviation), msmean +(2*msStandardDeviation)
mstsds, mstsde= msmean - (3*msStandardDeviation), msmean + (3*msStandardDeviation)
mslistofdatawithinfirstStandardDeviation=[result for result in mslist if result>msfsds and result<msfsde]
mslistofdatawithinsecondStandardDeviation=[result for result in mslist if result>msssds and result<msssde]
mslistofdatawithinthirdStandardDeviation=[result for result in mslist if result>mstsds and result<mstsde]
print("{}% of data for ms lies within 1 standard deviation".format(len(mslistofdatawithinfirstStandardDeviation)*100/len(mslist)))
print("{}% of data for ms lies within 2 standard deviation".format(len(mslistofdatawithinsecondStandardDeviation)*100/len(mslist)))
print("{}% of data for ms lies within 3 standard deviation".format(len(mslistofdatawithinthirdStandardDeviation)*100/len(mslist)))

# ms stands for maths score