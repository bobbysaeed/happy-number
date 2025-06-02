def happy_number(num):
    seen_nums = set()
    while num != 1 and num not in seen_nums:
        seen_nums.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1