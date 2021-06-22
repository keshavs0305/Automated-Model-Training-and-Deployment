import boto3
import pandas as pd
from io import StringIO

client = boto3.client('s3')

def lambda_handler(event, context):

    Bucket = 'level0-data'
    Key1 = 'input_data/train.csv'
    Key2 = 'input_data/new_data.csv'
    
    obj1 = client.get_object(Bucket = Bucket,Key = Key1)
    obj2 = client.get_object(Bucket = Bucket,Key = Key2)

    data1 = pd.read_csv(obj1['Body'])
    data2 = pd.read_csv(obj2['Body'])

    cols = [i for i in range(29)]
    data1.columns = cols
    data2.columns = cols

    dataf = data1.append(data2)
    
    csv_buffer = StringIO()
    dataf.to_csv(csv_buffer,header=False,index=False)
    
    s3_resource = boto3.resource('s3')
    s3_resource.Object(Bucket, Key1).put(Body=csv_buffer.getvalue())


    return {
    "Comment": "Insert your JSON here"
}