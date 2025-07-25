#!/bin/bash

while [[ "$#" -gt 0 ]]; do
  case $1 in
    --access_key)
      access_key="$2"
      shift
      ;;
    --secret_access_key)
      secret_access_key="$2"
      shift
      ;;
    --image)
      image="$2"
      shift
      ;;
    --tag)
      tag="$2"
      shift
      ;;
    --template)
      template="$2"
      shift
      ;;
    *)
      echo "Unknown parameter: $1"
      exit 1
      ;;
  esac
  shift
done

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
ssh-add -l

export repo=936433886933.dkr.ecr.ap-northeast-2.amazonaws.com
export image
export tag
export template

aws configure set aws_access_key_id "$access_key"
aws configure set aws_secret_access_key "$secret_access_key"
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin ${repo}

export DOCKER_BUILDKIT=1
docker buildx build --platform linux/arm64 -f $(pwd)/${template} \
  -t ${repo}/${image}:${tag} . --push

echo "Done.."
