#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
 
  # Open and read the file.
  f = open(filename, 'r')
  text = f.read()

  # year data
  # \s matches whitespace
  #\d matches a digit equivalent to [0-9] 
  # groups are separated by () so in this case the only group would be the year
  found = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
  if not found:
    #No year, error message.
    print("No match for the year!")
    sys.exit()
  year = found.group(1) # .group() would return ('1990',)
  # returns the year
  data = []
  data.append(year)
  #print(f'Year: {year}')

  # groups are separated by ()
  #\d matches a digit equivalent to [0-9] 
  #\w matches any word character (equivalent to [a-zA-Z0-9_]
  # according to https://www.rexegg.com/regex-quickstart.html + adds one or more
  # initially I was going to use * but I don't want to accidentally add something that's empty
  rankAndNames = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  
  rNList = {} 
  for rank, boy, girl in rankAndNames:
    if boy not in rNList:
      rNList[boy] = rank
    if girl not in rNList:
      rNList[girl] = rank
 
  sortedRNList = sorted(rNList.keys())
  for i in sortedRNList:
    data.append(f"{i} {rNList[i]}")

  return data 


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
      data = extract_names(filename)
      data = "\n".join(data)
      if not summary:
        print(data) 
      else:
        w = open(filename + '.txt', 'w')
        w.write(data + '\n')
        w.close() 
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
