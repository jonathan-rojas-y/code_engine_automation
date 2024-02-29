from upload_cos import upload_file, list_objects_buckets
from create_files import generate_file
import os

days_diferential = os.environ.get("DAYS_DIFERENTIAL")
bucket_name = os.environ.get("BUCKET_NAME")


# for i in range(1, 11):
#     filename = generate_file("automatically_created_file")
#     upload_file(BUCKET_NAME, filename, filename)

list_objects_buckets(bucket_name, float(days_diferential))