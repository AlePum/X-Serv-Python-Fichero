#!/usr/bin/python
# -*- coding: utf-8 -*-

fl = open("/etc/passwd" , "r")
lineas = fl.readlines()
for linea in lineas:
    print "->Username ", linea.split(':')[0], " ->Shell ", linea.split(':')[6]
print "Hay ", len(lineas), " usuarios"
