import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random
data = pd.read_csv("medium_data.csv")
dataList = data["reading_time"].tolist()

populationMean=statistics.mean(dataList)
print("Population mean:",populationMean)

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
mean_of_sample1=statistics.mean(data)
print(mean_of_sample1)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)
mean=statistics.mean(mean_list)
stdev=statistics.stdev(mean_list)

print(mean,stdev)
first_stdev_start,first_stdev_end=mean-stdev,mean+stdev
second_stdev_start,second_stdev_end=mean-(2*stdev),mean+(2*stdev)
third_stdev_start,third_stdev_end=mean-(3*stdev),mean+(3*stdev)

print("std1 :", first_stdev_start,first_stdev_end)
print("std1 :", second_stdev_start,second_stdev_end)
print("std1 :", third_stdev_start,third_stdev_end)

fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines",name="std1"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name="std1"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines",name="std2"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="std2"))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines",name="std3"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name="std3"))

fig.show()