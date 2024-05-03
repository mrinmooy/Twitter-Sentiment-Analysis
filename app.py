from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
import base64
from textblob import TextBlob
import pymysql
from pymysql import Error


app = Flask(__name__)
CORS(app)

aws_access_key_id = 'AKIA6GBMF4I4QCV5LOZX'
aws_secret_access_key = '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'

client = boto3.client(
    'kinesis',
    region_name='us-east-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)






stream_name = 'sentimentanalysis'



def send_data_to_kinesis(data, partition_key):
    
    data_encoded = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    response = client.put_record(
        StreamName=stream_name,
        Data=data_encoded,
        PartitionKey=partition_key
    )
    return response

@app.route('/api/positive', methods=['GET'])
def get_positive_tweets():
    
    shard_id = "shardId-000000000001"

    iterator_response = client.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='TRIM_HORIZON'   
    )

    shard_iterator = iterator_response['ShardIterator']
    
    all_records = []
    empty_response_count = 0   

    
    while shard_iterator and empty_response_count < 500:
        record_response = client.get_records(ShardIterator=shard_iterator, Limit=1000)
        records = record_response['Records']

        if records:
            tweets = [base64.b64decode(record['Data']).decode('utf-8') for record in records]
            all_records.extend(tweets)
            empty_response_count = 0  
        else:
            empty_response_count += 1  

        
        shard_iterator = record_response.get('NextShardIterator', None)

    
    # print(all_records)

    return jsonify(all_records)
   
@app.route('/api/negative', methods=['GET'])
def get_negative_tweets():

    shard_id = "shardId-000000000002"

    iterator_response = client.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='TRIM_HORIZON'  
    )

    shard_iterator = iterator_response['ShardIterator']

    all_records = []
    empty_response_count = 0   

    
    while shard_iterator and empty_response_count < 500:
        record_response = client.get_records(ShardIterator=shard_iterator, Limit=1000)
        records = record_response['Records']

        if records:
            tweets = [base64.b64decode(record['Data']).decode('utf-8') for record in records]
            all_records.extend(tweets)
            empty_response_count = 0  
        else:
            empty_response_count += 1  

        
        shard_iterator = record_response.get('NextShardIterator', None)

    
    # print(all_records)

    return jsonify(all_records)
   

@app.route('/api/tweet', methods=['POST'])
def send_tweet():

    data = request.get_json()  

    if data and 'tweet' in data:

        tweet_content = data['tweet'] 

        partition_key_positive = "rEAdDVUsxZ"
        partition_key_negative = "Ht5aIMMhsZ"

        analysis = TextBlob(tweet_content)
        tweet_polarity = analysis.polarity

        senti = 0
        global response

        if tweet_polarity >=0:
            print(0)
            response = send_data_to_kinesis(tweet_content, partition_key_positive)
            senti = 0
            print(response)  
        else:
            print(1)
            response = send_data_to_kinesis(tweet_content, partition_key_negative)
            senti = 1
            print(response)  

        try:
            connection = pymysql.connect(
                host='sql5.freesqldatabase.com',
                user='sql5702693',  # Replace with your actual username
                password='HfQNBBzFVX',  # Replace with your actual password
                database='sql5702693',
                port=3306
            )

            tweet_content = tweet_content[:100]
            with connection.cursor() as cursor:
                insert_query = """
                INSERT INTO allTweets (Content, Sentiment) VALUES (%s, %s);
                """
                cursor.execute(insert_query, (tweet_content, senti))
                connection.commit()
                # print(f"Data inserted: {my_string}, {my_bool}")

        except Error as e:
            print("Error while connecting to MySQL or operating", e)
        
        finally:
            if connection and connection.open:
                connection.close()
                print("MySQL connection is closed")


        return jsonify({"message": "Tweet sent to Kinesis stream", "alldetails": response}), 200

    else:

        return jsonify({"message": "No tweet data provided"}), 400


if __name__ == '__main__':
    app.run(debug=True)
