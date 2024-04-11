const awsConfig = require('./config/aws-config');

const { S3Client, ListBucketsCommand } = require("@aws-sdk/client-s3");

async function listS3Buckets() {
  const s3 = new S3Client({
    credentials: {
      accessKeyId: awsConfig.aws.accessKeyId,
      secretAccessKey: awsConfig.aws.secretAccessKey,
    },
    endpoint: awsConfig.aws.endpoint,
  });

  try {
    const response = await s3.send(new ListBucketsCommand({}));
    const Buckets = response.Buckets;
    console.log(Buckets);
  } catch (error) {
    console.error("Error listing buckets:", error);
  }
}

listS3Buckets();
