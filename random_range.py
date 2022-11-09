from random import randrange

def rndrange(a, b):
  in_a = int(a)
  in_b = int(b)
  rnd_num = randrange(1, 7)
  returnstr = "Out: " + rnd_num + " // " + a + b
  return returnstr
