import boto3
import os
import zipfile
import shutil

filePath = '//var/lib/jenkins/workspace/checkaws';


s3 = boto3.resource('s3')
prefix = 'serverless/checkpycompatible/dev/1610129844597-2021-01-08T18:17:24.597Z/checkpycompatible.zip' 


s3.meta.client.download_file('bucketpy', prefix , '//var/lib/jenkins/workspace/checkaws/checkpycompatible.zip')

with zipfile.ZipFile('//var/lib/jenkins/workspace/checkaws//checkpycompatible.zip', 'r') as zip_ref:
    zip_ref.extractall('//var/lib/jenkins/workspace/checkaws//')

if os.path.exists(filePath):
    os.remove( filePath +  '/checkpycompatible.zip')
    #os.remove('//var/lib/jenkins/workspace/checkaws//package-lock.json')
    #shutil.rmtree('//var/lib/jenkins/workspace/checkaws//node_modules')

else:
    print('Cannot delete the files')

#os.system('sls deploy')

