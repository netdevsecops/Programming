# function(n,k)
# if n > 20 return 0
# eger n < 20 onda range (1,n) araliqda onlari 1^k stepeninda cixart ve totalini hesabla
# if n < 20 then use range from 1 to n and then range of them use in 1^k ve sum output of them


n = int(input("Enter first number: "))
k = int(input("Enter second number: "))


def function(n, k):
    if n > 20:
        return 0
    elif n < 20:
        sum = 0
        for e in range(1, n):
            print(e**k)
            sum += e**k
    print(sum)


function(n, k)
