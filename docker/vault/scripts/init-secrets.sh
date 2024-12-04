#!/bin/bash

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

until vault status; do
  echo "Waiting for Vault..."
  sleep 1
done

vault kv put secret/myapp username="admin" password="supersecretpassword"
vault kv put secret/database db_name="mydb" db_password="dbpassword"
