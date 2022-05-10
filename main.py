import os
import sys
import json
import subprocess

def getconfig():
  try:
    configfile = open('config.json')
  except:
    print("config.json not found")
    sys.exit()
  configdata = json.load(configfile)
  return configdata

def main():
  configdata = getconfig()
  parent_path = configdata['gallery-dl-parent-path']
  archive_file = configdata['archivefile']
  url_file = configdata['urlfile']
  
  cmd = ['gallery-dl', '-T', '5', '-i', url_file, '--download-archive', archive_file]
  subprocess.run(cmd, cwd=parent_path, shell=True)

if __name__ == "__main__":
  main()