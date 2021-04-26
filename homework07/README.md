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
To make a POST request with curl and the expected output.
```
$ curl -X POST -H "content-type: application/json" -d '{"start":"1", "end":"2"}' 10.244.15.30:5000/jobs
{"id": "3924d089-e8d5-42ee-8ceb-cec5b413f81f", "status": "submitted", "start": "1", "end": "2"}
```
To check that the job went to completion, exec into a k8 pod and run python.
```
>>> from jobs import *
>>> rd.keys()
[b'job.3924d089-e8d5-42ee-8ceb-cec5b413f81f']
>>> rd.hgetall('job.3924d089-e8d5-42ee-8ceb-cec5b413f81f')
{"id": "3924d089-e8d5-42ee-8ceb-cec5b413f81f", "status": "complete", "start": "1", "end": "2"}
```

## Part C
Scaling the deployment to 2 pods.
```
$ kubectl scale deployment ewang-hw7-worker-deployment --replicas=2
```
To create 10 new jobs, the curl command from part A can be used 10 times.
```
$ curl -X POST -H "content-type: application/json" -d '{"start":"1", "end":"2"}' 10.244.15.71:5000/jobs
```
To check the IP of the pods, exec into a k8 pod and run python.
```
>>> from jobs import *
>>> rd.keys()
# from the result, select each key and paste it in the following command
>>> rd.hgetall('<keys>')
# results for all 10 should look like the following

```
















