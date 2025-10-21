menu={
    "sancocho": 15000,
    "bandeja paisa": 15000,
    "sudado": 15000

}

for clave, valor in menu.items():
    print(f"{clave}: {valor}")

total=0
platos =[]
while True:
    plato=input(" ingrese su plato: ")
    if plato.lower()== "pedir":
        break
    if plato in menu:
        total+= valor
    platos.append(plato)
    print("tus platos son :", platos , total)