import pandas as pd
import matplotlib.pyplot as plt
   
data = {
        'USB NIC': -77.4,
        'Cantenna': -79.9,
        'Colander': -76.6,
        'Alfa NIC': -54.2
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

# Bar graph setup
plt.xlabel("Antenna name")
plt.ylabel("Signal strength in dBm")
plt.title("Comparison of antenna signal strength in test point #10")
plt.gca().invert_yaxis()
plt.show()