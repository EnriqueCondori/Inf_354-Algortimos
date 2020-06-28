# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:51:01 2020

@author: WIN
"""
#una opcion para que no exista repetidos dentro de nuestra
#poblacion podemos hacer uso de:
#x=[random.sample(range(10),10)for i in range(10)] 
import random
modeloVector=[9,9,9,9,9,9,9,9,9,9]
largoIndividuo=10

num=10#cantidad de individuos
generaciones=5 #Generaciones
seleccion_individuos=2 #individuos>2
mutacion_probabilidad=0.2#0.2

def individuo(min,max):
    return[random.randint(min, max) for i in range(largoIndividuo)]

def newpoblacion():
    return[individuo(0, 9)for i in range(num)]

#Funcion en la que se debe cambiar en funcion a f(x)
def funcion_objetivo(individuo):
    aptitud=0#peso
    for i in range(len(individuo)):        
        if individuo[i]==modeloVector[i]:
            aptitud +=1
    return aptitud

def seleccion_y_reproduccion(poblacion):
    evaluacion=[(funcion_objetivo(i),i) for i in poblacion]
    #print("eval",evaluacion)
    #ordena la evaluacion, por cuantos 9 tiene el individuo
    evaluacion=[i[1]for i in sorted(evaluacion)]
    #print("eval",evaluacion)
    poblacion=evaluacion
    #print("tam",len(evaluacion)-seleccion_individuos)
    selected=evaluacion[(len(evaluacion)-seleccion_individuos):]
    #print("SE",selected)
    #print("pobla",poblacion)
    # #punto de cambio estatico para todos como pude ser random para cada uno
    puntoCambio=random.randint(1, largoIndividuo-1)
    #print(puntoCambio)
    #print("Evaluacion: ",evaluacion)
    for i in range(len(poblacion)-seleccion_individuos):
            #puntoCambio=random.randint(1, largoIndividuo-1)
            padre=random.sample(selected, 2)
            #print("padre",padre)
            poblacion[i][:puntoCambio]=padre[0][:puntoCambio]
            poblacion[i][puntoCambio:]=padre[1][puntoCambio:]
    #print("aca",poblacion)
    return poblacion
    
    

    
def mutacion(poblacion):
    for i in range(len(poblacion)-seleccion_individuos):
        if random.random()<=mutacion_probabilidad:
            puntoCambio=random.randint(1, largoIndividuo-1)
            nuevo_valor=random.randint(0, 9)
            while nuevo_valor == poblacion[i][puntoCambio]:
                nuevo_valor=random.randint(0, 9)
                #print("Cambio :",puntoCambio,"Nuevo Valor :",nuevo_valor)
                #print("Inicial",poblacion[i][puntoCambio])
            poblacion[i][puntoCambio]=nuevo_valor
            #print("Final",poblacion[i])
            
    return poblacion


#Principal
poblacion=newpoblacion()

while generaciones!=0:
    print("\nPoblacion Inicial:\n%s"%(poblacion))
    poblacion=seleccion_y_reproduccion(poblacion)
    print("\nSeleccion :\n%s"%(poblacion))
    poblacion=mutacion(poblacion)
    print("\nMutacion :\n%s"%(poblacion))
    generaciones=generaciones-1
