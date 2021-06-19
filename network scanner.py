
import scapy.all as scapy
import time
def scan(ip):
   # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst= 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
    
    arr = []          
    for i in answered_list:
        #print(i[1].psrc+"\t\t\t"+i[1].hwsrc)
        dict = {"ip":i[1].psrc,"mac":i[1].hwsrc}
        arr.append(dict)
    return arr    
        
        #print(i[1].hwsrc)
        #print("---------------------------")

def printfun(re):
    print("    IP \t\t\t\t MAC Address")
    print("-------------------------------------------------")
    for i in re:
        print(i["ip"]+"\t\t\t"+i["mac"])
# def get_mac(ip):
#     arp_request = scapy.ARP(pdst = ip)
#     broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast / arp_request
#     answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
#     return answered_list

#k = get_mac("192.168.29.1/24")

s = input("Enter the Target ip with /(no of block scan) EX:-192.168.29.1/24\n")
k = scan(s)
printfun(k)
