
import re
INPUT_FILE_PATH = 'Day 2/input.txt'



def power(game) :
    game = game.replace(': ', ', ')
    game = game.replace('; ', ', ')
    arr = game.split(",")
    arr = arr[1:]
    blue = 0
    green = 0
    red = 0
    for word in arr :
        if ("blue" in word) :
            # print(int (re.sub("[^0-9]","",word)))
            if (int (re.sub("[^0-9]","",word)) > blue) :
                blue = int (re.sub("[^0-9]","",word))
        if ("red" in word) :
            # print(int (re.sub("[^0-9]","",word)))
            if (int (re.sub("[^0-9]","",word)) > red) :
                red = int (re.sub("[^0-9]","",word));
        if ("green" in word) :
            # print(int (re.sub("[^0-9]","",word)))
            if (int (re.sub("[^0-9]","",word)) > green) :
                green = int (re.sub("[^0-9]","",word));
    # print(red)
    # print(blue)
    # print(green)
    return (red * blue * green)
    
def main():
    games = parse_input_file()
    arr = [power(game) for game in games]
    print(arr)
    print(sum(arr))





def parse_input_file() :
    with open(INPUT_FILE_PATH, 'r') as f:
        l = f.read().split("\n")
    return l

if __name__ == "__main__":
    main()