
def main():    
    fruits = {
        "Apple": 12.25,
        "Mango": 50.05,
        "Banana": 50.05,
        "Grape": 60.50,
        "Pineapple": 30,
        "Orange": 40.70,
        "Guava": 25
    }
    tot_cost=0
    for x, y in fruits.items():        
        userNum:int = int(input(f"How many ({x}) do you want?: "))
        fruit_total:float = userNum*float(y)
        tot_cost += float(fruit_total)
    
    print(f"Your Total is {tot_cost}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()