def pattern(n):
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n-1 or col ==0 or col ==n-1:
                print(1,end=" ")
            elif col+row == n//2+1 or col-row == n//2-1 or row-col == n//2-1 or row+col == n//2 + n-2:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print()
            


if __name__ == "__main__":
    while True:
        number = int(input('Enter Number here '))
        if number % 2 != 0 :
            break
        else:
            print('Enter Odd Number!!! ')
    pattern(number)
