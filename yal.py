import pandas as pd
import raas.py
from raas.py import *



class yal:
    def __init__(self,key = 0,next = None, prev = None):
        self.key=key
        self.next= next
        self.prev=prev

class malekiat(yal):
    def __init__(self,sabteahval=0, tamalok=0, pardakhti=0, next=None, prev=None):
        super(malekiat,self).__init__(sabteahval,next,prev)
        self.tamalok=tamalok
        self.pardakhti=pardakhti
        
          
class tarakonesh(yal):
    def __init__(self,shomare=0, zaman=0, mablagh=0, next=None, prev=None):
        super(tarakonesh,self).__init__(shomare,next,prev)
        self.zaman=zaman
        self.mablagh=mablagh

class tamas(yal):
    def __init__(self,shomare=0,zaman=0,modat=0, next=None, prev=None):
        super(tamas,self).__init__(shomare,next,prev)
        self.zaman=zaman
        self.modat=modat

class family(yal):
    def __init__(self,tarkibi=0, nesbat=0, shoruenesbat=0, next=None, prev=None):
        super(family,self).__init__(tarkibi,next,prev)
        self.nesbat=nesbat
        self.shoruenesbat=shoruenesbat


tamsa_csv=pd.read_csv('calls.csv')
tamsa_csv.columns=['prev','next','shomare','zaman','modat']

malekiat_csv = pd.read_csv('ownerships.csv')
malekiat_csv.columns = ['prev','next','sabteahval','tamalok', 'pardakhti']

family_csv = pd.read_csv('relationships.csv')
family_csv.columns = ['prev','next','nesbat','shoruenesbat']

tarakonesh_csv = pd.read_csv('transactions.csv')
tarakonesh_csv.columns = ['prev','next','shomare','zaman','mablagh']

malekiat_list=[]
tarakonesh_list=[]
tamas_list=[]
family_list=[]

for i in range(len(tamsa_csv)):
    tamas_list[i]=tamas(int(tamsa_csv[i:i+1]['shomare']),tamas_csv[i,i+1]['zaman'].str.cat(),tamas_csv[i,i+1]['modat'].str.cat())
    for j in range(len(hamrah_list)):
        if(hamrah_list[j].key==int(tamsa_csv[i:i+1]['prev'])):
            tamas_list[i].prev=hamrah_list[j]
        else:
            print("Data Not Found !! ")    
    for j in range(len(hamrah_list))    
        if(hamrah_list[j].key==int(tamsa_csv[i:i+1]['next'])):
            tamas_list[i].next=hamrah_list[j]    
        else:
            print("Data Not Found !! ")        

for i in range(len(tarakonesh_csv)):
    tarakonesh_list[i]=tarakonesh(int(tarakonesh_csv[i:i+1]['shomare']),tarakonesh_csv[i,i+1]['zaman'].str.cat(),int(tarakonesh_csv[i:i+1]['mablagh']))
    for j in range(len(hesabbanki_list)):
        if(hesabbanki_list[j].shhesab==int(tarakonesh_csv[i:i+1]['prev'])):
            tarakonesh_list[i].prev=hesabbanki_list[j]
        else:
            print("Data Not Found !! ")
    for j in range(len(hesabbanki_list))        
        if(hesabbanki_list[j].shhesab==int(tarakonesh_csv[i:i+1]['next'])):
            tarakonesh_list[i].next=hesabbanki_list[j]    
        else:
            print("Data Not Found !! ")
            

for i in range(len(malekiat_csv)):
    malekiat_list[i]=malekiat(int(malekiat_csv[i:i+1]['sabteahval']),malekiat_csv[i,i+1]['tamalok'].str.cat(),int(malekiat_csv[i:i+1]['pardakhti']))
    for j in range(len(shakhs_list)):
        if(shakhs_list[j].key==int(malekiat_csv[i:i+1]['prev'])):
            malekiat_list[i].prev=shakhs_list[j]
        else:
            print("Data Not Found !! ")
    CHECK=0        
    for j in range(len(mashin_list))
        if(mashin_list[j].key==int(malekiat_csv[i:i+1]['next'])):
            malekiat_list[i].next=mashin_list[j]
            CHECK=1
    if(CHECK==0)        
    for j in range(len(khane_list))    
        if(khane_list[j].key==int(malekiat_csv[i:i+1]['next'])):
            malekiat_list[i].next=khane_list[j]    
    else:
        pass
    
for i in range(len(family_csv)):
    family_list[i]=family(family_csv[i,i+1]['prev'].str.cat()+family_csv[i,i+1]['next'].str.cat(),family_csv[i,i+1]['nesbat'].str.cat(),family_csv[i,i+1]['shoruenesbat'].str.cat(),)
    for j in range(len(shakhs_list)):
        if(shakhs_list[j].key==int(family_csv[i:i+1]['prev'])):
            family_list[i].prev=shakhs_list[j]
        else:
            print("Data Not Found !! ")
    for j in range(len(shakhs_list)):
        if(shakhs_list[j].key==int(family_csv[i:i+1]['next'])):            
            family_list[i].prev=shakhs_list[j]
        else:
            print("Data Not Found !! ")


