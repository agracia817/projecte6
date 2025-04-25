'''
CREADOR -> Adria Gracia Sabate
VERSIO --> V1.0
DATA ----> 25/4/2025

jo no dono 0,30€ per a que tu et compris una 0,0 =)

->->->->JUSTIFICACIO DEL CODI CREAT-<-<-<-<-
aquest codi mesura la velocitat a partir de la distancia i el temps donats
'''
km=float(input('introdueix un valor en quilometres: '))
h=int(input('introdueix un enter en hores: '))

velocitat=km/h

if velocitat < 180 :
    print('has anat a',velocitat,'km/h,','ni the grefg va tant lent')
else :
    print('felicitats, has anat a',velocitat,"km/h, t'has guanyat una galleta")