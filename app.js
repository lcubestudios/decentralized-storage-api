// app.js
const express = require('express');
const AWSController = require('./controllers/awsController');
const ConsoleView = require('./views/consoleView');
const awsConfig = require('./config/awsConfig'); 
const cors = require('cors'); // Import the cors middleware


const app = express();
const port = 3000;

const awsController = new AWSController(awsConfig);

app.use(cors({ origin: 'http://localhost:8080' }));

app.get('/listbuckets', async (req, res) => {
  try {
    const buckets = await awsController.listBuckets();
    ConsoleView.displayBuckets(buckets);
    res.json({ buckets });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.get('/listfiles', async (req, res) => {
  // '/listfiles/:bucketName'
  // const { bucketName } = req.params;
  const bucketName = 'photos';
  try {
    const files = await awsController.listFilesInBucket(bucketName);
    ConsoleView.displayFiles(files);
    res.json({ files });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
