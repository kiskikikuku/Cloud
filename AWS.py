import boto3
import os
import subprocess

with open('rootkey.csv', 'r') as file:
    lines = file.readlines()
    access_key = lines[0].strip()
    secret_key = lines[1].strip()


