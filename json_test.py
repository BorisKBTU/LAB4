import json
import pandas as pd
from tabulate import tabulate

with open('sample-data.json', 'r') as file:
    df = json.load(file)
print_dict = []
for i in df['imdata']:
    elem = i['l1PhysIf']['attributes']
    new_elem = [elem["dn"], ' ', elem['speed'], elem['mtu']]
    print_dict.append(new_elem)
headers = ['DN', 'Description', 'Speed', 'MTU']
print('Interface Status')
print(tabulate(print_dict, headers=headers, tablefmt="grid"))
