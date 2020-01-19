import pandas as pd

class raas:

    def __init__(self,key = 0,inn = None, out = None):
        self.key = key
        self.inn = inn
        self.out = out


class hesabbanki(raas):

    dic={}
    def __init__(self,codemeli=0,namebank=0,shshaba=0,shhesab=0):
        super(hesabbanki,self).__init__(shshaba)
        self.codemeli=codemeli
        self.namebank=namebank
        self.shhesab=shhesab


class khane(raas):

    dic={}
    def __init__(self,codemeli=0,gheymat=0,codeposti=0,metraj=0,addres=0):
        super(khane,self).__init__(codeposti)
        self.codemeli=codemeli
        self.gheymat=gheymat
        self.metraj=metraj
        self.addres=addres


class mashin(raas):

    dic={}
    def __init__(self,pelak=0,codemeli=0,model=0,rang=0):
        super(mashin,self).__init__(pelak)
        self.codemeli=codemeli
        self.model=model
        self.rang=rang

class hamrah(raas):

    dic={}
    def __init__(self,codemeli=0,sim=0,operator=0):
        super(hamrah,self).__init__(sim)
        self.codemeli=codemeli
        self.operator=operator

class shakhs(raas):

    dic={}
    def __init__(self,name=0,familyname=0,codemeli=0,tarikhtavalod=0,mahaletavalod=0,mahalekar=0):
        super(shakhs,self).__init__(codemeli)
        self.name=name
        self.familyname=familyname
        self.tarikhtavalod=tarikhtavalod
        self.mahaletavalod=mahaletavalod
        self.mahalekar=mahalekar

 
hesabbanki_csv = pd.read_csv('accounts.csv')
hesabbanki_csv.columns = ['codemeli' , 'nemabank', 'shshaba' , 'shhesab']

mashin_csv = pd.read_csv('cars.csv')
mashin_csv.columns= ['model' ,'codemeli','pelak','rang']

khane_csv = pd.read_csv('homes.csv')
khane_csv.columns = ['codemeli', 'gheymat','codeposti','metraj','addres']

hamrah_csv = pd.read_csv('phones.csv')
hamrah_csv.columns = ['codemeli','sim','operator']

shakhs_csv = pd.read_csv('people.csv')
shakhs_csv.drop(columns= 'address',axis =1,inplace = True)  
shakhs_csv.columns = ['mahaletavalod','address','mahalekar','tarikhtavalod','codemeli','familyname','name']

for i in range(len(shakhs_csv)):
    shakhs.dic[shakhs_csv[i:i+1]['codemeli'].str.cat()] =shakhs(shakhs_csv[i,i+1]['name'].str.cat(),shakhs_csv[i,i+1]['familyname'].str.cat(),shakhs_csv[i,i+1]['tarikhtavalod'].str.cat(),shakhs_csv[i,i+1]['mahaletavalod'].str.cat(),shakhs_csv[i,i+1]['mahalekar'].str.cat())
for i in range(len(khane_csv)):
    khane.dic[khane_csv[i:i+1]['codeposti'].str.cat()] =khane(khane_csv[i:i+1]['codemeli'].str.cat(),(khane_csv[i:i+1]['gheymat'].str.cat(),khane_csv[i:i+1]['codeposti'].str.cat(),khane_csv[i:i+1]['matraj'].str.cat(),khane_csv[i,i+1]['addres'].str.cat())
for i in range(len(mashin_csv)):
    mashin.dic[mashin_csv[i:i+1]['pelak'].str.cat()] =mashin(mashin_csv[i,i+1]['pelak'].str.cat(),mashin_csv[i:i+1]['codemeli'].str.cat() , mashin_csv[i,i+1]['model'].str.cat() , mashin_csv[i,i+1]['rang'].str.cat())    
for i in range(len(hamrah_csv)):
    hamrah.dic[hamrah_csv[i:i+1]['sim'].str.cat()] =hamrah(hamrah_csv[i:i+1]['codemeli'].str.cat(),hamrah_csv[i:i+1]['sim'].str.cat(),hamrah_csv[i,i+1]['operator'].str.cat())   
for i in range(len(hesabbanki_csv)):
    hesabbanki.dic[hesabbanki_csv[i:i+1]['shshaba'].str.cat()] =hesabbanki(hesabbanki_csv[i:i+1]['codemeli'].str.cat() , hesabbanki_csv[i,i+1]['nemebank'].str.cat() , hesabbanki_csv[i:i+1]['shshaba'].str.cat() , hesabbanki_csv[i:i+1]['shhesab'].str.cat())

