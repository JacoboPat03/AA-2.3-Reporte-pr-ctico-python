jugadores = [
    {"nombre":"Brandon","edad":22},
    {"nombre":"Alana","edad":23},
    {"nombre":"Oso","edad":24},
    {"nombre":"Kafai","edad":25}

]

nombres_jugadores = list(map(lambda jugador: jugador["nombre"],jugadores))

print(nombres_jugadores)