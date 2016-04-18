from partida import Partida
from jugador import Jugador
p1=Partida("david",1)
print(p1.name)
j1=Jugador(1,"david")
j2=Jugador(2,"hola")
p1.addJugador(j1)
print(p1.jugadores[0].name)