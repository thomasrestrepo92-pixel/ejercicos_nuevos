menu={
    "sancocho": 18.000,
    "bandeja paisa": 12.000,
    "sudado": 15.000

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