import boto3
import os

def upload_to_s3(bucket_name, file_name, folder_name):
    s3 = boto3.client('s3')

    current_directory = os.getcwd()

    full_file_path = os.path.join(current_directory, file_name)

    with open(full_file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            folder_key = f'{folder_name}/'

            object_key = f'{folder_key}line_{line_number}.txt'

            s3.put_object(Body=line, Bucket=bucket_name, Key=object_key)

            print(f'Uploaded line {line_number} to S3 in the folder: {folder_name}')


if __name__ == "__main__":
    bucket_name = 'random-verse'

    # Replace 'your_file_path.txt' with the path to the file you want to upload
    file_name = 'bible-kjv-full.txt'

    folder_name = 'bible-verses'

    upload_to_s3(bucket_name, file_name, folder_name)

