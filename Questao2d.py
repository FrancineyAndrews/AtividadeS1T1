def main():
    #Entrada de dados
    h = int(input())
    m = int(input())
    s = int(input())
    
    #Processamento chamando a função
    r = segundos_desde_meia_noite(h, m, s)

    #Saída de dados
    print(f'{r}')

if __name__ == '__main__':
    main()
