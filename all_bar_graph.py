import numpy as np  
import matplotlib.pyplot as plt  

# Grouping variable  
X = ['#1','#2','#3','#4','#5','#6','#7','#8','#9','#10'] 

usb_nic = [-39.6, -67.2, -65.9, -62.2, -74.5, -75.3, -74.4, -74.6, -70, -77.4] 
cantenna = [-55.6, -61.7, -60.7, -45.8, -77, -72.9, -73.6, -63.6, -63.3, -79.9] 
colander = [-48.2, -76.9, -63.8, -60.7, -72.3, -73.8, -74.8, -72.9, -72.6, -76.6]
alfa_nic = [-32.3, -45.2, -48.7, -34.4, -49.1, -54.2, -56.4, -49.4, -49.9, -54.2]

X_axis = np.arange(len(X)) 
  
plt.rcParams["figure.figsize"] = [17.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.bar(X_axis - 0.5, usb_nic, 0.25, label = 'USB NIC') 
plt.bar(X_axis - 0.25, cantenna, 0.25, label = 'Cantenna')
plt.bar(X_axis, colander, 0.25, label = 'Colander') 
plt.bar(X_axis + 0.25, alfa_nic, 0.25, label = 'Alfa NIC') 

  
plt.xticks(X_axis + 0.25 / 4, X) 
plt.xlabel("Test sites") 
plt.ylabel("dBm value") 
plt.title("Comparison of signal strength from all test sites") 
plt.legend() 
plt.gca().invert_yaxis()
plt.show() 
