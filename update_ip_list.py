import requests
import json

url = "https://ip-ranges.salesforce.com/ip-ranges.json"
output_file = "salesforce-ip-list.txt"

res = requests.get(url)
data = res.json()

ip_list = []

for item in data.get('ipv4_prefixes', []):
    ip_list.append(item['ipv4_prefix'])

for item in data.get('ipv6_prefixes', []):
    ip_list.append(item['ipv6_prefix'])

with open(output_file, 'w') as f:
    for ip in ip_list:
        f.write(ip + "\n")

print(f"Total IPs extracted: {len(ip_list)}")
