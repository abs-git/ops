
#### Reference
* https://helm.sh/ko/docs/


#### Cmd

기본 명령어
```shell
helm create test 
```

```shell
# 배포
helm install test ./test -f values.yaml

# 수정
helm upgrade test ./test -f values.yaml
helm upgrade test ./test --set pullPolicy=IfNotPresent
helm get values pullPolicy

# 롤백
helm history test
helm rollback test pullPolicy 1

# 삭제
helm uninstall test
helm uninstall test --keep-history  # 기록 보존

```

helm 차트 저장소
* 패키지 형태(.tgz)로 저장된 오픈소스 차트 저장소
```shell
# 저장소 검색
helm search hub <chart name>

# 저장소 추가
helm repo add <repo name> <repo url>

# 저장소 내 차트 검색
helm search repo <repo name>

# 내 저장소 리스트
helm repo list

```

상태 확인
```shell
helm status test

helm list
helm list --namespace <namespace>

```