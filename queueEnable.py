
import boto3
# Add your creds
my_session = boto3.session.Session(aws_access_key_id="",  aws_secret_access_key="",region_name="")
client = my_session.client('lambda')


# If you want to enable all
function_name = [
'name_of_function'
]

# If Only particular map
function_sqs_mapper = {
    "name_of_function":"its_EventSourceArn"
}

for name in function_name:

    response = client.list_event_source_mappings(
        FunctionName=name,
    )

    for i in response['EventSourceMappings']:
        response = client.update_event_source_mapping(
        Enabled=True,
        FunctionName=i['FunctionArn'],
        UUID=i['UUID'],
    )

    print(response)


for name,source_arn in function_sqs_mapper.items():
    response = client.list_event_source_mappings(
        FunctionName=name,
        EventSourceArn = source_arn
    )

    for i in response['EventSourceMappings']:
        response = client.update_event_source_mapping(
        Enabled=True,
        FunctionName=i['FunctionArn'],
        UUID=i['UUID'],
    )

    print(response)
