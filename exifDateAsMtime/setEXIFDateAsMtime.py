#!/bin/env python

import exifread
import sys
import os
import time
import datetime

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

def updateOnePhoto(file):
  try:
    with open(file, 'rb') as f:
      tags = exifread.process_file(f)
      photoDate = tags['EXIF DateTimeDigitized']
      mtime = time.mktime(datetime.datetime.strptime(str(photoDate), "%Y:%m:%d %H:%M:%S").timetuple())
      atime = os.path.getatime(file)
      os.utime(file, (atime, mtime))
  except:
    print file + ": problem while extracting EXIF information"

def updatePhotos(fileOrDir):
  if os.path.isfile(fileOrDir):
    updateOnePhoto(fileOrDir)
  else :
    for f in os.listdir(fileOrDir):
      updatePhotos(os.path.join(fileOrDir,f))

if __name__ == "__main__":
  fileOrDir = parseArgs(sys.argv)
  updatePhotos(fileOrDir)
  sys.exit(0)

