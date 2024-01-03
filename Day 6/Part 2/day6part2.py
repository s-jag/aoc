import re
INPUT_FILE_PATH = 'Day 6/sample.txt'
import numpy




def main() :
    lines = parse_input_file()
    time = "" 
    record = ""
    count = 0
    for line in lines :
        arr = re.split("\s+", line)
        arr = arr[1:]
        if line.startswith("Time") :
            for x in arr :
                time += x
        else :
            for x in arr :
                record += x
    time = int(time) 
    record = int(record)
    for i in range(time) :
        x = i * (time - i)
        if x > record :
            count = time - (2 * i) + 1
            break
    print(count)        




def parse_input_file() :
    with open(INPUT_FILE_PATH, 'r') as f:
        l = f.read().split("\n")
    return l

if __name__ == "__main__":
    main()