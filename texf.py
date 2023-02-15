global var
var = {'null': 'null'}

def run(cmd: str, spliter=' *', errmsg=False):
  arg = cmd.split(spliter)
  try:
    if arg[0] == 'pt':
      print(arg[1])
    if arg[0] == 'pv':
      print(var[arg[1]])
    elif arg[0] == 'vs':
      var[str(arg[1])] = str(arg[2])
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

def exe(filepath: str, spliter=' *', errmsg=False):
  getfile = open(filepath, 'r')
  for line in getfile:
    run(line, spliter, errmsg)
  getfile.close()
