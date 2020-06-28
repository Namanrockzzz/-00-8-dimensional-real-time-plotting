import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
x_vals = []
y_vals = []
index = count()
def animate(i):
	i=(i+1)%100
	data = pd.read_csv('data.csv')
	x = data['xv']
	y1 = data['yv1']
	y2 = data['yv2']
	y3 = data['yv3']
	y4 = data['yv4']
	y5 = data['yv5']
	y6 = data['yv6']
	y7 = data['yv7']
	y8 = data['yv8']
	
	'''
	plt.xlabel("X-axis")
	plt.ylabel("Y-axis")
	'''

	a1=plt.subplot(4,4,5)
	a1.cla()
	a1.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y1,label='Channel 1')
	
	a2=plt.subplot(4,4,2)
	a2.cla()
	a2.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y2,label='channel 2')
	
	a3=plt.subplot(4,4,3)
	a3.cla()
	a3.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y3,label='channel 3')
	
	a4=plt.subplot(4,4,8)
	a4.cla()
	a4.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y4,label='channel 4')
	
	a5=plt.subplot(4,4,9)
	a5.cla()
	a5.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y5,label='channel 5')
	
	a6=plt.subplot(4,4,14)
	a6.cla()
	a6.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y6,label='channel 6')
	
	a7=plt.subplot(4,4,15)
	a7.cla()
	a7.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y7,label='channel 7')
	
	a8=plt.subplot(4,4,12)
	a8.cla()
	a8.set_xlim(left = max(0,i-6),right = i+6)
	plt.plot(x,y8,label='channel 8')

	plt.tight_layout()
	j=i//100
	
ani1 = FuncAnimation(plt.gcf(), animate, interval=500, save_count=10)
'''
ani2 = FuncAnimation(plt.figure(2), animate, interval=1000)
ani3 = FuncAnimation(plt.figure(3), animate, interval=1000)
ani4 = FuncAnimation(plt.figure(4), animate, interval=1000)
ani5 = FuncAnimation(plt.figure(5), animate, interval=1000)
ani6 = FuncAnimation(plt.figure(6), animate, interval=1000)
ani7 = FuncAnimation(plt.figure(7), animate, interval=1000)
ani8 = FuncAnimation(plt.figure(8), animate, interval=1000)
'''
plt.tight_layout()
plt.show()
