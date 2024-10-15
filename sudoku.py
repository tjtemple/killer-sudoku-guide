import itertools
import csv
from collections import defaultdict

nums = {9,8,7,6,5,4,3,2,1}

'''
for size in {2,3,4}:
    for combo in itertools.combinations(nums,size):
        print(combo)
        sums[sum(combo),size].append(combo)
'''

# should make file blank
with open("sums.csv","w") as f:
    pass

for size in {2,3,4,5}:
    sums = defaultdict(lambda:[])
    for combo in itertools.combinations(nums,size):
            string = ""
            for num in combo:
                string += str(num)
            sums[sum(combo)].append(string)

    header = []
    rows = defaultdict(lambda:[])
    max = 0
    for item in sums:
            header.append(f'{item}/{size}')
            '''
            for i in range(size):
                    print(f'{sums[sum]}[{i}] = {sums[sum][0][i]}')
                    rows[i].append(sums[sum][0][i])
            '''
            #print(f'{sum}/{size}: size = {len(sums[sum])}')
            if (len(sums[item])>max):
                max = len(sums[item])
    
    for item in sums:
        for i in range(max):
                    try:
                        #print(f'{sums[sum]}[{i}] = {sums[sum][i]}')
                        rows[i].append(sums[item][i])
                    except IndexError:
                        rows[i].append(" ")

    with open("sums.csv","a") as f:
        w = csv.writer(f)
        w.writerow(header)
        #print(header)
        for row in rows:
            w.writerow(rows[row])
            #print(rows[row])
