import os
import sys
import json
import yaml

if len(sys.argv) > 1:
    # check file exists
    if os.path.exists(sys.argv[1]):
        # open file for reading
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    else:
        # alert user that file specified does not exist
        print("ERROR: File " + sys.argv[1] + " not found")
        exit(1)
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library
yaml_string = yaml.dump(source_content)
# 2. Save the YAML into a new file with the name for it received as a argument
# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
# 2.2 Check the target file doesn't already exist
# 2.3 If previous conditions not met, then save YAML file
if len(sys.argv) == 2:
    print(yaml_string)
elif os.path.exists(sys.argv[2]):
    print("File already exists")
else:
    with open(sys.argv[2], "w") as yaml_file:
        yaml_file.write(yaml_string)