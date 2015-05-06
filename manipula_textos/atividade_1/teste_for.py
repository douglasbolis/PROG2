__author__ = 'douglas'

def main():
    vet = ["a", "ac", "ab"]
    vet.sort()
    vet2 = range(len(vet), -1)

    for i in range(len(vet), 0):
        print(vet[i])
    #fim for
    print(vet2)
#fim main

main()