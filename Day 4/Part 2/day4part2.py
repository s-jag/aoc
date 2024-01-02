import re
INPUT_FILE_PATH = 'Day 4/input.txt'

# def findScore(card) :
#     arr = re.split("\s+", card)
#     winning_numbers = arr[2:7]
#     card_numbers = arr[8:]
#     count = 0
#     for num in card_numbers :
#         if num in winning_numbers :
#             count += 1
#     return 0 if count == 0 else 2**(count - 1)

def main():
    cards = parse_input_file()
    arr = [(1) for i in range (len(cards))]
    for card in cards:
        idx = cards.index(card)
        temp = re.split("\s+", card)
        winning_numbers = temp[2:12]
        card_numbers = temp[13:]
        count = 0
        for num in card_numbers :
            if num in winning_numbers :
                count += 1
        for i in range(count) :
            if (i + idx + 1 < len(cards)) :
                arr[i + idx + 1] += arr[idx]
    print(sum(arr))






def parse_input_file() :
    with open(INPUT_FILE_PATH, 'r') as f:
        l = f.read().split("\n")
    return l

if __name__ == "__main__":
    main()