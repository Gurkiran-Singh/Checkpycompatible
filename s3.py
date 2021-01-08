import boto3
import os
import zipfile
import shutil


s3 = boto3.resource('s3')
s3.meta.client.download_file('bucketpy', 'serverless/checkpycompatible/dev/1610129844597-2021-01-08T18:17:24.597Z/checkpycompatible.zip', '/home/ubuntu/s3files/checkpycompatible.zip')


with zipfile.ZipFile('//home/ubuntu/s3files/checkpycompatible.zip', 'r') as zip_ref:

    zip_ref.extractall('//home/ubuntu/s3files//')


shutil.move("//home/ubuntu/s3files/handler.py", "//home/ubuntu/")

