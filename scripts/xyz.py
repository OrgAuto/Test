import path
import sys
import boto3

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from env.properties import *

print ("val is " + val)
print ("Number is " , int(num))
