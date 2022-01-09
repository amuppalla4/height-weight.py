import random
import plotly.express as px
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
count=[]
dice_result=[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
print("mean of the data is ", str(mean))
print("median of the data is ", str(median))
print("mode of the data is ", str(mode))
standard_deviation=statistics.stdev(dice_result)
print("standard deviation of the data is ", str(standard_deviation))
fig=ff.create_distplot([dice_result],["Result"], show_hist=False)
fig.show()