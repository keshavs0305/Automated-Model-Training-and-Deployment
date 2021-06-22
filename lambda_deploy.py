import boto3

client = boto3.client('sagemaker')

def lambda_handler(event, context):

    model_name = event["taskresult"]["ModelArn"].split("/")[-1]
    
    response = client.create_endpoint_config(
    EndpointConfigName=model_name,
    ProductionVariants=[
        {
            'VariantName': model_name,
            'ModelName': model_name,
            'InitialInstanceCount': 1,
            'InstanceType': 'ml.t2.medium'
            }
    ]
    )
    
    response = client.create_endpoint(
    EndpointName=model_name,
    EndpointConfigName=model_name
    )
    
    return