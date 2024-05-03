import boto3
import base64

def send_data_to_kinesis(stream_name, data, partition_key):
    # Initialize the Kinesis client
    client = boto3.client('kinesis', region_name='us-east-1')
    
    # Encode the data to base64 to ensure it is properly handled by Kinesis
    data_encoded = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    
    # Send the data
    response = client.put_record(
        StreamName=stream_name,
        Data=data_encoded,
        PartitionKey=partition_key
    )
    
    # Print the response from the Kinesis service
    print(response)

# Usage example
stream_name = 'sentimentanalysis'
data = "my health is bad i am sick"
partition_key = "Ht5aIMMhsZ"
send_data_to_kinesis(stream_name, data, partition_key)
