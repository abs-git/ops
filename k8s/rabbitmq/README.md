
### Docker
```shell
docker pull rabbitmq
docker run -d -p 15672:15672 -p 5672:5672 --name rabbitmq rabbitmq
docker exec rabbitmq rabbitmq-plugins enable rabbitmq_management

http://localhost:15672
```

### k8s
```shell
# Pod 종료시 대기열에 있는 데이터가 삭제되므로 Statefulset으로 생성

$ kubectl create namespace rabbitmq
$ kubectl apply -f rabbitmq-statefulset.yaml
$ kubectl apply -f rabbitmq-service.yaml
```