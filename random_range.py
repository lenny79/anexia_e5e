from random import randrange

def rndrange(event, context):
  rnd_num = 0
  par = event['params']
  
  try:
    a, b = int(event['params']['a']), int(event['params']['b'])
    rnd_num = randrange(a, b)
  
  except Exception:
    a, b = 0, 0
      
  returnstr = "Output: " + str(rnd_num) + " / First Argument: " + str(event) + " / Second Argument: " + str(context) + " / a: " + str(a) + " / b: " + str(b) + " / params: " + str(par)
  return returnstr
