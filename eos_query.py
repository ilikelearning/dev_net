import pyeapi

device_list = ['192.168.1.54', '192.168.1.56']

with open("eos_output_sample.txt", "w") as fl:
	for device in device_list:
		node = pyeapi.connect(transport="https", host=device, username="dev_user", password="dev_pass", port=None)
		ip_addr = node.execute(["show ip interface brief"])
		int_discard = node.execute(["show interfaces counters discards"])
		version = node.execute(["show version"])

		print(f"\n{device} - EOS {version['result'][0]['version']} | IP Address Information")
		print("-"*51)
		fl.write(f"\n{device} - EOS {version['result'][0]['version']} | IP Address Information\n")
		fl.write("-"*51)
		fl.write("\n")

		for intf in ip_addr['result'][0]['interfaces']:
			print("| {} has ip address {}/{} configured".format(intf, ip_addr['result'][0]['interfaces'][intf]['interfaceAddress']['ipAddr']['address'], 
			ip_addr['result'][0]['interfaces'][intf]['interfaceAddress']['ipAddr']['maskLen']))
			fl.write(f"| {intf} has ip address {ip_addr['result'][0]['interfaces'][intf]['interfaceAddress']['ipAddr']['address']}/{ip_addr['result'][0]['interfaces'][intf]['interfaceAddress']['ipAddr']['maskLen']}\n")
		
		print("+")
		fl.write("+\n")

		for intf in int_discard['result'][0]['interfaces']:
			print("| {} has {} Input Discards".format(intf,int_discard['result'][0]['interfaces'][intf]['inDiscards']))
			fl.write(f"| {intf} has {int_discard['result'][0]['interfaces'][intf]['inDiscards']} Input Discards\n")


