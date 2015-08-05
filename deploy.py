#!/usr/bin/python

from time import sleep
import boto3
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--service-name", dest='service_name', required=True)
args = parser.parse_args()

client = boto3.client('ecs', region_name='eu-west-1')

sys.stdout.write("Setting desiredCount=0\n")
sys.stdout.flush()
client.update_service(service=args.service_name, desiredCount=0)

while client.update_service(service=args.service_name)['service']['runningCount'] != 0:
    sys.stdout.write("runningCount!=0, sleeping\n")
    sys.stdout.flush()
    sleep(5)

sys.stdout.write("Setting desiredCount=1\n")
sys.stdout.flush()
client.update_service(service=args.service_name, desiredCount=1)

while client.update_service(service=args.service_name)['service']['runningCount'] == 0:
    sys.stdout.write("runningCount=0, sleeping\n")
    sys.stdout.flush()
    sleep(5)

sys.stdout.write("runningCount>0, Done!!\n")
sys.stdout.flush()