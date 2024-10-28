def plusMinus(arr):
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)

    total = len(arr)

    print(f"{positive_count / total:.6f}")
    print(f"{negative_count / total:.6f}")
    print(f"{zero_count / total:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
