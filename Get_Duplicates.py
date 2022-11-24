import os
import json
folder_path = r'C:\Users\harik\Desktop\decode-cx-backend-master\decode-cx-backend-master\fixtures'

folder = os.listdir(folder_path)

def fileread(path):
    file = open(path, encoding="utf8")
    return file.read()
result=[]
print(folder)

def get_duplicates():
    for file in folder:
        file_path = f'{folder_path}/{file}'
        json_file = json.load(open(file_path, encoding="utf8"))

        result = list(json_file.items())[1][1]
        # print(f"result:{result}")
        pks = [(item['PK'], item['SK']) for item in result]
        res = list(set([item for item in pks
                        if pks.count(item) > 1]))
        print(f"All the duplicates from file:{file} are : + {res}")

get_duplicates()