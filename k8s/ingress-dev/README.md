## dev

### fastapi app

```shell
# docker build -f fastapi/dockerfile -t fastapi-dev:latest .
docker buildx build --platform linux/arm64 -f fastapi/dockerfile -t fastapi-dev:latest .
docker run -p 8000:8000 fastapi-dev:latest
```

### AWS

```shell

export ecr=936433886933.dkr.ecr.ap-northeast-2.amazonaws.com
export repo=donghyun-fastapi
export access_key=
export secret_access_key=

aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin ${ecr}/${repo}

chmod +x ./fastapi/deploy-arm64.sh
./fastapi/deploy-arm64.sh --access_key $access_key \
                  --secret_access_key $secret_access_key \
                  --image donghyun-fastapi \
                  --tag app2 \
                  --template fastapi/app2.Dockerfile

chmod +x ./fastapi/deploy-x86.sh
./fastapi/deploy-x86.sh --access_key $access_key \
                  --secret_access_key $secret_access_key \
                  --image donghyun-fastapi \
                  --tag latest \
                  --template fastapi/dockerfile
```

### k8s
```shell
kubectl get nodes,svc,deployments,pods,ingress,secrets -A -o wide

```

### deployment

```shell
export ecr=936433886933.dkr.ecr.ap-northeast-2.amazonaws.com
export region=ap-northeast-2

# kubectl create secret generic test-secret \
#   --from-file=.dockerconfigjson=config.json \
#   --type=kubernetes.io/dockerconfigjson

kubectl create secret docker-registry donghyun-fastapi-secret \
  --docker-server=${ecr} \
  --docker-username=AWS \
  --docker-password=$(aws ecr get-login-password --region ap-northeast-2) \
  --namespace default
```

```shell
kubectl apply -f deploy/fastapi-worker1.yaml
kubectl delete -f deploy/fastapi-worker1.yaml
```

### ingress

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/baremetal/deploy.yaml

kubectl apply -f deploy/ingress.yaml

```

### test

```shell
curl http://192.168.0.6:30081
curl http://192.168.0.6:30082

curl http://192.168.0.6:30107/fastapi1
curl http://192.168.0.6:30107/fastapi2
```
