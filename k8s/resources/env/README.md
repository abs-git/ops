## Configuration & Environment resource


### ConfigMap

일반적인 사용 형태는 환경 변수로 pod에 주입하는 것임.<br>
```shell
kubectl apply -f config-env.yaml
kubectl apply -f pod-env.yaml

```

ConfigMap에 json이나 yaml 형태로 데이터를 저장한 후 pod에서 volume 형태로 참조가 가능.<br>
```shell
kubectl apply -f config-volume.yaml
kubectl apply -f pod-volume.yaml

```

### Descripts

어플리케이션 동작 중 ConfigMap이 변경되면, 자동 롤링 업데이트로 인해 변경 사항을 자동으로 반영함.<br>
이때, deployment와 stateful 에서 replicas를 설정하여 프로세스의 중단을 최소화 함.<br>
<br>

### Note

```shell

log_level: "TRACE"
log_level: "DEBUG"
log_level: "INFO"
log_level: "WARN"
log_level: "ERROR"
log_level: "FATAL"
log_level: "OFF"



```



