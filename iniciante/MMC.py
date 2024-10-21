def calcular_mmc(a,b):
    # função calcula o MDC
    def calcular_mdc(x,y):
        while y: 
            x, y = y, x % y 
            return x

        # Formula do MMC: mmc(a,b)=(a*b)/mdc(a,b)
        mdc = calcular_mdc(a,b)
        mmc = (a*b)//mdc
        return mmc

    # Entrada do usuário
    num1 = int(input("digite o primeiro número:"))
    num2 = int(input("digite o segundo número:"))

    # Calculo de exibição do MMC
    resultado = calcular_mmc(num1, num2)
    print (f"O MMc de {num1} e {num2} é: {resultado}")