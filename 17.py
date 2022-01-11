# Write a python program to find the sum of the series 1+11+111+1111.. up to n terms,using function.

def find_sum(n):
    sum = 0
    j = 1
     
    for i in range(1, n + 1):
        sum = sum + j
        j = (j * 10) + 1
    return sum
    
if __name__ == '__main__':
    n = int(input("Enter the number of terms: "))
    print("The sum of the series is:", find_sum(n))