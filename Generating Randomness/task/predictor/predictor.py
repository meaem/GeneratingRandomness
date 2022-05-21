def count_pattern(user_str,pattern):
    last_idx = user_str.find(pattern)
    zero_count = 0
    one_count = 0
    p_len = len(pattern)
    user_str_len = len(user_str)
    while last_idx != -1 and last_idx+p_len < user_str_len:
        if user_str[last_idx+p_len] == '0':
            zero_count +=1
        else: #if user_str[last_idx+p_len] == '1':
            one_count +=1
        last_idx +=1 # p_len
        last_idx=user_str.find(pattern,last_idx)
    return  zero_count,one_count


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
    for x in ['0','1']:
        for y in ['0','1']:
            for z in ['0','1']:
                pattern = f"{x}{y}{z}"
                zero_after,one_after = count_pattern(user_str,pattern)
                print(f"{pattern}: {zero_after},{one_after}")

main()