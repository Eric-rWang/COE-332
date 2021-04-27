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
$ curl -X POST -H "content-type: application/json" -d '{"start":"1", "end":"2"}' 10.244.10.27:5000/jobs
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
$ curl -X POST -H "content-type: application/json" -d '{"start":"1", "end":"2"}' 10.244.10.27:5000/jobs
```
To check the IP of the pods, exec into a k8 pod and run python.
```
>>> from jobs import *
>>> rd.keys()
# from the result, select each key and paste it in the following command
>>> rd.hmget('<keys>','pod_ip')
# results for all 10 should look like the following
{b'id': b'53d72b83-0e67-4770-8fc8-0b605955cac9', b'pod_ip': b'10.244.10.29'}
{b'id': b'9508ad95-cb0e-474a-8e26-4f658a7a5516', b'pod_ip': b'10.244.15.170'}
{b'id': b'c656c939-984a-41b1-baa3-15f364358f82', b'pod_ip': b'10.244.10.29'}
{b'id': b'24095177-c29a-41d7-8033-9da5f9e8f5aa', b'pod_ip': b'10.244.15.170'}
{b'id': b'aef1e265-fa41-4bdc-902a-59dedcf2b4cb', b'pod_ip': b'10.244.15.170'}
{b'id': b'0e24d99e-d0c5-4a91-8f98-e57f7e27e9ed', b'pod_ip': b'10.244.10.29'}
{b'id': b'32ea2f9c-73cd-4ccb-a75e-704938ef2754', b'pod_ip': b'10.244.15.170'}
{b'id': b'63488a3c-0234-408f-899f-f9d426bb1254', b'pod_ip': b'10.244.10.29'}
{b'id': b'ad31b9e7-d602-4b8b-84e8-7476ed618fd4', b'pod_ip': b'10.244.15.170'}
{b'id': b'6a106bbd-a876-4aa0-a4fa-65382b3f7d2c', b'pod_ip': b'10.244.10.29'}
```
It is interesting to note that when we scale the worker pods to 2, the jobs in the queue are split between the two pods.
As shown in the results above, there is an equal amount of jobs finished by both pods, 5 each. The IP address of the two
pods also match the IP shown when the following command is ran.
```
$ kubectl get pod -o wide
NAME                                           READY   STATUS    RESTARTS   AGE    IP              NODE                         NOMINATED NODE   READINESS GATES
ewang-hw7-worker-6f76c966d5-fwrxg              1/1     Running   0          19m    10.244.10.29    c009.rodeo.tacc.utexas.edu   <none>           <none>
ewang-hw7-worker-6f76c966d5-tnmnt              1/1     Running   0          15m    10.244.15.170   c03                          <none>           <none>
```














