const { S3Client, ListBucketsCommand, ListObjectsV2Command } = require("@aws-sdk/client-s3");
const awsConfig = require('../config/awsConfig'); 

class AWSModel {
  constructor() {
    this.s3 = new S3Client({
      credentials: {
        accessKeyId: awsConfig.accessKeyId,
        secretAccessKey: awsConfig.secretAccessKey,
      },
      endpoint: awsConfig.endpoint,
    });
  }

  async listBuckets() {
    try {
      const response = await this.s3.send(new ListBucketsCommand({}));
      return response.Buckets;
    } catch (error) {
      console.error("Error listing buckets:", error);
      throw new Error(`Controller Error: Error listing buckets: ${error.message}`);
    }
  }

  async listFilesInBucket(bucketName) {
    try {
      const response = await this.s3.send(new ListObjectsV2Command({
        Bucket: bucketName,
      }));
      return response.Contents.map(object => object.Key);
    } catch (error) {
      console.error("Error listing files in the bucket:", error);
      throw new Error(`Controller Error: Error listing files in the bucket: ${error.message}`);
    }
  }
}

module.exports = AWSModel;
