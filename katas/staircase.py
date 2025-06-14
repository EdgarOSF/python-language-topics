'''
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Function Description

Complete the  function with the following parameter(s):

: an integer
Print

Print a staircase as described above. No value should be returned.
Note: The last line is not preceded by spaces. All lines are right-aligned.

Input Format

A single integer, , denoting the size of the staircase.
'''


def staircase(n):
    # Write your code here
    stars = ''
    for i in range(1, n + 1):
        stars = ' ' * (n - i)
        stars += '#' * i
        print(stars)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
