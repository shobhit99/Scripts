import re

user_list = ['user11', 'user12', 'user21', 'user22', 'user23', 'user24', 'user31', 'user32', 'user41', 'user42', 'user51', 'user52', 'user61', 'user62', 'user63', 'user64']
pt_list = [2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2214, 2215, 2216, 2217]
userdict = dict(zip(pt_list,user_list))

with open("output.csv", "r") as f:
	data = f.read()
	for port in pt_list:
		pattern = '"\d{10}\.\d{9}","\S{17}","\d{2,5}","'+str(port)+'"'
		d = re.findall(pattern,data)
		if d != []:
			with open("{}.log".format(userdict[port]), "w") as k:
				k.write('\n'.join(d))