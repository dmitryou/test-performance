#!/bin/python


import config
import sys
import time


class PerformanceChecker:
   def __init__(self, config):
       self.config = config

   def fillFile(self):
       start = time.time()
       counter = 0
       linesToFill = 10000000
       newLine = '- This is line number \n'
       data = []
       while(counter < linesToFill):
           counter = counter + 1
           data.append(str(counter) + newLine)
       print(config.FILENAME)
       print(len(data))
       with open(config.FILENAME,'w') as file:
           try:
               file.writelines(data)
               print "Filled file: " + config.FILENAME
               file.close()
           except:
               print "Error detected!"
               file.close()
       end = time.time()
       print('Test time :' + str(end-start))

def main():
    checker = PerformanceChecker(config)
    checker.fillFile()

if __name__ == "__main__":
    main()