
# arr = [1,2,3,4,5]

def miniMaxSum(arr):
    # Write your code here
    arr.sort()



    # for i in arr:
    #     if i != arr[-1]:
    #         min_sum += i
    #     if i != arr[0]:
    #         max_sum += i

    print( sum(arr[:-1]), sum(arr[1:])) 

if __name__ == '__main__':
    # arr = [1,2,3,4,5]
    arr = [7, 69, 2, 221, 8974]

    # arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)