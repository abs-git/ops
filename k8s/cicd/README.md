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

```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# 초기 비밀번호 확인
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 --decode

# 비밀번호 변경
kubectl exec -it -n argocd deployment/argocd-server -- /bin/bash
argocd login 0.0.0.0:9000 --username admin --password <password>
argocd account update-password

```

```shell
kubectl port-forward --address=0.0.0.0 svc/argocd-server -n argocd 8080:443
```

repository register
```shell
```

application deployment
```shell
```