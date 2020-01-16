"""
Project Euler: Problem 1: Multiples of 3 and 5

"""
def multiplesOf3and5(number):
    # create the list of multiple 3 and 5 for a specific number
    liste = []
    for i in range(1,number):
        if i%3 == 0 or i%5 == 0:
            liste.append(i)
    # sum of all numbers in the list
    somme = 0
    for i in liste:
        somme = somme + i

    print(" Sum of all the multiples of 3 or 5 for number ",number," is ", somme)

# test multiples of 3 or 5 for number 1000
multiplesOf3and5(1000)
