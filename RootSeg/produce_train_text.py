import os
import numpy as np

# img path
initial_path = ""
# label path
processed_path = ""
# the path to save train.txt
txt_savepath = ""
initial_list = os.listdir(initial_path)
processed_list = os.listdir(processed_path)

if (len(initial_list) != len(processed_list)):
    print("The number of files is inconsistent")

a = []
for i in initial_list:
    a.append(i.split(".")[0])

b = []
for i in processed_list:
    b.append(i.split(".")[0])

t = len(a) if len(a) > len(b) else len(b)

for i in range(0, t):
    if (b[i] not in a):
        print(b[i])

for i in range(0, len(a)):
    if (a[i] not in b):
        print(a[i])

train_list = []
for i in range(0, len(initial_list)):
    print("Add " + initial_list[i] + " And " + processed_list[i])
    train_list.append(initial_list[i] + ";" + processed_list[i])

np.savetxt(txt_savepath, train_list, fmt='%s')
