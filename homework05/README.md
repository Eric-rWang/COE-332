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
Command used to create the deployment.
```
$ kubectl apply -f deployment_C.yml
```
To get the IP address of the pods use the following command.
```
$ kubectl get pods -o wide
NAME                                 READY   STATUS    RESTARTS   AGE     IP             NODE   NOMINATED NODE   READINESS GATES
hello-deployment-c-bd689f9c9-pz7cs   1/1     Running   0          4m57s   10.244.3.230   c01    <none>           <none>
hello-deployment-c-bd689f9c9-sswjn   1/1     Running   0          4m57s   10.244.5.83    c04    <none>           <none>
hello-deployment-c-bd689f9c9-trn4z   1/1     Running   0          4m57s   10.244.6.114   c03    <none>           <none>
```
Checking the logs of each of the pods, it reveals the IP address is the same as output shown above.
```
$ kubectl logs hello-deployment-c-bd689f9c9-pz7cs
Hello, Eric Wang from IP 10.244.3.230
```
```
$ kubectl logs hello-deployment-c-bd689f9c9-sswjn
Hello, Eric Wang from IP 10.244.5.83
```
```
$ kubectl logs hello-deployment-c-bd689f9c9-trn4z
Hello, Eric Wang from IP 10.244.6.114
```

















