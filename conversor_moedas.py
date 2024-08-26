import requests

def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    url= f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'
    resposta=requests.get(url)
    dados=resposta.json()
    return dados['rates'] [moeda_destino]

def converter_moeda (valor, moeda_origem, moeda_destino):
    taxa=obter_taxa_de_cambio(moeda_origem, moeda_destino)
    valor_convertido=valor*taxa
    return valor_convertido

def main():
    moeda_origem=input('Digite a moeda de origem (ex.:USD, EUR, BRL):').upper()
    moeda_destino=input('Digite a moeda de destino (ex.:USD, EUR, BRL):').upper()
    valor= float(input(f'Digite o valor em {moeda_origem}:'))
    
    valor_convertido=converter_moeda(valor, moeda_origem, moeda_destino)
    
    print(f'{valor} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}')
    
if __name__ == "__main__":
    main()