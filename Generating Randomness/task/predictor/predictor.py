


def main():
    user_str = ""
    while len(user_str) < 100:
        print('Print a random string containing 0 or 1:')
        s = input()
        count = 0
        for c in s:
            if c == '0' or c == '1':
                count +=1
                user_str += c
        if 100-len(user_str) > 0:
            print(f"Current data length is {len(s)}, {100-len(user_str)} symbols left")
    print(f"Final data string:\n{user_str}")


main()