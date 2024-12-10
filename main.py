def desenhar_triangulo(tamanho):
    for i in range(tamanho):
        espacos = ' ' * (tamanho - i - 1)
        asteriscos = '*' * (2 * i + 1)
        print(espacos + asteriscos)

def desenhar_quadrado(tamanho):
    for _ in range(tamanho):
        print('*' * tamanho)

def desenhar_losango(tamanho):
    for i in range(tamanho):
        espacos = ' ' * (tamanho - i - 1)
        asteriscos = '*' * (2 * i + 1)
        print(espacos + asteriscos)
    for i in range(tamanho - 2, -1, -1):
        espacos = ' ' * (tamanho - i - 1)
        asteriscos = '*' * (2 * i + 1)
        print(espacos + asteriscos)

def main():
    print("Escolha um padrão para desenhar:")
    print("1 - Triângulo")
    print("2 - Quadrado")
    print("3 - Losango")

    try:
        escolha = int(input("Digite o número correspondente à sua escolha: "))
        tamanho = int(input("Digite o tamanho do padrão (um número inteiro positivo): "))

        if tamanho <= 0:
            print("Por favor, insira um número positivo para o tamanho.")
            return

        if escolha == 1:
            desenhar_triangulo(tamanho)
        elif escolha == 2:
            desenhar_quadrado(tamanho)
        elif escolha == 3:
            desenhar_losango(tamanho)
        else:
            print("Opção inválida. Por favor, escolha entre 1, 2 e 3.")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    main()
