import boto3
import collections
import time; time.time()
import datetime
import os

region = 'sa-east-1'

def lambda_handler(event, context):
    # Calculating 1 week ago as begin date and 6 days ago as end date in milliseconds
    ms = int(round(time.time() * 1000))
    begin_date = (ms - 604800000)
    end_date = (ms - 518400000)

    # Get today date to input in prefix
    prefixDt = []
    today = datetime.date.today()
    prefixDt.append(today)

    # Create export task from CloudWatch log group to S3 
    client = boto3.client('logs')
    response = client.create_export_task(
    taskName='export to S3',
    logGroupName=os.environ['GroupName'], # Don't forget to define Environment Variable 'GroupName' 
    fromTime=begin_date,
    to=end_date,
    destination=os.environ['bucket'], # Don't forget to define Environment Variable 'bucket'
    destinationPrefix = str(prefixDt[0])
    )
    print(response)