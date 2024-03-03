# Recursion Eamples

# Q.1 Print name N times using recursion.
def name_print(i,n):
    if n+1 <=i:
        return
    
    print("Faheem")
    name_print(i+1,n)


# Q.2 Print linearly from 1 to N.
def linear_1ton(i,n):
    if i >= n+1:
        return
    print(i)
    linear_1ton(i+1,n)


# Q.3 Print N to 1.
def print_nto1(i,n):
    if n == i:
        return
    print(n-i)
    print_nto1(i+1,n)


# Q.4 Print linearly from 1 to N, by backtracking.
def linearly_1ton_backtracking(i):
    if i<1:
        return 
    linearly_1ton_backtracking(i-1)
    print(i)


# Q.5 Print N to 1 by backtracking.
def print_nto1_backtarcking(i,n):
    if i>n :
        return
    print_nto1_backtarcking(i+1,n)
    print(i)
    

# Q.6 Summation of N natural numbers. # Paramertrized way
def sum_of_n_natural_numbers(i,sum):
    if i<1:
        print(sum)
        return
    sum_of_n_natural_numbers(i-1,sum+i)


# Q.7 Summation of N natural bumbers. # Functional way
def sum_of_n_natural_numbers_func(n):
    if n == 0:
        return 0
    return n + sum_of_n_natural_numbers_func(n-1)




# Driver Code
# name_print(1,3)
# linear_1ton(1,5)
# print_nto1(0,5)
# linearly_1ton_backtracking(5)
# print_nto1_backtarcking(1,5)
# sum_of_n_natural_numbers(5,0)
# print(sum_of_n_natural_numbers_func(10))

    