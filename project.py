import plotly.figure_factory as pff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv('peodata.csv')
data = df ['reading_time'].to_list()
fig = pff.create_distplot([data],['reading_time'],show_hist=False)
fig.show()

mean = statistics.mean(data)
std = statistics.stdev(data)
print('mean of population',mean)
print('standerd dev',std)

def random_set_of_mean(counter): 
    dataset = [] 
    for i in range(0, counter): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 
    mean = statistics.mean(dataset) 
    return mean 

mean_list = [] 
for i in range(0,1000): 
    set_of_means= random_set_of_mean(100) 
    mean_list.append(set_of_means)
mean_sample=statistics.mean(mean_list)
std_sample = statistics.stdev(mean_list)
print('mean of population',mean_sample)
print('standerd dev',std_sample)
fig = pff.create_distplot([mean_list],['r_mean'],show_hist=False)
fig.show()