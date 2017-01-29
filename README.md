# photosTools

Scripts used to perform operations on the photo files (exif, name, mtime...)

## [exifDateAsMtime](exifDateAsMtime/setEXIFDateAsMtime.py)

Set the date where the photo was taken (in the EXIF data) as mtime of the photo file

```
Usage: ./setEXIFDateAsMtime.py <dir or file>
```

If the command is applied to a directory, the modification will occur on all the photos of the directory.

## [mtimeAsName](mtimeAsName/mtimeAsName.py)

Script used to rename a file by its mtime. Useful to sort files for examples.

```
Usage: ./mtimeAsName.py <dir or file>
```

The file is renamed with the following format : `%Y%m%d_%H%M%S.ex

## [updateMTime](updateMTime/updateMtime.py)

Script used to update the mtime of a file or all files recursively in a directory.

```
Usage: ./updateMtime.py <dir or file> <+|-><time delta>
```

Time delta example: 1d15h3m6s (d : days, h : hours, m : minutes, s : seconds). Each one is optional, but at least one has to be set.

