#!/usr/bin/env python3

import re
import operator
import csv 

errors = {}
per_users = {}


with open('sys.txt') as file:
    lines = file.readlines()
    for line in lines:
       # print(line)
        match_i = re.search('ERROR\s((\w*\s){2,})\((\w*)\)', line)
        if match_i != None:
            if match_i.group(1) not in errors:
                errors[match_i.group(1)] = 1
            else:
                errors[match_i.group(1)] += 1
            
            if match_i.group(3) not in per_users.keys():
                per_users[match_i.group(3)] = {'errors': 1, 'info': 0}
            else:
                per_users[match_i.group(3)]['errors'] += 1

        match_info = re.search('INFO\s(\w*\s){2,}(\[#\d*\])\s\((\w*)\)', line)
        if match_info != None:
            if match_info.group(3) not in per_users.keys():
                per_users[match_info.group(3)] = {'errors': 0, 'info': 1}
            else:
                per_users[match_info.group(3)]['info'] += 1



        
            

errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
per_users = sorted(per_users.items(), key=operator.itemgetter(0))
dict_errors = dict(errors)
dict_users  = dict(per_users)



field_names = ['Error', 'Count']

with open('errors.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for error, count in dict_errors.items():
        writer.writerow({'Error':error, 'Count': count})


field_names2 = ['Username', 'INFO', 'ERROR']
with open('users.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames = field_names2)
    writer.writeheader()
    for name, value in dict_users.items():
        writer.writerow({'Username': name, 'INFO': value['info'], 'ERROR': value['errors']})

