import raas.py
from raas.py import *
import raas.py
from raas.py import *


dict1={}
for k,v in shakhs.dic.items():
    if(v.mahalekar == "بنادر" or v.mahalekar == "گمرک"):
        u=[]
        u.append(k)
        dict1[k]=u

 
for k in family.dic.keys():
    li=k.split("+")
    for i in dict1.keys():
        if(li[0]==i):
            dict1[i].append(li[1])

list1=[]
for v in malekiat.dic.values():
    for i in dict1.keys():
        if(dict1[i]==v):
            list1.append(v)


