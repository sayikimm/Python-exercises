def find_most_frequent(lists):
    map = {}
    for item in lists:
        if item in map:
            map[item] += 1
        else:
            map[item] = 1

    max_num_of_word = 0
    word = None

    for item in map:
        if map[item] > max_num_of_word:
            word = item
            max_num_of_word = map[item]
    print(word)

find_most_frequent([])
