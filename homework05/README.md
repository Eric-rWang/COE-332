# Homework 05
## Table of Contents
* [Question A](#question-a)
* [Question B](#question-b)
* [Question C](#question-c)

## Question A
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
```