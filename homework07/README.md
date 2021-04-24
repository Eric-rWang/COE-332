# Deploying Flask API to k8s
## Table of Contents
* [Part A](#part-a)
* [Part C](#part-c)

## Part A
To create the deployments for both the flask and worker, the following commands were used.
```
$ kubectl apply -f ewang-hw7-flask-deployment.yml
deployment.apps/ewang-hw7-flask-deployment created
```
```
$ kubectl apply -f ewang-hw7-worker-deployment.yml
deployment.apps/ewang-hw7-worker-deployment created
```

To make a POST request with curl...
```
$ curl -X POST -H "content-type: application/json" -d '{"key2": ["a", "json", "list"]}' 10.244.5.83/jobs

```

## Part C
Scaling the deployment to 2 pods.
```
$ kubectl scale deployment ewang-hw7-flask-deployment --replicas=2
```

















