import boto.ec2
import datetime
conn = boto.ec2.connect_to_region("us-west-2",aws_access_key_id='AKIAJPXNQTF2TT5HKAAA',aws_secret_access_key='ibpsvLK8D7vZeDsAaWd2DJyOm5rLTOXE096ouk7f')
present_time =datetime.datetime.now().replace(second=0, microsecond=0)
next_time = datetime.datetime.now().replace(second=0, microsecond=0) + datetime.timedelta(minutes = 10)
print(present_time)
print (next_time)
conn.start_instances(instance_ids=['i-09bf0786ee02b7ade'])
serveron = True
print ("server started")
print (present_time.time())
while True:
    present_time = datetime.datetime.now().replace(second=0, microsecond=0)
    if next_time.time() <= present_time.time():
        if serveron:
            conn.stop_instances(instance_ids=['i-09bf0786ee02b7ade'])
            serveron=False
            print("server stopped")
            print(present_time)
        else:
            conn.start_instances(instance_ids=['i-09bf0786ee02b7ade'])
            serveron = True
            print("server started")
            print(present_time)
        next_time = datetime.datetime.now().replace(second=0, microsecond=0) + datetime.timedelta(minutes=10)

#conn.start_instances(instance_ids=['i-09bf0786ee02b7ade'])
#conn.stop_instances(instance_ids=['i-09bf0786ee02b7ade'])

