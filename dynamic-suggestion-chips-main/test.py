from flask import Flask,request
from pprint import pprint
from sentencesep import separator
from chipgenrator import chipgenerator

res=chipgenerator("paris")
print (res)
chip1,chip2,chip3=separator(res)
print(chip1,chip2)