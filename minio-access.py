from minio import Minio
client = Minio('xaod.servicex.ssl-hep.org:443',
               access_key='miniouser',
               secret_key='leftfoot1',
               secure=True
               )

buckets = client.list_buckets()
print(buckets)
