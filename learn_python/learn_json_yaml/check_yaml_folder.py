import os
import sys
import yaml

file_list = [file for file in os.listdir(sys.argv[1]) if os.path.isfile(sys.argv[1] + "/" + file)]

def check_valid_yaml(file_name):
    try:
        with open(sys.argv[1] + "/" + file_name, "r") as f:
            test_file = yaml.safe_load(f)
            print(f"{file_name} is a valid YAML file")
    except yaml.YAMLError:
        print(f"{file_name} is NOT a valid YAML file")

for file in file_list:
    check_valid_yaml(file)
