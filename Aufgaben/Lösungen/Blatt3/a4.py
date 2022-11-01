import random


def get_answer_options(options):
    answer = options[0]
    # Take the remaining options ([1:]) and shuffle them
    shuffled_options = options[1:]
    random.shuffle(shuffled_options)
    # Take the first 3 of the shuffled options
    result = shuffled_options[0:3]
    # Append the correct solution
    result.append(answer)
    # Shuffle again, so that the correct solution is not
    # always at the end
    random.shuffle(result)
    return result


countries = ["Deutschland", "Frankreich", "Italien", "Spanien", "Kroatien", "Niederlande", "Belgien", "Polen", "Ungarn"]

print(get_answer_options(countries))
