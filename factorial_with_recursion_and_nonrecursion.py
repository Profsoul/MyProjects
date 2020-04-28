user_input = int(input("Enter the number to find the factorial "))

ask = input("Recursive or non-recursive ").lower()
result = 1
if ask == 'non-recursive':
    for i in range(user_input):
        i += 1
        result *= i
    print(result)
elif ask == 'recursive':
    def facto(n):
        if n==0 or n ==1:
            return 1
        else:
            return n*facto(n-1)
    result = facto(user_input)
    print(result)

else:
    print("Please enter the valid the one!!!")
