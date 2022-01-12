import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

reading_mean = statistics.mean(reading_list)
writing_mean = statistics.mean(writing_list)

reading_median = statistics.median(reading_list)
writing_median = statistics.median(writing_list)

reading_mode = statistics.mode(reading_list)
writing_mode = statistics.mode(writing_list)

print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
print("Mean, Median and Mode of writing is {}, {} and {} respectively".format(writing_mean, writing_median, writing_mode))

reading_std_deviation = statistics.stdev(reading_list)
writing_std_deviation = statistics.stdev(writing_list)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

reading_thin_1_std_deviation = [result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_thin_2_std_deviation = [result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_thin_3_std_deviation = [result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_thin_1_std_deviation = [result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_thin_2_std_deviation = [result for result in writing_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_thin_3_std_deviation = [result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for reading lies within 1 standard deviation".format(len(reading_thin_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_thin_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_thin_3_std_deviation)*100.0/len(reading_list)))
print("{}% of data for writing lies within 1 standard deviation".format(len(writing_thin_1_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_thin_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_thin_3_std_deviation)*100.0/len(writing_list)))