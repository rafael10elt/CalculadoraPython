# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Calculadora em Python V2
print('\n*****************************Calculadora em Python V2*****************************\n')
def add(x,y):
  return x+y

def subtract(x,y):
  return x-y

def multiply(x,y):
  return x*y

def divide(x,y):
  return x/y

print("Selecione o número da operação desejada: ")
print("1- SOMA")
print("2- SUBTRAÇÃO")
print("3- MULTIPLICAÇÃO")
print("4- DIVISÃO")

option = input("\nDigite sua opção (1/2/3/4): ")

num1 = int (input ("Digite o primeiro número: "))
num2 = int (input ("Digite o segundo número: "))

if option == '1' :
   print(num1, "+" , num2, "=", add(num1,num2))
  
elif option == '2' :
   print(num1, "-" , num2, "=", subtract(num1,num2))
  
elif option == '3' :
 print(num1, "*" , num2, "=", multiply(num1,num2))
  
elif option == '4' :
   print(num1, "/" , num2, "=", divide(num1,num2))
  
else :
  print("Opção inválida!")

