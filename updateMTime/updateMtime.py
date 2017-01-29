#!/bin/env python

import sys
import os
import operator

operators = { "+": operator.add, "-": operator.sub }

def usage():
  print ""
  print "Usage: "+sys.argv[0]+" <dir or file> <+|-><time delta>"
  print ""
  print "   time delta example: 1d15h3m6s"
  print "                              d : days, h : hours, m : minutes, s : seconds"
  print "                              each one is optional, but at least one has to be set"
  sys.exit(1)

def parseTimeDelta(arg):
  delta = 0
  tmpNb=""

  for c in arg:
    if c.isdigit():
      tmpNb += c
    else:
      if c == 'd':
        delta += 24 * 60 * 60 * int(tmpNb)
      elif c == 'h':
        delta += 3600 * int(tmpNb)
      elif c == 'm':
        delta += 60 * int(tmpNb)
      elif c == 's':
        delta += int(tmpNb)
      tmpNb=""
  
  return delta

def parseArgs(args):
  if len(sys.argv) != 3 :
    usage()

  fileOrDir=os.path.abspath(sys.argv[1])
  if not os.path.exists(fileOrDir):
    print "Error: "+fileOrDir+" does not exist"
    sys.exit(1)

  operator = args[2][0]
  if not operator in ['-', '+']:
    print "Error: time delta must be preceded by '-' or '+'"
    sys.exit(1)

  timeDelta = parseTimeDelta(args[2][1:])

  return (fileOrDir, operator, timeDelta)

def updateFileMTime(file, operator, timeDelta):
  mtime = os.path.getmtime(file)
  atime = os.path.getatime(file)
  newMtime = operators[operator](mtime,timeDelta)
  os.utime(file, (atime, newMtime))

def updateMTime(fileOrDir, operator, timeDelta):
  if os.path.isfile(fileOrDir):
    updateFileMTime(fileOrDir,operator,timeDelta)
  else :
    for f in os.listdir(fileOrDir):
      updateMTime(os.path.join(fileOrDir,f),operator,timeDelta)

if __name__ == "__main__":
  (fileOrDir, operator, timeDelta) = parseArgs(sys.argv)
  updateMTime(fileOrDir, operator, timeDelta)
  sys.exit(0)

