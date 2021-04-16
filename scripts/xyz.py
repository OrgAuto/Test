import path
import sys
import boto3
import re

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from env.properties import *
re.search("hello", "hello there")
print ("val is " + val)
print ("Number is " , int(num))
