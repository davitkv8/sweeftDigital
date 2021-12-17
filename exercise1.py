from jovian.pythondsa import evaluate_test_cases


def word_order(words, lines):
    if lines > 0:

        words_to_list = words.split('\n')
        words_dictionary = {}
        index = 0

        while index < lines:
            if words_to_list[index] != '':
                if words_to_list[index] in words_dictionary:
                    words_dictionary[words_to_list[index]] += 1
                else:
                    words_dictionary[words_to_list[index]] = 1

            index += 1

        occurrences = tuple(numb for numb in words_dictionary.values())
        if not occurrences:
            occurrences = 0,
    else:
        words_dictionary = {}
        occurrences = (0,)

    return {'distinct_words': len(words_dictionary),
            'occurrences': occurrences}


def visualize_word_order():

    lines = int(input("n :"))
    words = ''
    for i in range(lines):
        words += input() + '\n'

    print(word_order(words, lines))


visualize_word_order()


test_cases = [
    {'input': {'lines': 4, 'words': 'bcdef\nabcdefg\nbcde\nbcdef'},
     'output': {'distinct_words': 3, 'occurrences': (2, 1, 1)}},

    {'input': {'lines': 4, 'words': '\n\nword\nnext'},  # If lines are empty (not containing words)
     'output': {'distinct_words': 2, 'occurrences': (1, 1)}},

    {'input': {'lines': 0, 'words': ''},  # If 0 lines
     'output': {'distinct_words': 0, 'occurrences': (0,)}},

]

evaluate_test_cases(word_order, test_cases)  # Demonstrating with test cases
