import re
INPUT_FILE_PATH = 'Day 6/input.txt'
import numpy




def main() :
    lines = parse_input_file()

    times = []
    records = []
    counts = [0, 0, 0, 0]
    for line in lines :
        arr = re.split("\s+", line)
        arr = arr[1:]
        if line.startswith("Time") :
            times = [int(x) for x in arr]
        else :
            records = [int(x) for x in arr]

    for time in times :
        for i in range(time) :
            x = i * (time - i)
            if x > records[times.index(time)] :
                counts[times.index(time)] += 1
    print(numpy.prod(counts))        




def parse_input_file() :
    with open(INPUT_FILE_PATH, 'r') as f:
        l = f.read().split("\n")
    return l

if __name__ == "__main__":
    main()