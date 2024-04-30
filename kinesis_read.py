import boto3
import base64

 
client = boto3.client('kinesis', region_name='us-east-1')

 
stream_name = 'sentimentanalysis'

 
shard_id = "shardId-000000000002"

 
iterator_response = client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)
shard_iterator = iterator_response['ShardIterator']

all_records = []
empty_response_count = 0   

 
while shard_iterator and empty_response_count < 20:
    record_response = client.get_records(ShardIterator=shard_iterator, Limit=1)
    records = record_response['Records']

    if records:
        tweets = [base64.b64decode(record['Data']).decode('utf-8') for record in records]
        all_records.extend(tweets)
        empty_response_count = 0  
    else:
        empty_response_count += 1  

     
    shard_iterator = record_response.get('NextShardIterator', None)

 
print(all_records)