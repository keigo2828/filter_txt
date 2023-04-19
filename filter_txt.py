import shutil
import os
import glob
import time



def move_glob(dst_path,recursive=True):
    with open('./list.txt') as f:
        for line in f:
            year = line[0:2]
            number = line[4:7]
            P = glob.glob(f"./input_file/*{year}*{number}.txt", recursive=recursive)
            for p in P:
                #print(p[0],year,number)
                shutil.move(p, dst_path)


current_dir_path = os.getcwd()
output_file_path = current_dir_path + '/output_file'
input_file_path = current_dir_path + '/input_file'

os.makedirs(output_file_path, exist_ok = True) 
os.makedirs(input_file_path, exist_ok = True) 

#print(glob.glob(input_file_path + '/*.txt'))

move_glob(output_file_path)