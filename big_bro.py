'''
CREADOR -> Adria Gracia Sabate
VERSIO --> V1.0
DATA ----> 25/4/2025

jo no dono 0,30€ per a que tu et compris una 0,0 =)

->->->->JUSTIFICACIO DEL CODI CREAT-<-<-<-<-
aquest codi decideix qui es mes gran a partir d'una edat donada
'''
edat_primer=int(input('introdueix la edat de la primera prsona: '))
edat_segon=int(input('introdueix la edat de la segona prsona: '))

if edat_primer > edat_segon :
    print("l'edat de la primera persona amb",edat_primer,'anys es el mes gran dels dos')
else :
    print("l'edat de la segona persona amb",edat_segon,'anys es el mes gran dels dos')