#!/usr/bin/python

from io import open

import sys, getopt
import csv
import json

reload(sys)
sys.setdefaultencoding("utf-8")

#Get Command Line Arguments
def main(argv):
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    read_csv(input_file, output_file)

#Read CSV File
def read_csv(file, json_file):
    csv_rows = []
    output = open(json_file, "w")
    with open(file, 'r', encoding='mac_roman') as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            cs_row = []
            cs_row = ([{title[i]:row[title[i]] for i in range(len(title))}])
            output.write(unicode(json.dumps(cs_row)))
            output.write(unicode("\n"))
    output.close()
# #Convert csv data into json and write it
# def write_json(data, json_file):
#     with open(json_file, "w") as f:
#         # if format == "pretty":
#         #     f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
#         # else:
#         # try:
#             f.write(unicode(json.dumps(data)))
#             f.write(unicode("\n"))

if __name__ == "__main__":
   main(sys.argv[1:])