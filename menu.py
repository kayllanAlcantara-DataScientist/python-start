def questao1():
    numero_secreto = 37
    tentativas = 5
    for i in range(tentativas):
        chute = int(input(f"Tentativa {i+1}/{tentativas}: Digite um número de 1 a 100: "))
        if chute == numero_secreto:
            print("Parabéns, você acertou!")
            return
        elif chute < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")
    print(f"Você perdeu! O número era {numero_secreto}.")


def questao2():
    estoque = 50
    while True:
        print("\nControle de Estoque")
        print("1 - Vender Produto")
        print("2 - Comprar Produto")
        print("3 - Sair")
        opc = input("Escolha: ")
        if opc == "1":
            qtd = int(input("Quantidade para vender: "))
            if qtd < 1:
                print("A venda deve ser de pelo menos 1 produto.")
            elif qtd > estoque:
                print("Estoque insuficiente.")
            else:
                estoque -= qtd
                print(f"Venda realizada. Estoque atual: {estoque}")
        elif opc == "2":
            qtd = int(input("Quantidade para comprar: "))
            if qtd < 1:
                print("A compra deve ser de pelo menos 1 produto.")
            elif estoque + qtd > 100:
                print("Compra excede o limite de 100 produtos.")
            else:
                estoque += qtd
                print(f"Compra realizada. Estoque atual: {estoque}")
        elif opc == "3":
            print(f"Saindo... Estoque final: {estoque}")
            break
        else:
            print("Opção inválida.")


def questao3():
    x = int(input("Digite o valor limite X: "))
    soma = 0
    qtd = 0
    while soma <= x:
        n = int(input("Digite um número inteiro: "))
        soma += n
        qtd += 1
    print(f"Soma total: {soma} | Quantidade de números: {qtd}")


def questao4():
    votos = {"João": 0, "Maria": 0, "Nulo": 0, "Branco": 0}
    while True:
        print("\n1 - João | 2 - Maria | 3 - Nulo | 4 - Branco | 0 - Encerrar")
        op = input("Digite seu voto: ")
        if op == "1":
            votos["João"] += 1
        elif op == "2":
            votos["Maria"] += 1
        elif op == "3":
            votos["Nulo"] += 1
        elif op == "4":
            votos["Branco"] += 1
        elif op == "0":
            break
        else:
            print("Opção inválida.")
    total = sum(votos.values())
    print("\nResultado da votação:")
    for k, v in votos.items():
        perc = (v/total*100) if total > 0 else 0
        print(f"{k}: {v} votos ({perc:.2f}%)")


def questao5():
    ivo = 5000
    carla = 3000
    anos = 0
    while carla <= ivo:
        ivo *= 1.004
        carla *= 1.009
        anos += 1
    print(f"Em {anos} anos, Carla terá {int(carla)} habitantes e Ivo terá {int(ivo)} habitantes.")


def questao6():
    maior = 0
    menor = float("inf")
    total_res = total_com = total_ind = total_geral = 0
    cont = 0
    while True:
        opc = input("Deseja informar consumo? (s/n): ").lower()
        if opc != 's':
            break
        preco = float(input("Preço do kWh: "))
        qtd = float(input("Quantidade de kWh: "))
        tipo = input("Tipo (R=Residencial / C=Comercial / I=Industrial): ").upper()
        consumo = preco * qtd
        maior = max(maior, consumo)
        menor = min(menor, consumo)
        if tipo == "R":
            total_res += consumo
        elif tipo == "C":
            total_com += consumo
        elif tipo == "I":
            total_ind += consumo
        total_geral += consumo
        cont += 1
    media = total_geral / cont if cont > 0 else 0
    print(f"Maior: {maior:.2f} | Menor: {menor:.2f}")
    print(f"Total Residencial: {total_res:.2f}")
    print(f"Total Comercial: {total_com:.2f}")
    print(f"Total Industrial: {total_ind:.2f}")
    print(f"Média Geral: {media:.2f}")


def questao7():
    total = 0
    comp_idades = 0
    comp_qtd = 0
    fem_cursos = {}
    jovem_nome = ""
    jovem_idade = 999
    jovem_curso = ""
    cursos = {"Administração":0, "Computação":0, "Medicina":0, "Direito":0, "Jornalismo":0}
    apt_menor20 = 0
    while True:
        nome = input("Nome (ou FIM): ")
        if nome.upper() == "FIM":
            break
        idade = int(input("Idade: "))
        genero = input("Gênero (M/F): ").upper()
        curso = input("Curso: ").title()
        motivo = input("Motivo (remuneração/aptidão/outros): ").lower()
        total += 1
        if idade < 20 and motivo == "aptidão":
            apt_menor20 += 1
        if curso in cursos:
            cursos[curso] += 1
        if curso == "Computação":
            comp_idades += idade
            comp_qtd += 1
        if genero == "F":
            fem_cursos[curso] = fem_cursos.get(curso, 0) + 1
        if motivo == "remuneração" and idade < jovem_idade:
            jovem_nome, jovem_idade, jovem_curso = nome, idade, curso
    print(f"Alunos <20 com aptidão: {apt_menor20}")
    for c,v in cursos.items():
        perc = (v/total*100) if total>0 else 0
        print(f"{c}: {perc:.2f}%")
    media_comp = comp_idades/comp_qtd if comp_qtd>0 else 0
    print(f"Média de idade em Computação: {media_comp:.1f}")
    curso_fem_mais = max(fem_cursos, key=fem_cursos.get, default="Nenhum")
    print(f"Curso mais frequentado por mulheres: {curso_fem_mais}")
    if jovem_nome:
        print(f"Mais jovem por remuneração: {jovem_nome}, {jovem_idade} anos, {jovem_curso}")


# -------- MENU PRINCIPAL --------
while True:
    print("\n==============================")
    print("= 1 - Para Resolução da Questão 1 =")
    print("= 2 - Para Resolução da Questão 2 =")
    print("= 3 - Para Resolução da Questão 3 =")
    print("= 4 - Para Resolução da Questão 4 =")
    print("= 5 - Para Resolução da Questão 5 =")
    print("= 6 - Para Resolução da Questão 6 =")
    print("= 7 - Para Resolução da Questão 7 =")
    print("= 0 - Para SAIR do Sistema! ======")
    opcao = input("Escolha uma opção: ")
    if opcao == "1": questao1()
    elif opcao == "2": questao2()
    elif opcao == "3": questao3()
    elif opcao == "4": questao4()
    elif opcao == "5": questao5()
    elif opcao == "6": questao6()
    elif opcao == "7": questao7()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else: