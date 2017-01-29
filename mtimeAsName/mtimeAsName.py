#!/bin/env python

import sys
import os
from datetime import datetime

def usage():
  print ""
  print "Usage: "+sys.argv[0]+" <dir or file>"
  print ""
  sys.exit(1)

def parseArgs(args):
  if len(sys.argv) != 2 :
    usage()

  fileOrDir=os.path.abspath(sys.argv[1])
  if not os.path.exists(fileOrDir):
    print "Error: "+fileOrDir+" does not exist"
    sys.exit(1)

  return fileOrDir

def updateFile(file):
  mtime = os.path.getmtime(file)
  mtime = datetime.fromtimestamp(mtime)
  name = mtime.strftime("%Y%m%d_%H%M%S")
  ext = file.split(".").pop().lower()
  filename = name + "." + ext
  filename = os.path.join(os.path.dirname(file), filename)
  os.rename(file, filename)
  print file + " -> " + filename

def updateFiles(fileOrDir):
  if os.path.isfile(fileOrDir):
    updateFile(fileOrDir)
  else :
    for f in os.listdir(fileOrDir):
      updateFiles(os.path.join(fileOrDir,f))

if __name__ == "__main__":
  fileOrDir = parseArgs(sys.argv)
  updateFiles(fileOrDir)
  sys.exit(0)

