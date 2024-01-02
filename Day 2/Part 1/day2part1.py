
import re
INPUT_FILE_PATH = 'Day 2/input.txt'



def isValid(game, idx) :
    game = game.replace(': ', ', ')
    game = game.replace('; ', ', ')
    arr = game.split(",")
    arr = arr[1:]
    for word in arr :
        if ("blue" in word) :
            if (int (re.sub("[^0-9]","",word)) <= 14) :
                continue;
            else :
                # print(word  + " blue")
                return 0
        if ("red" in word) :
            if (int (re.sub("[^0-9]","",word)) <= 12) :
                continue;
            else :
                # print(word  + " red")
                return 0
        if ("green" in word) :
            if (int (re.sub("[^0-9]","",word)) <= 13) :
                continue;
            else :
                # print(word + " "  + " green")
                return 0
    return idx + 1
    
def main():
    games = parse_input_file()
    arr = [isValid(game, games.index(game)) for game in games]
    print(arr)
    print(sum(arr))





def parse_input_file() :
    with open(INPUT_FILE_PATH, 'r') as f:
        l = f.read().split("\n")
    return l

if __name__ == "__main__":
    main()