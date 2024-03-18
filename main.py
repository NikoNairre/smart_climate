import os
from format_data import *
from utils import *
from copy import deepcopy
element_files = os.listdir("sample data/element data")

all_data_file = []
all_state_file = []

for i in range(0, 6000, 100):   #读取到所有编号的数据
    #读数据信息
    with open("sample data/element data/Z_SURF_I_00016-REG_2012121816" + str(i).zfill(4) + "_O_AWS-RD_FTM.txt") as f:
        data = f.read()
        line_data = data.split("\n")
        valid, cur_data = read_data(line_data, i)
        if valid:
            all_data_file.append(cur_data)

for i in range(0, 6000, 100):
    #读状态信息
    with open("sample data/state data/Z_SURF_I_00016-REG_2012121816" + str(i).zfill(4) + "_R_AWS-RD_FTM.txt") as f:
        data = f.read()
        line_data = data.split("\n")
        valid, cur_data = read_state(line_data, i)
        if valid:
            all_state_file.append(cur_data)
        

#直接给的数据太完美了，所以有个别数据进行了夸张的改动，仅是为了测试质控程序的功能
all_bad_QC = exam_quality(all_data_file)

#打印数据和状态的各种信息
t0: DataFile = all_data_file[0]
t1: StateFile = all_state_file[0]
print_DataFile(t0)
print_StateFile(t1)

print(all_bad_QC)

#将所有预警结果输出到QC_result文件夹下
with open("QC_result/result.txt", 'w') as f:
    for timestamp in all_bad_QC:
        if len(all_bad_QC[timestamp]) == 0:
            continue
        f.write(timestamp + '\n')
        for warning in all_bad_QC[timestamp]:
            f.write(warning + '\n')
        f.write('\n')



