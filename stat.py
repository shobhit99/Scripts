import subprocess
import time
import re
import csv
from datetime import datetime
from multiprocessing import Process

output_list = []
mem_used_list = []
cpu_output_list = []
network_stat_down = []
network_stat_up = []
times = []
def bmon():
	net_output = subprocess.check_output("bmon -o ascii > net_op",shell=True)

def getinkb(val):
	if val.endswith("KiB"):
		return val.strip("KiB")
	elif val.endswith("MiB"):
		return float(val.strip("MiB"))*1000
	elif val.endswith("B"):
		return float(val.strip("B"))/1000
try:
	p = Process(target=bmon)
	p.start()
	while True:
		cpu_output = subprocess.check_output("top -b -n1 | grep 'Cpu(s)' | awk '{print $2 + $4}'",shell=True)
		mem_output = subprocess.check_output("free -m | grep Mem",shell=True)

		mem_output = mem_output.split()
		total_mem = float(mem_output[1])
		available_mem = float(mem_output[2])
		mem_used = (available_mem/total_mem)*100
		
		mem_used_list.append(mem_used)
		cpu_output_list.append(cpu_output.strip("\n"))
		times.append(time.time())
		time.sleep(1)
except:
	
	net_output_data = open("net_op","r").read()
	data = re.findall(r".+eth0.+",net_output_data)
	for d in data:
		values = d.split()
		down = getinkb(values[1])
		up = getinkb(values[3])
		network_stat_up.append(up)
		network_stat_down.append(down)
	ts = int(time.time())
	with open("{}.csv".format(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')), "w") as csvfile:
		fields = ['Timestamp','Memory Usage','Cpu Usage','Network Down','Network Up']
		csvwriter = csv.writer(csvfile, delimiter=',')
		csvwriter.writerow(fields)
		for i in range(len(mem_used_list)):
			arr = [times[i],mem_used_list[i],cpu_output_list[i],network_stat_down[i],network_stat_up[i]]
			csvwriter.writerow(arr)
	
