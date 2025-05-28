# função que irei utilizar para ver se a linguagem é regular ou não L = {a^n b^n | n >= 0}
def pertence_linguagem(w):
    n_a = 0  # Contador de 'a'
    n_b = 0  # Contador de 'b'
    fase_b = False  # Indica se já começou a ler 'b'

    for c in w:
        if c == 'a' and not fase_b:
            n_a += 1  # adiciona 1 à 'a'
        elif c == 'b':
            fase_b = True  # adiciona 1 à 'b'
            n_b += 1
        else:
            return False  # caso qualquer outro simbolo, falso

    
    return n_a == n_b and n_a > 0


# Função que aplica o lema do bombeamento
def aplicar_lema_bombeamento(w, p):
    print(f"Testando w = '{w}' com p = {p}")
    encontrou_quebra = False  # Flag para verificar se tem quebra do lema

    # Gera todas as divisões possíveis w = xyz, com restrições:
    # |xy| <= p e |y| > 0
    for i in range(1, p + 1):
        x = w[:i - 1]       #x: do início até posição i-1
        y = w[i - 1:i]      #y: apenas o caracter na posição i-1
        z = w[i:]           #z: do caracter i em diante

        print(f"\nDivisão: x='{x}' y='{y}' z='{z}'")

        # Testa diferentes repetições de y (i = 0, 1, 2, 3)
        for i_val in range(0, 4):
            w_bombeada = x + y * i_val + z  # Monta a nova string 'bombeada'
            resultado = pertence_linguagem(w_bombeada)  # Verifica se ainda pertence

            # nosso resultado do teste
            print(f"i={i_val}: '{w_bombeada}' -> {'Pertence' if resultado else 'Não pertence'}")

            # Se não pertence, houve quebra do lema
            if not resultado:
                encontrou_quebra = True

    # Resultado final do teste
    if encontrou_quebra:
        print("\n Quebra do lema encontrada. A linguagem NÃO é regular.")
    else:
        print("\n Nenhuma quebra encontrada. Isso não prova se a linguagem é ou não regular.")


p = 3  # Valor de bombeamento 
w = 'aaabbb'  # String que pertence à linguagem, com tamanho >= p

# Executa o teste do lema do bombeamento
aplicar_lema_bombeamento(w, p)