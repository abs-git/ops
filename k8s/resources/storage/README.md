

#### NFS 서버 생성
공유 디렉토리 경로: /mnt/shared <br>

```shell
# nfs 서버 (192.168.0.8 / master node)
sudo apt-get install nfs-kernel-server
/mnt/shared *(rw,sync,no_subtree_check)   # 모든 클라이언트에서 접근 가능

sudo exportfs -ra
sudo exportfs -v
sudo systemctl restart nfs-kernel-server

nfsstat -s

# nfs 서버 공유 디렉토리 마운트 테스트 (worker node)
sudo apt-get install nfs-common
sudo mount <nfs server ip>:/mnt/shared /mnt/shared     # nfs server ip: 192.168.0.8
sudo umount /mnt/shared
```

동적 프로비저닝 (NFS 서버)<br>
<br>
NFS provisioner: K8S에서 NFS 서버에 동적으로 디렉토리를 생성하고 PV를 자동으로 프로비저닝 함.<br>
동적 프로비저닝을 사용해 공유 디렉토리를 생성할 시 디렉토리 이름은 pvc-<<uid>> 로 생성됨. 변경하려면 provisioner를 수정해야함.<br>

```shell
kubectl apply -k github.com/kubernetes-sigs/nfs-subdir-external-provisioner/deploy
kubectl apply -f nfs-storage.yaml
```

#### deploy
```shell

# hostpath
kubectl apply -f hostpath-pv.yaml
kubectl apply -f hostpath-pvc.yaml
kubectl apply -f hostpath-pod.yaml

# nfs
kubectl apply -f nfs-pv.yaml
kubectl apply -f nfs-pvc.yaml
kubectl apply -f nfs-pod.yaml

kubectl get pv,pvc

```

### Descripts

일반적으로 pv가 생성된 환경에서 pvc는 조건에 맞는 pv를 찾아 바인딩 되는 형태임.<br>
<br>
PV는 독립적인 저장소 리소스이며 간 path가 중복되지 않도록 유의함.<br>
NFS 서버를 사용할 경우, 여러 개의 PV가 동일한 NFS 서버의 경로를 참조할 수 있음.<br>
이때, accessModes와 pvc의 storage 요청 크기 등의 차이를 두어 경쟁 상태를 해소함.<br>
<br>
hostPath는 PV가 배포되는 노드의 로컬 파일 시스템에 생성이 됨.<br>
hostPath의 경로가 이미 존재하면 해당 경로를 사용함. 지정된 경로가 없으면 생성.<br>
노드가 삭제되거나 pod가 다른 노드로 스케줄링 되면 데이터에 접근 불가.<br>
hostPath는 동적 프로비저닝을 지원하지 않으므로 pvc의 storage 크기는 pv 보다 작아야 함.<br>
<br>

### Note

```shell

PV와 PVC는 같은 accessModes를 사용해야 바인딩이 됨.

accessModes:
- ReadWriteOnce         # RWO: 하나의 노드에서만 '읽기/쓰기' 가능
- ReadWriteOncePod      # RWO-Pod: 단일 Pod에서만 '읽기/쓰기' 가능.
- ReadOnlyMany          # ROX: 여러 노드에서 '읽기' 전용으로 접근 가능.
- ReadWriteMany         # RWX: 여러 노드에서 '읽기/쓰기' 가능.

persistentVolumeReclaimPolicy: Retain     # PVC 삭제 시 PV 유지
persistentVolumeReclaimPolicy: Delete     # PVC 삭제 시 PV와 데이터도 삭제
persistentVolumeReclaimPolicy: Recycle    # PVC 삭제 시 PV 데이터 초기화 후 재사용 (v1.11 이후 사용하지 않음.)

```

