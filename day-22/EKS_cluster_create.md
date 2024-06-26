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



