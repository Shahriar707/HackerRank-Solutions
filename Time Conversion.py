import os

def timeConversion(s):
    hour = int(s[:2])
    minutes = s[3:5]
    seconds = s[6:8]
    period = s[-2:]

    if period == 'AM':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minutes}:{seconds}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    fptr.write(result + '\n')
    fptr.close()
