import os
import boto3
import random

def get_number_of_objects(bucket_name, prefix):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    return response.get('KeyCount', 0)

def choose_random_object(bucket_name, prefix):
    num_objects = get_number_of_objects(bucket_name, prefix)

    print(num_objects)

    if num_objects == 0:
        print(f"No objects found in the folder: {prefix}")
        return None

    random_index = random.randint(0, num_objects - 1)
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix).get('Contents', [])

    chosen_object = objects[random_index]

    print(chosen_object)

    return chosen_object['Key']

def read_object_content(bucket_name, object_key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    return response['Body'].read().decode('utf-8')

def send_to_sns(topic_arn, message):
    # sns = boto3.client('sns')
    # sns.publish(TopicArn=topic_arn, Message=message)
    print(f"Message sent to SNS topic: {topic_arn}")

def handler(event, context):
    bucket_name = 'random-verse'

    bible_verses_folder_name = 'bible-verses'

    sns_topic_arn = 'your_sns_topic_arn'

    random_object_key = choose_random_object(bucket_name, bible_verses_folder_name)

    if random_object_key:
        object_content = read_object_content(bucket_name, random_object_key)
        send_to_sns(sns_topic_arn, object_content)

if __name__ == "__main__":
    handler({},{})
