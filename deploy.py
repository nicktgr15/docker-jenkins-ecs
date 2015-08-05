#!/usr/bin/python

from time import sleep
import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--service-name", dest='service_name', required=True)
args = parser.parse_args()

client = boto3.client('ecs', region_name='eu-west-1')

print("Setting desiredCount=0")
client.update_service(service=args.service_name, desiredCount=0)

while client.update_service(service=args.service_name)['service']['runningCount'] != 0:
    print("runningCount!=0, sleeping")
    sleep(5)

print("Setting desiredCount=1")
client.update_service(service=args.service_name, desiredCount=1)

while client.update_service(service=args.service_name)['service']['runningCount'] == 0:
    print("runningCount=0, sleeping")
    sleep(5)

print("runningCount>0, Done!!")