#!/usr/bin/python3
#
# Ilustra una implementación "sencilla" del Algoritmo del Banquero de Djikstra
# (simplificado a una única categoría de recursos)

procesos = ['A', 'B', 'C', 'D', 'E', 'F']
reclamo = {'A': 6,
           'B': 4,
           'C': 6,
           'D': 3,
           'E': 4,
           'F': 3
           }
asignado = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
# solicita = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

disponibles = 10
libres = 1

def banquero(quien, cuanto):
    # Asumiendo que, a partir de la situación actual, yo _otorgara_ la solicitud
    # de asignar "cuanto" a "quien", ¿es posible llegar a un _estado seguro_ que
    # permita que todos los procesos terminen, incluso si presentan su reclamo
    # máximo?
    maximo = reclamo[quien] - asignado[quien]
    print('== Partamos de que: ==')
    print('== Reclamo:  ', reclamo)
    print('== Asignado: ', asignado)
    print('%s solicita %d' % (quien, cuanto))

    if cuanto > maximo:
        print('¡Nanai! (%d > %d)' % (cuanto, maximo) )
        raise RuntimeError('Estaría pidiendo más allá de su reclamo')

    if cuanto > libres:
        raise RuntimeError('Se pasa a la sala de espera... (%d > %d)' %
                           (cuanto, libres))

    restantes = {}
    for p in procesos:
        restantes[p] = reclamo[p] - asignado[p]
    restantes[quien] -= cuanto

    while len(restantes.keys()) != 0:
        menor = encuentra_candidato(restantes)
        print('Mi candidato es "%s"  ' %
              (menor))
        print('Evaluando la situación restante: ', restantes)
        recursos = restantes[menor]
        if libres < recursos:
            raise RuntimeError('¡No quedan suficientes para que %s termine',
                               menor)
        del(restantes[menor])

    print('Llegamos a un estado seguro')
    return(True)

def encuentra_candidato(restantes):
    candidato = min(restantes, key=restantes.get)
    return(candidato)


## ↓ Lo siguiente sería el equivalente a un open('recurso') por parte de B
banquero('B', 1)
print('¡B es feliz!')
