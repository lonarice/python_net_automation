from genie import testbed
import pprint
from prettytable import PrettyTable

d = {"devices":{
        "netc_test":{
            "connections":{
                "vty":{
                    "ip":"192.168.29.128",
                    "port":22,
                    "protocol":"ssh"
            }},
            "credentials":{
                "default":{
            "username":"admin",
            "password":"C1sco12345"}},
            "os":"iosxe"
        }
}}
def get_ver(device_inv,target_dev):
    test= testbed.load(device_inv)
    device = test.devices[target_dev]
    device.connect(log_stdout=False)
    x = device.parse('show version')
    t = PrettyTable(["chassis","Hostname","Version","up Time"])
    t.add_row([x['version']['chassis'],x['version']['hostname'],x['version']['version'],x['version']['uptime']])
    return(t)

def get_interface(device_inv,target_dev):
    test= testbed.load(device_inv)
    device = test.devices[target_dev]
    device.connect(log_stdout=False)
    x = device.parse('show ip interface brief')
    new_list=list(x['interface'].keys())
    t=PrettyTable(['interface',"IP","Status","Protocol"])
    for i in new_list:
        t.add_row([i,x['interface'][i]['ip_address'],x['interface'][i]['status'],x['interface'][i]['protocol']])
    return(t)
if __name__ == "__main__":
    
    y=get_interface(d,"netc_test")
    pprint.pprint(y)