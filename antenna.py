import pandas as pd
import matplotlib.pyplot as plt
   
data = {
        '#1': -32.3,
        '#2': -45.2,
        '#3': -48.7,
        '#4': -34.4,
        '#5': -49.1,
        '#6': -54.2,
        '#7': -56.4,
        '#8': -49.4,
        '#9': -49.9,
        '#10': -54.2,
       }
  
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# Create the bar plot
barlist = plt.bar(courses, values, 
                width = 0.4)

# Set barplot colours
barlist[0].set_color('red')
barlist[1].set_color('green')
barlist[2].set_color('blue')
barlist[3].set_color('purple')
barlist[4].set_color('red')
barlist[5].set_color('teal')
barlist[6].set_color('pink')
barlist[7].set_color('brown')
barlist[8].set_color('indigo')
barlist[9].set_color('orange')


# Bar graph setup
plt.xlabel("Testing areas")
plt.ylabel("Signal strength in dBm")
plt.title("Comparison of signal strength using the Alfa NIC at the 10 test areas")
plt.gca().invert_yaxis()
plt.show()