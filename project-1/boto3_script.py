import boto3

aws_management_console = boto3.session.Session(profile_name="default")
iam = aws_management_console.resource('iam')
iam_client = aws_management_console.client('iam')
s3=aws_management_console.client('s3')
ec2 = boto3.client('ec2')


print("Resource",dir(iam))
print("Client",dir(iam_client.list_users()))
print("Client Bucket",dir(s3))

#listing out all the users in iam
for user in iam.users.all():
    print(user.name)

#listing out all the buckets in s3
for buckets in s3.buckets.all():
    print(buckets.name)

#listing out all the instances in ec2
for inst in ec2.describe_instances()['Reservations']:
    for each_inst in inst['Instances']:
        print(each_inst['InstanceId'])

# res = ec2.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
# pprint.pprint(res)

#Resource is higher order object which is only available for some aws services
#client is low-level service 
#https://boto3.amazonaws.com/v1/documentation/api/1.14.0/index.html