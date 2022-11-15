from random import randrange

def rollD6(event, context):
  rnd_d6 = randrange(1, 7)
  return rnd_d6

def rolld20(event, context):
  rnd_d20 = randrange(1,21)
  return rnd_d20
