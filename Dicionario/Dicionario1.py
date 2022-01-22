usuarios={}
usuarios={
    "Chaves": ["Chaves Silva", "17/06/1975","Recep_01"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_03"]
    
}
usuarios["Florinda"]=["Florinda Flores","26,11,2017","Recap_01"]
usuarios["Florinda"]=["Florinda Flores","26,11,2016","Recap_0"]

print(usuarios)
print("Dados:",usuarios.get("Chaves"))
print("Dados:",usuarios.get("Chapolin"))
print("Dados:",usuarios.get("Quico"))
print("Dados:",usuarios.get("Florinda"))