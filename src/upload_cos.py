import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = 	"https://s3.us-south.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "mrRcJehhTissq2BGmfyPPlT3s8fMcuIMsJf_LOEe_EoR" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/63722e5308d7490dacf3aca6b0448cc7:a695fe6f-9c57-4a16-963a-a4d2c71f6c01::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

# Create client 
cos = ibm_boto3.client("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

def get_buckets():
    print("Retrieving list of buckets")
    try:
        # buckets = cos.objects.all()
        buckets = cos.list_buckets()
        for bucket in buckets['Buckets']:
            print("Bucket Name: {0}".format(bucket["Name"]))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))

def upload_file(bucket_name, file_name, cos_file_name):
    try:
        with open(file_name, "rb") as f:
            cos.upload_fileobj(f, bucket_name, cos_file_name)
        print("Archivo cargado")
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))