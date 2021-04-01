# Using Kubernetes
## Table of Contents
* [Part A](#part-a)
* [Part B](#part-b)
* [Part C](#part-c)

## Part A
Command to create the pod.
```
$ kubectl apply -f kube_A.yml
```
Command to get the pod using an appropriate selector.
```
$ kubectl get pods --selector "greeting=personalized"
```
The output of the command above is as follows...
```
NAME      READY     STATUS     RESTARTS      AGE
hello     1/1       Running    0		 	 6m30s
```
Checking the logs of the pod, the output is what is expected.
```
$ kubectl logs hello
Hello,
```
To delete the pod, the command below is used.
```
$ kubectl delete pods hello
pod "hello" deleted
```

## Part B
Command to create the pod.
```
$ kubectl apply -f kube_B.yml
```
Command used to check the logs of the pod and its output.
```
$ kubectl logs hello
Hello, Eric Wang
```
To delete the pod, the command below is used.
```
$ kubectl delete pods hello
pod "hello" deleted
```

## Part C


















