'''
CREADOR -> Adria Gracia Sabate
VERSIO --> V1.0
DATA ----> 25/4/2025

jo no dono 0,30€ per a que tu et compris una 0,0 =)

->->->->JUSTIFICACIO DEL CODI CREAT-<-<-<-<-
aquest codi mesura les hores i els minuts a partir dels minuts introduits
'''
import math
minuts_a=int(input('introdueix un valor en minuts: '))
hores=math.trunc(minuts_a / 60)
minuts_b=minuts_a % 60

print('serien',hores,'hores','i',minuts_b,'minuts')