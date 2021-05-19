def mypoint(str1, num1):
    result1 = "My name is %-10s, point is %5d." %(str1, num1)
    print(result1)

def tryal(alpha,beta):
    result2 = ("名前は{myname}です。年齢は{myold}歳です。" .format(myname = alpha, myold = beta))
    print(result2)

tryal("Yamada", 20)
