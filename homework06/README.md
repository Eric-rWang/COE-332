# Deploying Flask API to k8s
## Table of Contents
* [Part 1](#part-1)
* [Part 2](#part-2)
* [Part 3](#part-3)
* [Part 4](#part-4)
* [Part 5](#part-5)

## Part 1
Before working on part 1. The creation of the deployment, pvc, service, and debug yml files are needed.
Creating the PVC (persistent volume claim) for the Redis data required these information.
```
labels:
	username: ewang
	env: test
```
```
accessModes:
	- ReadWriteOnce
```
```
storageClassName: rbd
resources:
	requests:
		storage: 1Gi
```
To create the PVC the following command is used.
```
$ kubectl apply -f ewang-pvc.yml
```
The output should be...
```
persistentvolumeclaim/ewang-pvc-data created
```

## Part 2
Creating the deployment for the Redis database requires these information.
* Using the same labels in the PVC and include an app label with value ewang-test-redis
* Setting replicas to 1
* The image used is redis:5.0.0
* Creating a volumeMount and associate it with a volume, mount path is /data

Creating the deployment is the same as the PVC.
```
$ kubectl apply -f ewang-test-redis-deployment.yml
```
Output is the following.
```
deployment.apps/ewang-test-deployment created
```

## Part 3
A service is needed for the Redis database. Creating one requires the following information.
* Using the same username and env labels as before
* type should be ClusterIP
* Defined a selector
* port and targetPort set to 6379

To create the service.
```
$ kubectl apply -f ewang-test-redis-service.yml
```
Output is the following.
```
service/ewang-service created
```

To verify steps 1 through 3 are working, the following is done.
```
$ kubectl get services
NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
ewang-service              ClusterIP   10.101.218.139   <none>        6379/TCP   23h
```
The command above is run to get the IP of the test redis service shown in the output.
With the Cluster-IP, the next step is the exec into the debug container.
```
$ kubectl get pods
NAME                                           READY   STATUS              RESTARTS   AGE
ewang-debug-deployment-5cc8cdd65f-5k8lh        1/1     Running             0          23h
ewang-test-deployment-9f89b9c68-9g2fs          1/1     Running             0          22h
```
```
$ kubectl exec -it ewang-debug-deployment-5cc8cdd65f-5k8lh -- /bin/bash
```
Inside the pod install redis, launch the python shell, import redis and create a Python redis client object.
```
$ pip install redis
$ python
> import redis
> rd = redis.StrictRedis(host='10.101.218.139', port=6379, db=0)
```
To verify the the Redis service is storing the data a key created.
```
> rd.set('key','test')
```
Delete the redis pod and verify k8s creates a new redis pod.
```
$ kubectl delete pods ewang-test-deployment-9f89b9c68-9g2fs
pod "ewang-test-deployment-9f89b9c68-9g2fs" deleted
```
Running kubectl get pods, it is seen that k8s creates a new redis pod and inside the debug container, running
rd.get('key') returns 'test' showing the data infact survived the pod restart.

## Part 4
Creating a deployment for the flask API, the Redis deployment can be carried over with minor changes.
* Using the same username and env labels as before
* 2 replicas instead of 1
* Expose port 5000
```
$ kubectl apply -f ewang-test-flask-deployment.yml
deployment.apps/ewang-test-flask-deployment created
```

## Part 5
Next, creating the service for flask API requires the following.
* Using the same username and env labels as before
* The type of service is ClusterIP
* Defined a selector
* port and targetPort is 5000
```
$ kubectl apply -f ewang-test-flask-service.yml
service/ewang-test-flask-service created
```


























