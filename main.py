import os, sys
import json


result = []


def get_duplicates(a):
    folder_path = a
    folder = os.listdir(folder_path)
    print(folder)
    try:
        for file in folder:
            file_path = f'{folder_path}/{file}'
            json_file = json.load(open(file_path, encoding="utf8"))
            result = list(json_file.items())[1][2]
            pks = [(item['PK'], item['SK']) for item in result]
            res = list(set([item for item in pks if pks.count(item)>1]))
            print(f"All the duplicates from file:{file} are : + {res}")
            #sys.exit(0)

    except IndexError:
        print("Cannot access out of range elements")
        sys.exit(1)


def main():
    get_duplicates('C:\\Users\\harik\\Desktop\\decode-cx-backend-master\\decode-cx-backend-master\\fixtures')


if __name__ == "__main__":
    main()

