#avg
import csv
from collections import Counter

with open ('./project/HTWT.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
total = 0
for x in new_data:
    total = total + x

mean = total/n
print("Mean [Average] is: "+str(mean))

#median
new_dat = []
for i in range(len(file_data)):
    n_nu = file_data[i][2]
    new_dat.append(n_nu)

m = len(new_dat)
new_dat.sort()

if(m%2 == 0):
    #Getting 1st number:
    median1 = float(new_dat[m//2])
    
    #Gettin 2nd number:
    median2 = float(new_dat[(m//2)-1])

    median = (median1+median2)/2
else:
    median = float(new_dat[n//2])

print('median is: ' + str(median))

#mode
new_da=[]
for i in range(len(file_data)):
	n_n = file_data[i][1]
	new_da.append(n_n)



#Calculating Mode
da = Counter(new_da)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in da.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
