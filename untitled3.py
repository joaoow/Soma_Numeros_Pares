# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fA2N9IdURNMAYUNVQ1iTtEh96ifcPVCX
"""

lista = [10, 2, 5, 7, 6, 3]
n=len(lista) #len trás o comprimento que está dentro da lista ex:6 elementos o n é igual a 6 (n=6)
soma=0
for i in range(n): #gera um intervalo de 0 a 5
 if(lista[i]%2==0):
  soma=soma+lista[i]
  print(f'O somatorio dos elementos pares da lista é: {soma}')


  #OU

lista = [10, 2, 5, 7, 6, 3]
soma=0
for num in lista:
 if(num%2==0):
  soma=soma+num
print(f'O somatorio dos elementos pares da lista é: {soma}')