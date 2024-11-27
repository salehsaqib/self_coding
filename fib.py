def main():    
    MAX_FIB:int = 10000
    pre_fib:int = 0
    curr_fib:int = 1
    print(pre_fib, end = " ")
    while (curr_fib < MAX_FIB):                
        print(curr_fib, end=" ")
        next_fib = pre_fib + curr_fib
        pre_fib = curr_fib
        curr_fib  = next_fib

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()