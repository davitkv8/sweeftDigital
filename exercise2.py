from jovian.pythondsa import evaluate_test_cases

test_cases = [
    {'input': {'w': 'ab'}, 'output': 'ba'},
    {'input': {'w': 'bb'}, 'output': 'no answer'},
    {'input': {'w': 'hefg'}, 'output': 'hegf'},
    {'input': {'w': 'dhck'}, 'output': 'dhkc'},
    {'input': {'w': 'dkhc'}, 'output': 'hcdk'},
    {'input': {'w': 'a'}, 'output': 'no answer'},
]

def bigger_is_greater(w):
    word_length = w.__len__()
    i = word_length - 1
    if i > 0:
        while w[i] <= w[i-1]:
            i -= 1
            if i == 0:
                return 'no answer'

        to_list = list(w[0:i])+(sorted(w[i:]))

        if i == 1 and word_length > 2:
            to_list[i - 1], to_list[i+1] = to_list[i+1], to_list[i - 1]
        else:
            to_list[i-1], to_list[-1] = to_list[-1], to_list[i-1]

        return ''.join(to_list)
    return 'no answer'


evaluate_test_cases(bigger_is_greater, test_cases)
