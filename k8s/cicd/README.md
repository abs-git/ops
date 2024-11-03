### Jenkins

Install
```shell
docker compose -f jenkins/docker-compose.yaml up

sudo docker exec -it jenkins bash
cat /var/jenkins_home/secrets/initialAdminPassword
> key

localhost:8080

```

repository register
```shell

ssh-keygen -t rsa -f .ssh/jeknins-key

```



### ArgoCD