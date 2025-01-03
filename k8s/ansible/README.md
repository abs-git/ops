### Ansible

===

- kubernetes version: 1.28.2
- 


#### Setup
```shell
ansible-inventory -i setup/inventory/hosts.ini --list

# encrypt (option)
ansible-vault encrypt setup/inventory/hosts.ini
ansible-vault decrypt setup/inventory/hosts.ini

# allow root
ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/permit-root.yml

# status check
ansible workers -i setup/inventory/hosts.ini -m ping
ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/ping.yml --ask-vault-pass

# install kube
ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/kube-install.yml -vvv
ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/swap-off.yml

```

#### Clustering
```shell
# init cluster
ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/swap-off.yml
ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/clustering.yml

# add new workers
ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/new-workers.yml


```

#### Clustering (with kubespray) ..ing
```shell
git submodule update --recursive --remote

conda create -n kubespray python==3.10.* -y
conda activate kubespray
pip install -r kubespray/requirements.txt
```

```shell

ansible-playbook -i setup/inventory/hosts.ini -become --become-user=root kubespray/playbooks/cluster.yml


```