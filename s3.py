import boto3
import os
import zipfile
import shutil

filePath = '//var/lib/jenkins/workspace/checkaws';
s3filePath = 'serverless/checkpycompatible/dev/1610129844597-2021-01-08T18:17:24.597Z/checkpycompatible.zip'

s3 = boto3.resource('s3')
s3.meta.client.download_file('bucketpy', 'serverless/checkpycompatible/dev/1610129844597-2021-01-08T18:17:24.597Z/checkpycompatible.zip', '//var/lib/jenkins/workspace/checkaws/checkpycompatible.zip')

with zipfile.ZipFile('//var/lib/jenkins/workspace/checkaws//checkpycompatible.zip', 'r') as zip_ref:
    zip_ref.extractall('//var/lib/jenkins/workspace/checkaws//')

if os.path.exists(filePath):
    os.remove('filePath/checkpycompatible.zip')
    os.remove('filePath/package-lock.json')
    os.rmdir('filePath/node_modules')

else:
    print('Cannot delete the files')

os.system('sls deploy')

