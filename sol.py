// coded by harish rane

n  = int(input("Enter the number of types list should repeat"))
L = [1,2,3]

for i in range(1,n+1,1):
    L = L+L

print(L)
