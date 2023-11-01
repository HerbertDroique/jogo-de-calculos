#!/usr/bin/env python
# coding: utf-8

# # DESAFIO DE MATEMÁTICA BÁSICO
# 
# ## By Herbert Droique 
# 
# ### Consiste em um programa onde é sorteado uma operação matemática (multiplicação, divisão, adição, subtração), e tambem sorteia 2 números aleatórios entre 1 e 100.
# 
# #### O Usuário responde 10 questões e ao final o programa imprime se foi Aprovado ou Reprovado, tendo que ter uma média mínima de 6 pontos ou 60% para ser aprovado.   

# In[5]:


#Importando a função random para sortear ou núneros e as operações
import random

# importando a função para limpar a tela no windows e linux
from os import system, name


# In[6]:


#função para limpar a tela a cada execução
def limpaTela():
    
    #windows
    if name == 'nt':
        _ = ('cls')
        
    #MAC ou Linux
    else :
        _ = ('clear')


# In[9]:


#função game com os processos do jogo
def game():
    
    limpaTela()
    print("Bem Vindo(a) ao Jogo 'Cálculos Matemáticos'")
    print("\n Realize os 10 cáculos gerados pelo computador e receba o seu resultado no jogo ao final.\n Boa Sorte.")
    
    #Lista de Operações
    listaOperacoes = ['+','-','*','/']
    
   
    #Quantidade de Perguntas
    qtdPerguntas = 1
    
    #Respostas Erradas do Usuário
    respErrada = []
    
    while qtdPerguntas < 11:
        
        #Sorteando a Operação
        op = random.choice(listaOperacoes)
        
        #Lista com os números de 0 a 100
        n = range(1,100)
        
        n1 = random.choice(n)
        n2 = random.choice(n)
        
        
        
                
        qtdPerguntas +=1
        
        #Condicional de Acordo com a operação
        if op == '+':
            
            #Resultado Correto
            resMaquina = n1 + n2
            
            
            print("\n%d + %d" %(n1,n2))
            resposta = int(input("Qual o resultado da operação acima: "))
            
            
            
            if resposta == resMaquina:
                pass
                
            else:
                respErrada.append(resposta)
        
        if op == '-':
            
            #Resultado Correto
            resMaquina = n1 - n2
            
            
            print("\n%d - %d" %(n1,n2))
            resposta = int(input("Qual o resultado da operação acima: "))
            
            
            
            if resposta == resMaquina:
                pass
                
            else:
                respErrada.append(resposta)
                
        if op == '*':
            
            #Resultado Correto
            resMaquina = n1 * n2
            
            
            print("\n%d x %d" %(n1,n2))
            resposta = int(input("Qual o resultado da operação acima: "))
            
            
            
            if resposta == resMaquina:
                pass
                
            else:
                respErrada.append(resposta)
                
        if op == '/':
            
            #Resultado Correto
            resMaquina = n1 / n2
            
            
            print("\n%d / %d" %(n1,n2))
            resposta = int(input("Qual o resultado da operação acima: "))
            
            
            
            if resposta == resMaquina:
                pass
                
            else:
                respErrada.append(resposta)
                
        
    
    print("\nVocê errou:",len(respErrada), "resposta(s)")
    resultado = 'Você foi Aprovado(a)' if len(respErrada) <= 4 else 'Você foi Reprovado(a), Tente Novamente'
    print(resultado)
    
    
    

# Bloco main
  
if __name__ == "__main__":
    game()
    print("\nLIFELONG LEARNING :)\n")


# ## 
