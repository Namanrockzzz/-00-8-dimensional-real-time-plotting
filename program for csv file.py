import csv
from random import uniform as fl
import time

x=0
y1=0.5
y2=29.4
y3=34.7
y4=46.81
y5=62.23
y6=77.732
y7=85.65
y8=93.86
fieldnames=["xv","yv1","yv2","yv3","yv4","yv5","yv6","yv7","yv8"]

with open('data.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while x<100:
    with open('data.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info={
            "xv": x,
            "yv1": y1,
            "yv2":y2,
            "yv3":y3,
            "yv4":y4,
            "yv5":y5,
            "yv6":y6,
            "yv7":y7,
            "yv8":y8
            }
        csv_writer.writerow(info)
        print(x, y1,y2,y3,y4,y5,y6,y7,y8)

        x=x+1
        y1=fl(0.0,10.0)
        y2=fl(20.0,30.0)
        y3=fl(30.0,40.0)
        y4=fl(40.0,50.0)
        y5=fl(60.0,70.0)
        y6=fl(70.0,80.0)
        y7=fl(80.0,90.0)
        y8=fl(90.0,100.0)

    time.sleep(0.5)
