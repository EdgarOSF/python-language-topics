
arr = [1,2,3,4,5]

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0

    for i in arr:
        if i != arr[-1]:
            min_sum += i
        if i != arr[0]:
            max_sum += i

    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = [1,2,3,4,5]

    # arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)