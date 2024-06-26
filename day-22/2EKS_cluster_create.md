## EKS cluster create using eksctl prerequisition

Please follow the prerequisites doc before this.

## Create Cluster using eksctl with Fargate as worker node

```
eksctl create cluster --name demo-cluster --region us-east-1 --fargate
```

## Delete the cluster

```
eksctl delete cluster --name demo-cluster --region us-east-1
```
## update kubeconfig file so that we can use kubectl with this cluster
This command updates your kubeconfig file with configuration details for a specific Amazon EKS cluster. It retrieves the necessary information (like the cluster endpoint and authentication details) and adds a new context to your kubeconfig file. If the context for the specified cluster already exists, it updates it with the latest configuration.

```
aws eks update-kubeconfig --name demo-cluster

```