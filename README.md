# Setting up a Local Docker Registry and Deploying to Kubernetes

This document outlines the steps to create a local Docker registry, build and push a Docker image to it, and deploy it to a Kubernetes cluster, accessing it via NodePort.

## Step 1: Create a Local Docker Registry

We'll use the official `registry:2` image to create our local registry.

1.  **Run the Registry Container:**

    docker run -d -p 5000:5000 --restart=always --name registry registry:2
   
    This command starts a registry container on port 5000. The `--restart=always` flag ensures the registry restarts if it stops.

2.  **Verify the Registry:**

    You can check if the registry is running by visiting `http://<your-docker-host-ip>:5000/v2/` or http://localhost:5000/v2/ in your browser. If it's working, you should see an empty JSON response.

## Step 2: Build a Local Docker Image 

For this example, we'll create a simple Python Flask App For Book Search

1.  **Create a Dockerfile:**

    Dockerfile is already available here just execute the below command
	
	a) direct tagging with localhost 
	
		docker build . -t  localhost:5000/docker-book-store-local-repo

	b) ceate image without local tag
	
		docker build  -t  docker-book-store-local-repo .
	

## Step 3: Tag and Push the Docker Image to the Local Registry

1.  **Tag the Image:**

    Tag the image with the registry address and a name.

    
		docker tag docker-book-store-local-repo localhost:5000/docker-book-store-local-repo
    
	*Skip if you already  done 2.1.a above
	
    
2.  **Push the Image:**

    Push the tagged image to the local registry.


    docker push localhost:5000/docker-book-store-local-repo



## Step 4: Deploy to Kubernetes using `kubectl`

1.  **Create a Deployment YAML file ( `flask-py-app-deployment.yaml`):**

    
2.  **Apply the YAML files:**

    kubectl apply -f flask-py-app-deployment.yaml


3.  **Verify the Deployment and Service:**

    kubectl get deployments
    kubectl get services


## Step 5: Access the Application via NodePort

1.  **Get the Node IP:**

    Find the IP address of one of your Kubernetes nodes.

	kubectl get nodes -o wide

2.  **Access the Application:**
	
	http://<NodePort-IP>:32000
	
	if node port Ip not working check with localhost
	
    Open a web browser and navigate to http://localhost:32000. You should see the Book Search Page

