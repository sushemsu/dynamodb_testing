#!/usr/bin/env python
"""
generic module for learning stuffs for the dynamodb
docref dynamodb sawce
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_table
"""
import boto3
import random
import datetime
import json
import time
import threading
import uuid

class ddb:
	client = boto3.client
	tableName = 'test'

	def __init__(self, setup=True):
		"""setup connect to local dynamo db through boto client, supports setup bool (wipes db on true)"""
		self.client = boto3.client("dynamodb", endpoint_url="http://127.0.0.1:8000");
		if setup:
			self.setup_table()

	def destroy_table(self):
		"""destroys table specified in class"""
		self.client.delete_table(TableName=self.tableName)

	def table_exists(self):
		"""return bool if class.tableName exists in local dynamodb"""
		try:
			self.client.describe_table(TableName=self.tableName)
			return(True)
		except:
			return(False)

	def setup_table(self):
		"""runs a create table for example data"""
		if(self.table_exists()):
			self.destroy_table()
		else:
			self.client.create_table(
				AttributeDefinitions=[{'AttributeName': 'uuid', 'AttributeType': 'S'},{'AttributeName': 'date', 'AttributeType': 'S'}],
				TableName=self.tableName,
				KeySchema=[{'AttributeName': 'uuid', 'KeyType': 'HASH'}, {'AttributeName': 'date', 'KeyType': 'RANGE'}],
				BillingMode='PAY_PER_REQUEST'
				)

	def generate_thread(self, run_duration=30, sleep_duration=1):
		"""populates generic uuid(time based) and datetime data for dynamodb"""
		for i in range(run_duration):
			uuid_gen = uuid.uuid1()
			date_now = datetime.datetime.now()
			self.client.put_item(TableName=self.tableName, Item={'uuid': {'S': str(uuid_gen)}, 'date': {'S': str(date_now)}})
			time.sleep(sleep_duration)

	def generate(self):
		"""used to call background thread for generate_thread"""
		generate_thread = threading.Thread(target=self.generate_thread, name="generate_thread")
		generate_thread.start()

def main():
	print("not designed to be directly invoked")

if __name__ == "__main__":
	main()
