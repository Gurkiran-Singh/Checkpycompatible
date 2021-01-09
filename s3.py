import boto3
import os
import zipfile
import shutil


s3 = boto3.resource('s3')
s3.meta.client.download_file('bucketpy', 'serverless/checkpycompatible/dev/1610129844597-2021-01-08T18:17:24.597Z/checkpycompatible.zip', '/var/lib/jenkins/workspace/checkaws/checkpycompatible.zip')


with zipfile.ZipFile('//var/lib/jenkins/workspace/checkaws/checkpycompatible.zip', 'r') as zip_ref:

    zip_ref.extractall('//var/lib/jenkins/workspace/checkaws//')


os.remove('//var/lib/jenkins/workspace/checkaws/checkpycompatible.zip, package-lock.json')

