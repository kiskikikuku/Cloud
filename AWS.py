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

def availableZones():
    response = ec2.describe_availability_zones()
    zones = [zone['ZoneName'] for zone in response['AvailabilityZones']]
    print("Available zones: ", zones)

def availableRegions():
    response = ec2.describe_regions()
    regions = [region['RegionName'] for region in response['Regions']]
    print("Available regions: ", regions)

def startInstance():
    id = input("Enter the Instance ID: ")
    ec2.start_instances(InstanceIds=[id])
    print(f"Starting {id}")

def stopInstance():
    id = input("Enter the Instance ID: ")
    ec2.stop_instances(InstanceIds=[id])
    print(f"Stopping {id}")

def createInstance():
    # 필요한 매개변수 설정
    ami_id = 'ami-0c55b159cbfafe1f0'  # Amazon Linux 2 AMI ID (예시)
    instance_type = 't2.micro'
    min_count = 1
    max_count = 1

    # 인스턴스 생성
    response = ec2.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=min_count,
        MaxCount=max_count,
        KeyName='cloud-test2'
    )

    # 생성된 인스턴스 ID 출력
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} created successfully.")

def rebootInstance():
    id = input("Enter the Instance ID: ")
    ec2.reboot_instances(InstanceIds=[id])
    print(f"Rebooting {id}")

def listImages():
    response = ec2.describe_images(Owners=['self'])
    images = [image['ImageId'] for image in response['Images']]
    print('Available images: ', images)

def main():
    while True:
        print("------------------------------------------------------------")
        print("1. list instance 2. available zones")
        print("3. start instance 4. available regions")
        print("5. stop instance 6. create instance")
        print("7. reboot instance 8. list images")
        print("99. quit")
        print("------------------------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            instancesList()
        elif choice == '2':
            availableZones()
        elif choice == '3':
            startInstance()
        elif choice == '4':
            availableRegions()
        elif choice == '5':
            stopInstance()
        elif choice == '6':
            createInstance()
        elif choice == '7':
            rebootInstance()
        elif choice == '8':
            listImages()
        elif choice == '99':
            print("Quiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()