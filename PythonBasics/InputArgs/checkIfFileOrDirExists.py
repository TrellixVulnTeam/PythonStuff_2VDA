
#https://www.guru99.com/python-check-if-file-exists.html
import os.path
from os import path

def main():

   print ("file exists:"+str(path.exists('guru99.txt')))
   print ("File exists:" + str(path.exists('career.guru99.txt')))
   print ("directory exists:" + str(path.exists('myDirectory')))

   print ("file versionCheck3.py exists:"+str(path.exists('versionCheck3.py')))
   #print ("File exists:" + str(path.exists('career.guru99.txt')))
   print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/PythonStuff/')))
   print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/Pytho/')))
   print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/PythonStuff/PythonBasics/InputArgs/commandLineArgs1.py')))
   print ("directory exists:" + str(path.exists('/Users/kpadhikari/GitProj/KPAdhikari/PythonStuff/PythonBasics/InputArgs')))

if __name__== "__main__":
   main()
