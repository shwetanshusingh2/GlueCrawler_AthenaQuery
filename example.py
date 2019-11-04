import boto3

bucket = 'bucket name'
key = 'key'
s3 = boto3.resource('s3')
versions = s3.Bucket("data-shwet").object_versions.filter(Prefix="lambda_trigger.py")
lar = [version for version in versions]
print(lar[0].get().get('VersionId'))
for version in versions:
    obj = version.get()
    print(obj.get('VersionId'), obj.get('ContentLength'), obj.get('LastModified'))