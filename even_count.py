def main():    
    nums:dict = {}
    while True:
        userNum:str = str(input("Enter Any Number(None for End) : "))
        if userNum=="":
            break
        if userNum in nums:
            x:int = int(nums[userNum])+1
            nums.update({userNum:x})
        else:
            nums.update({userNum:1})
    for x, y in nums.items():
        print(f"{x} appears {y} times")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()