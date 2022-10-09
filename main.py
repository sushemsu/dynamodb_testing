#!/usr/bin/env python
import json
import ddb

ddb = ddb.ddb()
#ddb.destroy_table()
#ddb.destroy_table()
ddb.generate()

#client.scan(TableName="test", FilterExpression="#id > :min", ExpressionAttributeNames={"#id": "id"}, ExpressionAttributeValues={':min': {"N": "13"}})

