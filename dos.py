import simpy 
import random
#new numero entre 0-10
#ready numero entre 1-10
#running 3 instrucciones
#


def ram(proceso,env):
    while True:
        proceso_duracion = random.randint(1,6)
        print(proceso,'comienza el primer proceso de la ram en %d' % env.now,'tiempo que dura este proceso',proceso_duracion)
        yield env.timeout(proceso_duracion)

        segundo_proceso = random.randint(1,6)
        print (proceso,'Comienza el segundo proceso de la ram %d' % env.now,'tiempo que dura el segundo proceso', proceso_duracion)
        yield env.timeout(segundo_proceso)

#ambiente de simuación, que en este caso será la ram

env = simpy.Environment()

env.process(ram('1',env))
env.process(ram('2',env))
env.run(until=25) #correr procesos hasta 25, luego correr con 50,100,150 y 200
