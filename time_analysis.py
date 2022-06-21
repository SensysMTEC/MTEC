from matplotlib import pyplot as plt
import os
import os.path
import subprocess
import argparse
import configparser

mini=1000000000000000000000
maxi=0
if __name__ =='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--c', type=int, nargs="?")
	parser.add_argument('--f', type=str, nargs="?")
	args = parser.parse_args()
	time_list = [args.f]
	average_latency=[]
	detail_latency=[]
	count = args.c
	for each in time_list:
		latency_dict={}
		scheme_latency=[]

		file = open(each,"r")
		instance = 1
		latency_tot = 0
		while instance < count*2+1:
			time_stamp = file.readline()
			if time_stamp == "\n":
				break
			time_stamp = time_stamp.split(":")
			#print(time_stamp)
			if len(time_stamp) == 2:
				first_half = time_stamp[0]
				stamp = int(time_stamp[1])
				if stamp < mini:
					mini = stamp
				if stamp > maxi:
					maxi = stamp
				first_half = first_half.split(" ")
				if first_half[1] not in latency_dict.keys():
					latency_dict[first_half[1]]=[stamp]
				else:
					latency_dict[first_half[1]].append(stamp)
			instance+=1
		result_received = 0 
		for i in range(1,count+1):
			if len(latency_dict[str(i)]) == 2:
				result_received+=1
				latency = abs(latency_dict[str(i)][1]-latency_dict[str(i)][0])/1000000000
				#print(latency)
				scheme_latency.append(latency)
				latency_tot += latency
		print("average: {}".format(latency_tot/result_received))
		print(f"throughput: {(maxi-mini)/(1000000000*result_received)}")
		print(f"result received :{result_received}")

