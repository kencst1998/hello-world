
minikube start

--- hello-world app:
kubectl create -f webserver/redis_cluster.yml
kubectl create -f webserver/webserver_rc.yml
kubectl create -f webserver/webserver_svc.yml

* output: http://192.168.99.100:30080/
* reference: https://github.com/prometheus/client_python/blob/master/README.md

--- jenkins:
kubectl create -f jenkins/jenkins-master.yml
kubectl create -f jenkins/service.yml
kubectl create -f jenkins/jenkins-slaves.yml

* Jenkins homepage: http://192.168.99.100:31031/
* manage jenkins -> Available -> install git plugin
* create git repository: https://github.com/kencst1998/hello-world.git
* build comment: cd webserver && docker build -t stchen2017/hello_world .
* reference: https://github.com/carlossg/kubernetes-jenkins

--- prometheus:
kubectl create configmap prometheus-server-conf --from-file=prometheus/config.yml
kubectl create -f prometheus/deployment.yml
kubectl create -f prometheus/service.yml

* prometheus homepage: http://192.168.99.100:30434/graph
* available app specific count: total_requests
* references:
* https://github.com/prometheus/prometheus/blob/master/documentation/examples/prometheus-kubernetes.yml
* https://coreos.com/blog/prometheus-and-kubernetes-up-and-running.html

--- rolling update:
kubectl rolling-update hello-world --image=stchen2017/hello_world:latest --image-pull-policy=Always

