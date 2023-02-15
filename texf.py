global var1
global var2
global var3

def run(cmd: str, spliter=' *', errmsg=True):
  arg = cmd.split(spliter)
  try:
    if arg[0] == 'pv':
      if arg[1] == 'v1':
        print(var1)
      elif arg[1] == 'v2':
        print(var2)
      elif arg[1] == 'v3':
        print(var3)
      else:
        print('no variable found')
    elif arg[1] == 'sv':
      if arg[0] == 'v1':
        var1 = arg[2]
      elif arg[0] == 'v2':
        var2 = arg[2]
      elif arg[0] == 'v3':
        var3 = arg[2]
      else:
        print('no variable found')
    else:
      if errmsg:
        print('command error')
      else:
        pass
  except:
    if errmsg:
      print('syntax error')
    else:
      pass

def exe(filepath: str, spliter=' *', errmsg=True):
  getfile = open(filepath, 'r')
  for line in getfile:
    run(line, spliter, errmsg)
  getfile.close()
