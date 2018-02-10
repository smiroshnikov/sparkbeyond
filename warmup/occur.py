""""
will check for max words occurrences in single file
"""


def occurance_of_words_file(N_most_occured_words, file_path):
    dict = {}
    occur_dict = {}
    with open(file_path) as f:
        lines = f.readlines()
    words = [line for line in lines]
    # words = lines.split(" ")
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    for x in range(0, N_most_occured_words):
        max_item = max(dict, key=dict.get)  # Just use 'min' instead of 'max' for minimum.
        occur_dict[max_item] = dict[max_item]  # word : occurs
        del dict[max_item]
    return occur_dict


result = occurance_of_words_file(3, "my_word_file.txt")
for k, v in result.items():
    print(k, v)
