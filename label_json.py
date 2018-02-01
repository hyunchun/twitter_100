from __future__ import print_function
from __future__ import division
try:
    import json
except ImportError:
    import simplejson as json
import string
import sys

# ----- labeler function ----- #
def labeler_json():
    filename = sys.argv[1]
    inFile = open("%s" %(filename), "r")
    category_list = []
    for line in inFile:
        tweet = json.loads(line.strip())
        print(tweet['screen_name'])
        print(tweet['text'].encode(encoding="utf-8"))
        input_category = raw_input("Label: ")
        if (input_category == "previous") or (input_category == "Previous") or (input_category == "pervious") or (input_category == "Pervious") or (input_category == "prev") or (input_category == "perv"):
            category_list.pop()
            print(prev_line)
            new_input = raw_input("New label for previous line: ")
            category_list.append(new_input)
            print(['screen_name'])
            print(tweet['text'].encode(encoding="utf-8"))
            input_category = raw_input("Label: ")
        category_list.append(input_category)
        prev_line = tweet['text'].encode(encoding="utf-8")

    inFile.close()
    inFile = open("%s" %(filename), "r")   
    filename += "_labeled"
    outFile = open("%s" %(filename), "w")
    count = 0
    print("labeling....")
    for line in inFile:
        tweet = json.loads(line.strip())
        tweet['category'] = category_list[count]
        count += 1
        outFile.write(json.dumps(tweet))
        outFile.write('\n')

    # checker_active = raw_input("do you want to check: ")
    # if int(checker_active) == 1:
    #     print(json.dumps(tweet, indent=4))

    inFile.close()
    outFile.close()
    print("tweet text saved in file: %s" %(filename))
    print("%s entries read" %(count))

# ----- main ----- #
def main():
    labeler_json()

# ---------------------- #
if __name__ == "__main__":
    main()
