# Programa Estatística de Disciplinas - Python
import os
 
# Declaração de Variáveis
resp = 'S'
op = 0 #responsável por armazenar a opção do menu
tot_calc = 0 #totaliza o número de alunos que escolheram a disciplina de Cálculo de uma Variável
tot_base = 0  #totaliza o número de alunos que escolheram a disciplina de Bases de Programação
tot_mode = 0 #totaliza o número de alunos que escolheram a disciplina de Modelagem de Novos Negócios
tot_para = 0 #totaliza o número de alunos que escolheram a disciplina de Paradigmas de Linguagens de Programação
tot_alunos = 0 #totaliza o número total de alunos
med = 0 #armazena a média do aluno
med_calc = 0 #armazena a soma das médias dos alunos que escolheram Cálculo de uma Variável
med_base = 0 #armazena a soma das médias dos alunos que escolheram Bases de Programação
med_mode = 0 #armazena a soma das médias dos alunos que escolheram Modelagem de Novos Negócios
med_para = 0 #armazena a soma das médias dos alunos que escolheram Paradigmas de Linguagens de Programação
# Programa Principal
while resp == 'S' or resp == 's':
    os.system('CLS') # para linux, utilizar os.system('CLEAR')
 
    tot_alunos = tot_alunos+1 #Incrementa o total de alunos a cada nova entrada de dados
 
    # Menu de Opções
    print("""
    Escolha a sua Disciplina
   
    [1] Cálculo de uma Variável
    [2] Bases de Programação
    [3] Modelagem de Novos Negócios
    [4] Paradigmas de Linguagens de Programação
   
    """)
    op = int(input('Qual sua opção?'))
    med = float(input("Qual foi a sua média? "))
 
    # Verifica a opção da linguagem
    if op == 1:
        tot_calc = tot_calc+1
        med_calc = med_calc+med
    elif op == 2:
        tot_base = tot_base+1
        med_base = med_base+med
    elif op == 3:
        tot_mode = tot_mode+1
        med_mode = med_mode+med
    elif op == 4:
        tot_para = tot_para+1
        med_para = med_para+med
    else:
        print('Escolha inválida!')
    # Verifica se tem novo alunos
    resp = str(input('Outro aluno (S/N) ?'))
 
# Mostra resultados
os.system('CLS')
 
print('* * *  RELATÓRIO DA PESQUISA  * * *')
 
print(f'\nTotal de alunos que escolheram Cálculo de uma Variável                 ... {tot_calc}')
print(f'\nTotal de alunos que escolheram Bases de Programação                    ... {tot_base}')
print(f'\nTotal de alunos que escolheram Modelagem de Novos Negócios             ... {tot_mode}')
print(f'\nTotal de alunos que escolheram Paradigmas de Linguagens de Programação ... {tot_para}')
 
print(f'\nMédia aritmética das médias de Cálculo de uma Variável        ... {(med_calc/tot_calc) if tot_calc > 0 else 0}')
print(f'\nMédia aritmética das médias de Bases de Programação          ... {(med_base/tot_base) if tot_base > 0 else 0}')
print(f'\nMédia aritmética das médias de Modelagem de Novos Negócios  ... {(med_mode/tot_mode) if tot_mode > 0 else 0}')
print(f'\nMédia aritmética das médias de Paradigmas de Linguagens de Programação ... {(med_para/tot_para) if tot_para > 0 else 0}')
print(f'\nTotal de aluos ..................... {tot_alunos}')
 
if tot_calc>tot_base and tot_calc>tot_mode and tot_calc>tot_para:
    print("\nDisciplina de maior adesão foi Cálculo de uma Variável") 
elif tot_base>tot_calc and tot_base>tot_mode and tot_base>tot_para:
    print("\nDisciplina com maior adesão foi Bases de Programação")
elif tot_mode>tot_calc and tot_mode>tot_base and tot_mode>tot_para:
    print("\nDisciplina com maior adesão foi Modelagem de Novos Negócios")
else:
    print("\nDisciplina com maior adesão foi Paradigmas de Linguagens de Programação")
 
os.system('PAUSE')