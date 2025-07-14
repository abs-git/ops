## model resistry


### Mlflow
```shell
sudo apt-get install apache2-utils
htpasswd -c ./docker/htpasswd donghyun

docker network create mlflow-net

docker-compose -f docker/docker-compose.yaml build
docker-compose -f docker/docker-compose.yaml up -d

```

```shell
http://localhost:8080
http://localhost:9001
```