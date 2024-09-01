def fibonacci(num):
    a, b = 0, 1
    if num == a or num == b:
        return True
    while b < num:
        a,b = b , a + b
        if b  == num:
            return True
    return False
    
numero = int(input("Digite um número inteiro :"))   

if fibonacci(numero):
    print("O número",numero,"pertence a sequência Fibonacci.")
else:
   print("O número",numero,"não pertence a sequência Fibonacci.")
