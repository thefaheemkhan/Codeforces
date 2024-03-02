# Recursion Practice Questions

# WHAT is Recursion
# WHY use Recursion
# WHEN use Recursion
# HOW use Recursion

"""
#### Recursion Cheat Sheet
-> Base Case: Every recursive function must have one or more base cases to terminate the recursion. Base cases represent the simplest form of the problem and can be solved directly.
-> Recursive Step: Recursive functions break down the problem into smaller instances of the same problem. Each recursive call should bring the problem closer to the base case.
-> Convergence: Recursive algorithms must converge towards the base case(s) to terminate. Improper convergence can lead to infinite recursion.
-> Stack: Recursion uses the call stack to store information about each recursive call. Excessive recursion can lead to stack overflow errors.

#### Example Problems:
-> Factorial: Computing the factorial of a number.
-> Fibonacci Sequence: Generating Fibonacci numbers.
-> Tree Traversal: Pre-order, in-order, and post-order traversal of binary trees.
-> Recursive Binary Search: Searching for an element in a sorted array using recursion.
-> Merge Sort and Quick Sort: Sorting algorithms that use recursion.

#### Pros:
-> Elegant and intuitive solution for problems that can be divided into smaller subproblems.
-> Simplifies the code and makes it easier to understand.

#### Cons:
-> May consume more memory due to the overhead of function calls and maintaining the call stack.
-> Excessive recursion can lead to stack overflow errors.
-> Not always the most efficient solution, especially for problems with overlapping subproblems.

#### Optimization:
-> Tail Recursion: Optimizing recursive functions where the recursive call is the last operation performed.
-> Memoization: Storing the results of expensive function calls and reusing them to avoid redundant computations (dynamic programming).
-> Practice: Regular practice and understanding of recursion are essential to master its concepts and applications.
"""

# Global variable
counter = 0


# Q.1 Print name 10 times using recursion.
def recursion_1():
    global counter
    if counter == 10:
        return
    
    print("faheem")
    counter += 1
    recursion_1()


# Q.2 Print Linearly from 1 to n.
def recursion_2(n):
    global counter
    if counter == n:
        return
    print(counter+1)
    counter += 1
    recursion_2(n)


# Q.3 Print from n to 1.
def recursion_3(n):
    if n == 0:
        return
    print(n)
    n -=1 
    recursion_3(n)


# Q.4 Sum of 1st N numbers.
sum = 0
def recursion_4(n):
    global counter
    if counter == n+1:
        return
    global sum
    sum = sum + counter
    print(sum)
    counter += 1
    recursion_4(n)  


# Q.5 Factorial of N numbers. (Eg factorial of 5 is 5*4*3*2*1)
def recursion_5(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * recursion_5(n - 1)  # Recursive step: n! = n * (n-1)!


# Q.6 Reverse an array
# Q.7 Check if a string is palindrome or not.
# Q.8 Fibonacci number




# Driver Code Section
# recursion_1()
# recursion_2(5)
# recursion_3(5)
# recursion_4(5)
# result = recursion_5(5)  # Calculate factorial of 5 , print("Factorial of 5 is:", result)  # Output: 120
    

# Some more topics to be covered in Recursion
"""
    1. Parametrized and fubctional recursion_
    2. Problems on functional recursion_
    3. Multiple recursion calls
"""