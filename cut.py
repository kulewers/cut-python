#!/usr/bin/env python3

import argparse
import sys

def main():
  parser = argparse.ArgumentParser(
    prog="cut",
    description="remove sections from each line of files"
  )
  parser.add_argument('infile', nargs='?', type=argparse.FileType("r"),
                      default=sys.stdin)
  parser.add_argument('-f', '--fields', type=str, nargs="+", required=True)
  parser.add_argument('-d', '--delimiter', default='\t', type=str)
  args = parser.parse_args()

  fieldNums = set() 
  for item in args.fields:
    if ',' in item:
      fieldNums |= set([int(n) for n in item.split(',')])
    elif ' ' in item:
      fieldNums |= set([int(n) for n in item.split(' ')])
    else:
      fieldNums |= int(item)
  
  for line in args.infile:
    matchOnLine = False
    line = line.rstrip('\n')
    fields = line.split(args.delimiter)
    if fields:
      for fieldN in sorted(list(fieldNums)):
        isLastField = sorted(list(fieldNums))[-1] == fieldN
        if len(fields) < fieldN:
          break
        if isLastField:
          print(fields[fieldN-1], end='')
        else:
          print(fields[fieldN-1], end=args.delimiter)
        matchOnLine = True
    if matchOnLine:
      print('\n', end='')



if __name__ == "__main__":
  main()