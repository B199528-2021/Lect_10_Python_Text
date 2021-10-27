#!/usr/local/bin/python3

my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
site = "GAATTC"
print("Lengths of",site,"cleaved fragments are",my_dna.find(site) + 1,"and",len(my_dna) -(my_dna.find(site)+1),"bases")
