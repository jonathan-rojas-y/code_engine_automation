# from upload_cos import upload_file, list_objects_buckets
from create_files import generate_file
import os

BUCKET_NAME = "cos-test-efact-bucket-01"

# for i in range(1, 11):
#     filename = generate_file("automatically_created_file")
#     upload_file(BUCKET_NAME, filename, filename)

days_diferential = os.environ.get("DAYS_DIFERENTIAL")

# list_objects_buckets("cos-test-efact-bucket-01", days_diferential)

print(days_diferential)
print(type(days_diferential))