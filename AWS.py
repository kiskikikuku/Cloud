import boto3
import csv
import subprocess

aws_acc_key = ''
aws_scr_key = ''

with open('rootkey.csv', 'r') as file:
    lines = file.readlines()
    keys = lines[1].strip().split(',')  # 두 번째 줄을 읽고 ','로 분리

    if len(keys) == 2:
        aws_acc_key, aws_scr_key = keys

aws_region = 'ap-northeast-2' # 구역 선택
ec2 = boto3.client('ec2', aws_access_key_id=aws_acc_key, aws_secret_access_key=aws_scr_key, region_name=aws_region)

def instancesList():
    response = ec2.describe_instances()
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    print("Instanace lists:", instances)
