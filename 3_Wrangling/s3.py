#!/usr/bin/env python
# coding: utf-8


# Let's use Amazon S3		



def get_file(s3,bucket_name=None,download_file=None,rename_file=None):
    
    bucket = s3.Bucket(bucket_name)

    with open(rename_file, 'wb') as data:
        bucket.download_fileobj('{f}'.format(f=download_file), data)

    return rename_file


def upload_file(s3,bucket_name=None,upload_file=None,rename_file=None):
    
    with open(upload_file, 'rb') as data:
        s3.Bucket(bucket_name).put_object(Key=rename_file, Body=data)

    return rename_file