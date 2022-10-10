#!/usr/bin/env bash
set -xepP -- -
[[ ! -e DynamoDBLocal.jar ]] && curl -s "https://s3.us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz" | tar xz DynamoDBLocal.jar DynamoDBLocal_lib -f - 
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb &
