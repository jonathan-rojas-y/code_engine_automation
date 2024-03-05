from upload_cos import upload_file, list_objects_buckets
from create_files import generate_file
import os
from datetime import datetime

days_diferential = os.environ.get("DAYS_DIFERENTIAL")
bucket_name = os.environ.get("BUCKET_NAME")

hora_actual = datetime.now().time()

list_objects_buckets(bucket_name, float(days_diferential))