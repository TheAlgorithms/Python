import json
import os
import sys

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1])
        json.load(file)
        file.close()
        print("Validate JSON!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkjson.py <file>")


"""
    To run it use :

        checkJSON test.json

"""
