# -*- coding: utf-8 -*-

"""
import pickleshare

text_file= open("P:\Coursera\Complete-Python-Bootcamp-master\Final Capstone Projects\AnnaKarenina.txt","r")
lines = text_file.readlines()
print len(lines)

lines = lines[51:]

indices = [i for i, s in enumerate(lines) if 'Chapter' in s]


print 'Operations Completed'    


for i in range(238):
    starting = indices[i]
    ending = indices[i+1]
    chapter = lines[starting:ending]
    new_file = open(str(i)+'.txt', 'w')
    for item in chapter:
        new_file.write("%s\n" % item)

print("completed")
