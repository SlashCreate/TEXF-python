def run(cmd: str, spliter=' *', errmsg=False):
  arg = cmd.split(spliter)
  if arg[0] == 'pt':
    print(arg[1])
  else:
    if errmsg:
      print('error')
    else:
      pass

def exe(filepath: str, spliter=' *', errmsg=False):
  getfile = open(filepath, 'r')
  for line in getfile:
    run(line, spliter, errmsg)
  getfile.close()
