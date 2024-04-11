// controllers/awsController.js
const AWSModel = require('../models/awsModel');
const awsConfig = require('../config/awsConfig'); // Adjust the path as needed

class AWSController {
  constructor() {
    this.model = new AWSModel(awsConfig);
  }

  async listBuckets() {
    try {
      return await this.model.listBuckets();
    } catch (error) {
      throw new Error(`Controller Error: ${error.message}`);
    }
  }

  async listFilesInBucket(bucketName) {
    try {
      return await this.model.listFilesInBucket(bucketName);
    } catch (error) {
      throw new Error(`Controller Error: ${error.message}`);
    }
  }
}

module.exports = AWSController;
