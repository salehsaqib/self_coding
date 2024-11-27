def main():    
    next_fib:int = 1
    fib:list = [0,1]
    list_ind:int = 1
    pre_list_ind:int = 1
    while (next_fib < 10000):        
        pre_list_ind = list_ind-1
        next_fib = int(fib[pre_list_ind]) + int(fib[list_ind])
        fib.append(next_fib)
        list_ind +=1
        
    for i in range(len(fib)-1):
        print(fib[i],end=" ")
    
        
        


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()