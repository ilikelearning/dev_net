import pyeapi

device_list = ['192.168.1.54', '192.168.1.56']

for device in device_list:
	node = pyeapi.connect(transport="https", host=device, username="dev_user", password="dev_pass", port=None)
	ip_addr = node.execute(["show ip interface brief"])
	int_discard = node.execute(["show interfaces counters discards"])
	version = node.execute(["show version"])

	print(f"\n{device} - EOS {version['result'][0]['version']} | IP Address Information")
	print("-"*51)

	for intf in ip_addr['result'][0]['interfaces']:
		print("| {} has ip address {}/{} configured".format(intf, ip_addr['result'][0]['interfaces'][intf]['interfaceAddress']['ipAddr']['address'], 
		ip_addr['result'][0]['interfaces'][intf]['interfaceAddress']['ipAddr']['maskLen']))
		
	print("+")

	for intf in int_discard['result'][0]['interfaces']:
		print("| {} has {} inDiscards".format(intf,int_discard['result'][0]['interfaces'][intf]['inDiscards']))
