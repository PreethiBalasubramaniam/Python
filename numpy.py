import random 
import numpy as np

random.seed(1234)
rr = np.random.normal(loc=0, scale=0.5, size=(5000, 1000))

steps = np.where(rr > 0, 1, -1)

walks = steps.cumsum(1)

hitsNegative50 = (walks == -50).any(1)

hitsNegative50.sum()

crossing_times = (walks[hitsNegative50] == -50).argmax(1)
total_number = len(crossing_times)

avg_crossing_time = crossing_times.mean()

print("The number of random walks that hit -50:", total_number)
print("The average minimum crossing time:", avg_crossing_time)
