import boto3
import base64

# Initialize a Kinesis client
client = boto3.client('kinesis', region_name='us-east-1')

# Name of your Kinesis stream
stream_name = 'sentimentanalysis'

# Shard ID, this should be dynamically fetched or specified based on your application logic
shard_id = "shardId-000000000002"

# Get an iterator for the shard
iterator_response = client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)
shard_iterator = iterator_response['ShardIterator']

all_records = []
empty_response_count = 0  # To track consecutive empty responses

# Fetch records in a loop until there are 100 consecutive empty responses
while shard_iterator and empty_response_count < 20:
    record_response = client.get_records(ShardIterator=shard_iterator, Limit=1)
    records = record_response['Records']

    if records:
        # all_records.extend(records)  # Merge non-empty records
        # Decode and process your records as needed
        tweets = [base64.b64decode(record['Data']).decode('utf-8') for record in records]
        # Print or process the tweets
        print(tweets)
        # all_records.extend(tweets)
        empty_response_count = 0  # Reset the empty response count when records are found
    else:
        empty_response_count += 1  # Increment empty response count when no records are found

    # Get the next shard iterator
    shard_iterator = record_response.get('NextShardIterator', None)

# Optionally process all records outside the loop if needed
print(all_records)