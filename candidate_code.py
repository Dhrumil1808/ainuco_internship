from __future__ import print_function
import math

def diff_one_id(a, b):
    return id(b[0] - a[0])

def task_1():
    a = [10]
    b = a
    b[0] += 1
    
    return diff_one_id(a, b)

def ifprime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for i in range(2, (int) (math.sqrt(n)) + 1):
            if(n%i==0):
                return False
        return True


def main():
    result_1 = task_1()
    print("result 1: ", result_1)
    primes=[]
    reverse=[]
    prime_26=[]
    prime_97=[]
    ascii_values=[]
    string=""
    print("********************************************************************************")
    for i in range(1,101):
        prime=ifprime(i)
        if(prime):
            primes.append(i)     #stores the prime numbers between 1 and 100
            reverse.append(int(str(i)[::-1])) #prime number is reversed 

    print("primes between 1 and 100: ", primes)
    print("********************************************************************************")
    print("reversal of prime numbers", reverse)

    for i in range(0,len(reverse)):
        prime_26.append(reverse[i] % 26) #stores prime numbers remainder when divided by 26
        prime_97.append(reverse[i] % 26 + 97) # ascii values for the small letters
        ascii_values.append(str(unichr(reverse[i] % 26 + 97)))
    print("********************************************************************************")
    print("prime numbers modulo 26", prime_26)
    print("********************************************************************************")
    print("prime numbers modulo 26 plus 97", prime_97)
    print("********************************************************************************")
    print("ascii values of prime numbers between 1 and 100" , ascii_values)
    for i in range(0,len(ascii_values)):
        string += ascii_values[i]
    print("string =", string)    

if __name__ == '__main__':
    main()