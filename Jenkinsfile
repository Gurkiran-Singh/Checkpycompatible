pipeline{
    
    agent any 
    
    stages{
       
        
        
    stage('Downloading and Deploying S3 Artifact in Kubeless'){
        
        steps{
            
        sh """
        
        #!/bin/bash
        
        
        python3 /var/lib/jenkins/workspace/checkaws/s3.py
        
      	echo "Lambda Function has been Successfuly Deployed in Kubeless Cluster"

	echo "Showing the list of deployed functions in Kubeless Cluster"
        
        kubeless function ls
            
           """ 
            
        }
        
        
    }
        
    }
}
    
