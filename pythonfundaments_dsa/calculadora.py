#!/usr/bin/env python
# coding: utf-8

# # Calculadora em Python

# In[10]:


from platform import python_version


# In[56]:


def soma(a,b):
    print ("\n%r + %r = " %(a,b), a+b)
    return 

def sub(a,b):
    print ("\n%r - %r = " %(a,b), a-b)
    return 

def mult(a,b):
    print ("\n%r x %r = " %(a,b), a*b)
    return 

def div(a,b):
    print ("\n%r : %r = " %(a,b), a/b)
    return  


# In[61]:


print("Operações")
print("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")


# In[ ]:


pergunta = 0
while pergunta == 0:
    
    op = int(input("\nDigite sua operação(1/2/3/4): "))
    while op != 1 and op != 2 and op != 3 and op != 4:
        op = int(input("\nOpção inválida. Digite outra(1/2/3/4): "))
        
    primeiro = float(input("\nDigite o primeiro número: "))
    segundo = float(input("\nDigite o segundo número: "))

    if op == 1:
        soma(primeiro, segundo)

    elif op == 2:
        sub(primeiro,segundo)

    elif op == 3:
        mult(primeiro,segundo) 

    elif op == 4:
        while segundo == 0 :
            segundo = float(input("\nNúmero inválido para divisão. Digite outro número: ")) 
        div(primeiro, segundo)


# In[ ]:




