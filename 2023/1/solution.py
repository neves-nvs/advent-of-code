#!/opt/homebrew/bin/python3

# https://adventofcode.com/2023/day/1

done = False
calibration = []
while not done:
    try:
        line = input()
        digits = ''.join(filter(lambda i: i.isdigit(), line))
        calibration.append(int(digits[0] + digits[-1]))
    except EOFError:
        done = True
print(sum(calibration))