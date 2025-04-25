'''
CREADOR -> Adria Gracia Sabate
VERSIO --> V1.0
DATA ----> 24/4/2025

jo no dono 0,30€ per a que tu et compris una 0,0 =)

->->->->JUSTIFICACIO DEL CODI CREAT-<-<-<-<-
aquestr codi el que fa es que a partir d'un preu d'algun producte, et mostra el preu original mes l'IVA inclos
'''
IVA=21

preu_inicial=int(input())
preu_final= preu_inicial + preu_inicial * IVA / 100

print("el preu inicial es:",preu_inicial,"pero el preu amb IVA es:",preu_final)