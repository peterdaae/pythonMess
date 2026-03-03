class PrimeChecker:

    n = int(input("Write a number: "))


    if n <= 1:
        print("Not prime (numbers <= 1 are not prime)")
    elif n == 2:
        print("Prime (2 is the smallest prime number)")
    else:

        is_prime = True


        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime")
        else:
            print("Not prime")


