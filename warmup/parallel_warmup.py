import string

import time

import multiprocessing


def count_words_that_start_with_letter(word_list, letter='A'):
    required_letter_count = 0
    for line in word_list:
        if line.startswith(letter):
            required_letter_count += 1
    print("there are " + str(required_letter_count) + " words that start with '" + letter + "'")
    return required_letter_count


def check_if_any_double_letter_exist(word_list):
    creepy_word_list = []

    for letter in string.ascii_lowercase:
        exists = False
        print("checking letter ..." + letter)
        for word in word_list:
            print("checking word --> " + word + "and double letter  ----> " + letter)
            if letter * 2 in word:
                exists = True
                creepy_word_list.append(word)
                print("added " + word)
        if not exists:
            print("there are no english words with double " + letter)

    print(str(len(creepy_word_list)) + "total words in list ")
    return creepy_word_list


if __name__ == "__main__":
    start = time.time()

    with open('words.txt') as f:  # difference between using file and with
        lines = f.readlines()
        lines = [line for line in lines]  # convert lines into string

    pool = multiprocessing.Pool()  # I define separate process for each line
    double_word_list = check_if_any_double_letter_exist(lines)

    print(f'total  letter words in english dictionary of :{len(double_word_list)}')
    end = time.time()
    print(f'Time to complete: {end - start:.2f}')

"""
max words argument == 2 
dick 1900 raz 
penis 3500
hashtable


"""
