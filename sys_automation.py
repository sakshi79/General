#!/usr/bin/env python3
import shutil
#du = shutil.disk_usage("/")
#print(du)
import psutil
#print(psutil.cpu_percent(0.1))   
#print(psutil.cpu_percent(0.1))
#print(psutil.cpu_percent(0.5))
#print(psutil.cpu_percent(0.5))
# Here the numbers in the bracket are the time intervals
# ie, the duration for which we are calculating the average cpu usage
# we do so since the cpu usage is different at each instant of time.

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20   # returns True if more then 20% disk is free

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("Error!")
else:
    print("Everything is OK!")
    