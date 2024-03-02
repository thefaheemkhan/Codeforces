# Printing diffreent types of patterns to understand loops better.

# Pattern 1
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
# Logic code Block Pattern-1
def pattern_1(n):
    for i in range(n):
        for j in range(n):
            print(" * ",end=" ")
        print()




# Pattern 2
"""
*
* *
* * *
* * * *
* * * * *
"""
# Logic code block Pattern- 2
def pattern_2(n):
    for i in range(n):
        for j in range(i):
            print(" * ", end=" ")
        print()



# Pattern 3
"""
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
"""
# Logic code block Pattern- 3
def pattern_3(n):
    for i in range(1,6):
        for j in range(1,i+1):
            print(j, end=" ")
        print()



# Pattern 4
"""
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5
"""
# Logic code block Pattern- 4
def pattern_4(n):
    for i in range(1,6):
        for j in range(1,i+1):
            print(i, end=" ")
        print()


# Pattern 5
"""
* * * * *
* * * *
* * *
* *
*
"""
# Logic code block Pattern- 5
def pattern_5(n):
    for i in range(n):
        for j in range(n-i):
            print(" * ", end=" ")
        print()


# Pattern 6
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
# Logic code block Pattern- 6
def pattern_6(n):
    for i in range(1, n + 1):
        print(" " * (n - i) * 2 + "* " * (2 * i - 1))



# Driver code Block
# pattern_1(5)
# pattern_2(6)
# pattern_3(5)
# pattern_4(5)
# pattern_5(5)
# pattern_6(5)