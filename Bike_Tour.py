# Kickstart_Problem
#Round_B_2020
#Bike_Tour

T = int(input())
for x in range(1,T+1):
    count = 0
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(N):
        if i != 0 and i!= N-1:
            if A[i]> A[i-1]and A[i]>A[i+1]:
                count += 1
            else:
                pass
    
    print("Case "+"#{}".format(x)+": "+str(count))
"""
 #The above code is the solution for the KickStart 2020 Round_B.
 ##Bike Tour Problem.

   ///////////Soul Corporation////////////

Contact us @profsoul23@gmail.com

"""
    
