import boto3
import csv
import os
import subprocess
import time

# check entropy for 5 minutes
seconds = 0
N = 360
results = [["seconds", "count", "entropy_avail"]]
filename_abs = '/home/ec2-user/RHEL6_entropy_results.csv'
filename_rel = 'RHEL6_entropy_results.csv'

for i in range(N):
    with open("count.txt", "r") as f:
        count = f.readline()
    entropy = os.popen('cat /proc/sys/kernel/random/entropy_avail').read()
    entropy = int(entropy.strip('\n'))
    results.append([seconds, count, entropy])
    time.sleep(1)
    seconds += 1

# write to .csv
with open(filename_abs, "w") as f:
    writer = csv.writer(f)
    writer.writerows(results)

# upload to s3
bucket = 'entropy'
object_name = filename_rel
s3_client = boto3.client('s3')
response = s3_client.upload_file(filename_abs, bucket, object_name, ExtraArgs={"ServerSideEncryption": "aws:kms"})
