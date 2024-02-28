from upload_cos import upload_file
from create_files import generate_file

BUCKET_NAME = "cos-test-efact-bucket-01"

for i in range(1, 11):
    filename = generate_file("automatically_created_file")
    upload_file(BUCKET_NAME, filename, filename)
