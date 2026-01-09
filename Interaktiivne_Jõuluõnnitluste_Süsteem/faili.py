import glob
import os

f = open("data.txt","r")
print(dir(f))
f.close

def leia_projektifailid(laiend):
    if not laiend.startswith("."):
        laiend = "." + laiend
    return glob.glob(f"*{laiend}")
    
     







