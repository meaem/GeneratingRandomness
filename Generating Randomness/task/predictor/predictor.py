import random

LEAST_LENGTH = 100


def count_pattern(user_str, pattern):
    last_idx = user_str.find(pattern)
    zero_count = 0
    one_count = 0
    p_len = len(pattern)
    user_str_len = len(user_str)
    while last_idx != -1 and last_idx + p_len < user_str_len:
        if user_str[last_idx + p_len] == '0':
            zero_count += 1
        else:  # if user_str[last_idx+p_len] == '1':
            one_count += 1
        last_idx += 1  # p_len
        last_idx = user_str.find(pattern, last_idx)
    return zero_count, one_count


def clean_str(s):
    result = ""
    for c in s:
        if c == '0' or c == '1':
            # count +=1
            result += c
    return result


def count_correct(test_str, pridication_str):
    return sum([1 if x == y else 0 for x, y in zip(test_str, pridication_str)])


def predict(test, stats):
    predition = ""
    for _ in range(3):
        predition += str(random.randint(0, 1))

    for i in range(3, len(test)):
        triad = test[i - 3:i]
        # print(f"triad: {triad}")
        results = stats[triad]

        if results[0] > results[1]:
            predition += '0'
        else:
            predition += '1'
        # print(f"triad: {triad} results: {results} prediction: {predition}")
    return predition


def main():
    user_str = ""
    while len(user_str) < LEAST_LENGTH:
        print('Print a random string containing 0 or 1:')
        s = input()
        user_str += clean_str(s)
        if LEAST_LENGTH - len(user_str) > 0:
            print(f"Current data length is {len(s)}, {LEAST_LENGTH - len(user_str)} symbols left")
    print(f"Final data string:\n{user_str}")
    stats = {}
    for x in ['0', '1']:
        for y in ['0', '1']:
            for z in ['0', '1']:
                pattern = f"{x}{y}{z}"
                zero_after, one_after = count_pattern(user_str, pattern)
                print(f"{pattern}: {zero_after},{one_after}")
                stats[pattern] = (zero_after, one_after)
    print("Please enter a test string containing 0 or 1:")
    test_str = clean_str(input())
    pridication_str = predict(test_str, stats)
    print(f"prediction:\n{pridication_str}")
    correct = count_correct(test_str[3:], pridication_str[3:])
    print(
        f"Computer guessed right {correct} out of {len(test_str[3:])} symbols ({100 * correct / len(test_str[3:]):.2f} %)")


# print(max((5, 8)))
main()
# 0010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
# 0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010