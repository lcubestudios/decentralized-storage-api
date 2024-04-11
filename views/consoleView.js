// views/consoleView.js
class ConsoleView {
  static displayBuckets(buckets) {
    console.log("Buckets:");
    buckets.forEach(bucket => {
      console.log(bucket.Name);
    });
    console.log("\n");
  }

  static displayFiles(files) {
    console.log("Files in the bucket:");
    files.forEach(file => {
      console.log(file);
    });
    console.log("\n");
  }
}

module.exports = ConsoleView;
