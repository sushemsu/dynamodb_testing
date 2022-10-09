#!/usr/bin/env bash
set -xe
[[ ! -e DynamoDBLocal.jar ]] && curl -s "https://s3.us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz" | tar xzf -
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb &
