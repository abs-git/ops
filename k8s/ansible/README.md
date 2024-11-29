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

```

#### Clustering
```shell

ansible-playbook -i setup/inventory/hosts.ini setup/playbooks/clustering.yml -vvv

```