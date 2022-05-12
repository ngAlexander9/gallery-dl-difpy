import os
import sys
import json
import subprocess
from difPy import dif
import argparse

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
  # Set up parser
  parser = argparse.ArgumentParser()
  single_action_group = parser.add_mutually_exclusive_group()
  single_action_group.add_argument("-d", "--download-only", help = "only download (gallery-dl)", action="store_true")
  single_action_group.add_argument("-c", "--cull-only", help="only cull (difpy)", action="store_true")
  args = parser.parse_args()

  configdata = getconfig()
  parent_path = configdata['gallery-dl-parent-path']
  gallery_path = parent_path + '/gallery-dl'
  archive_file = configdata['archivefile']
  url_file = configdata['urlfile']
  
  if not args.cull_only:
    # gallery-dl to download from urls
    print("Downloading from list")
    pass
    cmd = ['gallery-dl', '-T', '5', '-i', url_file, '--download-archive', archive_file]
    subprocess.run(cmd, cwd=parent_path, shell=True)

  if not args.download_only:
    # difpy to delete duplicate images
    print("Deleting duplicate files")
    pass
    dirs = []
    getdirs(gallery_path, dirs)
    for dir in dirs:
      search = dif(dir, delete=True, silent_del=True)
  
  
    

if __name__ == "__main__":
  main()