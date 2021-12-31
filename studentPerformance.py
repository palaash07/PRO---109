import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
mathScore = df["math score"].to_list()
readingScore = df["reading score"].to_list()
writingScore = df["writing score"].to_list()

#mean
mathMean = statistics.mean(mathScore)
readingMean = statistics.mean(readingScore)
writingMean = statistics.mean(writingScore)

#mode
mathMode = statistics.mode(mathScore)
readingMode = statistics.mode(readingScore)
writingMode = statistics.mode(writingScore)

#median
mathMedian = statistics.median(mathScore)
readingMedian = statistics.median(readingScore)
writingMedian = statistics.median(writingScore)

print("For maths scores, mean = {}, mode = {} and median = {}".format(mathMean, mathMode, mathMedian))
print("For reading scores, mean = {}, mode = {} and median = {}".format(readingMean, readingMode, readingMedian))
print("For writing score, mean = {}, mode = {} and median = {}".format(writingMean, writingMode, writingMedian))

#standard deviation
mathsStd = statistics.stdev(mathScore)
readingStd = statistics.stdev(readingScore)
writingStd = statistics.stdev(writingScore)

mathsFirstStdStart, mathsFirstStdEnd = mathMean - mathsStd, mathMean + mathsStd
mathsSecondStdStart, mathsSecondStdEnd = mathMean - (2*mathsStd), mathMean + (2*mathsStd)
mathsThirdStdStart, mathsThirdStdEnd = mathMean - (3*mathsStd), mathMean + (3*mathsStd)

readingFirstStdStart, readingFirstStdEnd = readingMean - readingStd, readingMean + readingStd
readingSecondStdStart, readingSecondStdEnd = readingMean - (2*readingStd), readingMean + (2*readingStd)
readingThirdStdStart, readingThirdStdEnd = readingMean - (3*readingStd), readingMean + (3*readingStd)

writingFirstStdStart, writingFirstStdEnd = writingMean - writingStd, writingMean + writingStd
writingSecondStdStart, writingSecondStdEnd = writingMean - (2*writingStd), writingMean + (2*writingStd)
writingThirdStdStart, writingThirdStdEnd = writingMean - (3*writingStd), writingMean + (3*writingStd)

liftOfDataWithinOneStandardDeviationForMaths = [result for result in mathScore if result > mathsFirstStdStart and result < mathsFirstStdEnd]
liftOfDataWithinTwoStandardDeviationForMaths = [result for result in mathScore if result > mathsSecondStdStart and result < mathsSecondStdEnd]
liftOfDataWithinThreeStandardDeviationForMaths = [result for result in mathScore if result > mathsThirdStdStart and result < mathsThirdStdEnd]

liftOfDataWithinOneStandardDeviationForReading = [result for result in readingScore if result > readingFirstStdStart and result < readingFirstStdEnd]
liftOfDataWithinTwoStandardDeviationForReading = [result for result in readingScore if result > readingSecondStdStart and result < readingSecondStdEnd]
liftOfDataWithinThreeStandardDeviationForReading = [result for result in readingScore if result > readingThirdStdStart and result < readingThirdStdEnd]

liftOfDataWithinOneStandardDeviationForWriting = [result for result in writingScore if result > writingFirstStdStart and result < writingFirstStdEnd]
liftOfDataWithinTwoStandardDeviationForWriting = [result for result in writingScore if result > writingSecondStdStart and result < writingSecondStdEnd]
liftOfDataWithinThreeStandardDeviationForWriting = [result for result in writingScore if result > writingThirdStdStart and result < writingThirdStdEnd]

print("{}% of data for maths Score lies within 1 standard deviations".format(len(liftOfDataWithinOneStandardDeviationForMaths)*100.0/len(mathScore)))
print("{}% of data for maths Score lies within 2 standard deviations".format(len(liftOfDataWithinTwoStandardDeviationForMaths)*100.0/len(mathScore)))
print("{}% of data for maths Score lies within 3 standard deviations".format(len(liftOfDataWithinThreeStandardDeviationForMaths)*100.0/len(mathScore)))
print("{}% of data for reading Score lies within 1 standard deviation".format(len(liftOfDataWithinOneStandardDeviationForReading)*100.0/len(readingScore)))
print("{}% of data for reading Score lies within 2 standard deviations".format(len(liftOfDataWithinTwoStandardDeviationForReading)*100.0/len(readingScore)))
print("{}% of data for reading Score lies within 3 standard deviations".format(len(liftOfDataWithinThreeStandardDeviationForReading)*100.0/len(readingScore)))
print("{}% of data for writing Score lies within 1 standard deviation".format(len(liftOfDataWithinOneStandardDeviationForWriting)*100.0/len(writingScore)))
print("{}% of data for writing Score lies within 2 standard deviations".format(len(liftOfDataWithinTwoStandardDeviationForWriting)*100.0/len(writingScore)))
print("{}% of data for writing Score lies within 3 standard deviations".format(len(liftOfDataWithinThreeStandardDeviationForWriting)*100.0/len(writingScore)))

