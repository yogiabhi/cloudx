#!/usr/bin/python2
import time


print "welcome to the adhoc cloud service"
print "##################################"
print "###                             ##"
print "###       adhoc cloud           ##"
print "###                             ##"
print "###             ###             ##"
print "##################################"
time.sleep (1)
c_user=raw_input("enter cloud credentials :  ")
c_password=raw_input("enter cloud Password :  ")
if         c_user == 'root'and c_password == '123123':
           print"please wait for adhoc cloud service"


           execfile('menu.py')
else:
 print "enter valid credential"
