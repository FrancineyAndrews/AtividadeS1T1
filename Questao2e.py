def area_piso(largura, comprimento):
    return largura * comprimento

def volume_sala(largura, comprimento, altura):
    return largura * comprimento * altura

def area_paredes(altura, largura, comprimento):
    return (2 * altura * largura) + (2 * altura * comprimento)

def main():
    #Entrada de dados
    a = float(input('Digite a altura da parede: '))
    c = float(input('Digite o comprimento da parede: '))
    l = float(input('Digite a largura da parede: '))
    
    #Processamento chamando a função
    piso = area_piso(l, c)
    sala = volume_sala(a, c, l)
    paredes = area_paredes(a, l, c)

    #Saída de dados
    print(f'Área do piso da sala: {piso:0.2f}')
    print(f'Volume da sala: {sala:0.2f}')
    print(f'Área das paredes da sala: {paredes:0.2f}')


if __name__ == '__main__':
    main()
