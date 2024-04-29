import boto3
import hashlib
import binascii

def hash_partition_key(partition_key):
    """Return the MD5 hash of the partition key as a hex integer."""
    return int(hashlib.md5(partition_key.encode()).hexdigest(), 16)

def find_partition_key_for_shard(shard_start, shard_end):
    """Generate partition keys and check if their hash falls within the shard's range."""
    import random
    import string

    while True:
        # Generate a random string as a partition key
        random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        hash_key = hash_partition_key(random_key)
        
        # Check if the hash key falls within the shard's hash key range
        if shard_start <= hash_key <= shard_end:
            return random_key

# Example shard hash key ranges (you must replace these with actual values)
shard_start = 0  # Example start (hex converted to decimal)
shard_end = 113427455640312821154458202477256070484   # Example end (hex converted to decimal)

# Find a partition key that maps to the desired shard
suitable_partition_key = find_partition_key_for_shard(shard_start, shard_end)
print(f"Suitable partition key: {suitable_partition_key}")
























# import boto3

# client = boto3.client('kinesis', region_name='us-east-1')
# stream_name = 'sentimentanalysis'

# response = client.list_shards(StreamName=stream_name)
# shards = response.get('Shards', [])

# for shard in shards:
#     print(f"Shard ID: {shard['ShardId']}, Hash Key Range: {shard['HashKeyRange']}")
