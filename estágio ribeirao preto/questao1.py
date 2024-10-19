def eh_fibonacci(numero):
    

    #início da sequência de Fibonacci
    a, b = 0, 1
    
    #continuamos calculando a sequência até que o valor 'b' ultrapasse ou seja igual ao número
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b

    return False


#digitar o número para ser verificado
numero = int(input("Informe um número: "))

#verificando
if eh_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
