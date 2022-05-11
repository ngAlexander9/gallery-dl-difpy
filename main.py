import os
import sys
import json
import subprocess
from difPy import dif

def getconfig():
  try:
    configfile = open('config.json')
  except:
    print("config.json not found")
    sys.exit()
  configdata = json.load(configfile)
  return configdata

def getdirs(gallery_path, dirs):
  for file in os.listdir(gallery_path):
    dir_path = os.path.join(gallery_path, file)
    if os.path.isdir(dir_path):
      dirs.append(dir_path)
      print(dir_path)
      getdirs(dir_path, dirs)

def main():
  configdata = getconfig()
  parent_path = configdata['gallery-dl-parent-path']
  gallery_path = parent_path + '/gallery-dl'
  archive_file = configdata['archivefile']
  url_file = configdata['urlfile']

  cmd = ['gallery-dl', '-T', '5', '-i', url_file, '--download-archive', archive_file]
  subprocess.run(cmd, cwd=parent_path, shell=True)
  
  dirs = []
  getdirs(gallery_path, dirs)
  for dir in dirs:
    search = dif(dir, delete=True, silent_del=True)
    

if __name__ == "__main__":
  main()