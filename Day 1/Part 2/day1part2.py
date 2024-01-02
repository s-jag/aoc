# Trebuchet?!
import re

INPUT_FILE_PATH = 'Day 1/input.txt'

def main():
    words = parse_input_file()
    arr = [Trebuchet(word) for word in words]
    print(sum(arr))

def Trebuchet(word) :
    replacements = [('one','o1e'),('two','t2o'),('three','thr3e'),('four','fo4r'),('five','fi5e'),('six','s6x'),('seven','sev7n'),('eight','ei8ht'),('nine','n9ne')]
    for (a,b) in replacements:
        word = word.replace(a,b)
    nums = re.sub("[^0-9]","",word)
    num = int(nums[0] + nums[len(nums)-1])
    # print(num)
    return num

def parse_input_file() :
    with open(INPUT_FILE_PATH, 'r') as f:
        words = f.read().split("\n")
    return words

if __name__ == "__main__":
    main()