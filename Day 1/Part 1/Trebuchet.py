# Trebuchet?!
import re

INPUT_FILE_PATH = 'input.txt'

def main():
    words = parse_input_file()
    arr = [Trebuchet(word) for word in words]
    print(sum(arr))

def Trebuchet(word) :
    nums = re.sub("[^0-9]","",word)
    num = int(nums[0] + nums[len(nums)-1])
    return num

def parse_input_file() :
    with open(INPUT_FILE_PATH, 'r') as f:
        words = f.read().split("\n")
    return words

if __name__ == "__main__":
    main()