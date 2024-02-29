import ibm_boto3
from ibm_botocore.client import Config, ClientError
from datetime import datetime, timedelta
import pytz

# Constants for IBM COS values
COS_ENDPOINT = 	"https://s3.us-south.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "mrRcJehhTissq2BGmfyPPlT3s8fMcuIMsJf_LOEe_EoR" # eg "W00YixxxxxxxxxxMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/63722e5308d7490dacf3aca6b0448cc7:a695fe6f-9c57-4a16-963a-a4d2c71f6c01::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003xxxxxxxxxx1c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

# Constants for Time
TIME_ZONE_LIMA = pytz.timezone('America/New_York')

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

def get_date_cos_file(file_name, bucket_name):
    try:
        response = cos.get_object(
            Bucket=bucket_name,
            Key=file_name,
        )

        return response['LastModified'].astimezone((TIME_ZONE_LIMA))
    except Exception as e:
        print("Unable to get data: {0}".format(e))

# get_date_cos_file("automatically_created_file_20240227_185711476109.txt","cos-test-efact-bucket-01")


def delete_cos_file(file_name, bucket_name, date_pivot):
    try:
        last_modified_file = get_date_cos_file(file_name, bucket_name)
        if date_pivot >= last_modified_file:
            response = cos.delete_object(
                Bucket=bucket_name,
                Key=file_name,
            )
            print(f"Archivo {file_name} eliminado")
        else:
            pass
    except Exception as e:
        print("Unable to delete object: {0}".format(e))

# date_str = "27/02/2024 6:57:14 pm"
# date_formated = datetime.strptime(date_str, "%d/%m/%Y %I:%M:%S %p")

# date_utc_minus_5 = TIME_ZONE_LIMA.localize(date_formated)

# delete_cos_file("automatically_created_file_20240227_185711476109.txt",
#                 "cos-test-efact-bucket-01", 
#                 date_utc_minus_5
# )
        

# OBTENER EL LISTADO DE OBJETOS DE UN BUCKET


def list_objects_buckets(bucket_name,days_diferential):
    response = cos.list_objects_v2(
        Bucket=bucket_name
    )

    date_pivot = datetime.now(TIME_ZONE_LIMA) - timedelta(days=days_diferential)
    cont_deleted_files = 0
    for item in response["Contents"]:
        object_date_utc = item["LastModified"].astimezone(TIME_ZONE_LIMA)
        
        if date_pivot >= object_date_utc:
            print(f"Se elimina: {item["Key"]}")
            cont_deleted_files = cont_deleted_files + 1
    print(f"Total de items: {len(response["Contents"])}")
    print(f"Total eliminados: {cont_deleted_files}")

