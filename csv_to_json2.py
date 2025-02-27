#!/usr/bin/python

import sys, getopt
import csv
import json

reload(sys)
sys.setdefaultencoding("latin-1")

#Get Command Line Arguments
def main(argv):
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # format = ''
    # try:
    #     opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    # except getopt.GetoptError:
    #     print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
    #     sys.exit(2)
    # for opt, arg in opts:
    #     if opt == '-h':
    #         print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
    #         sys.exit()
    #     elif opt in ("-i", "--ifile"):
    #         input_file = arg
    #     elif opt in ("-o", "--ofile"):
    #         output_file = arg
    #     elif opt in ("-f", "--format"):
    #         format = arg
    read_csv(input_file, output_file)

#Read CSV File
def read_csv(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        # for row in csv_rows:   
        #     print(row["text"])
        write_json(csv_rows, json_file)

#Convert csv data into json and write it
def write_json(data, json_file):
    with open(json_file, "w") as f:
        # if format == "pretty":
        #     f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        # else:
        f.write(json.dumps(data))

if __name__ == "__main__":
   main(sys.argv[1:])