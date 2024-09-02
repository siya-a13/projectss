---
longform:
  format: single
  title: Amazon S3 - Performance
---
### 1. **S3 Baseline Performance**

Amazon S3 provides high availability and performance for storing and retrieving data. The baseline performance can vary based on several factors:

- **Read/Write Performance:**
    - **PUT/COPY/POST/DELETE requests**: S3 can handle hundreds to thousands of requests per second. By default, you can make **3,500 PUT/COPY/POST/DELETE** requests per second per prefix in a bucket.
    - **GET requests**: S3 can handle **5,500 GET/HEAD** requests per second per prefix.
- **Scalability:**
    - S3 automatically scales to handle any request rate, so your performance can scale up with your workload.
- **Data Consistency:**
    - S3 provides strong read-after-write consistency for PUTs of new objects and eventual consistency for overwrite PUTs and DELETEs.

To achieve optimal performance, consider using parallelization and optimizing the object key naming scheme to distribute load evenly across S3’s infrastructure.

### 2. **S3 Byte-Range Fetch**

S3 supports **byte-range fetches**, which allows you to retrieve only a specific portion of an object, rather than downloading the entire object. This is particularly useful for large files where you might only need a segment of the data.

**Use Cases:**

- **Resuming Partial Downloads:** If a download fails, you can resume it by fetching only the remaining part of the object.
- **Efficient Data Processing:** For processing large files in chunks (e.g., streaming video files), you can fetch only the required parts.
- **Parallel Downloads:** You can download different parts of the object in parallel, which can speed up the download process.

**How to Use:**

- When making a GET request, you can specify the `Range` header with the desired byte range, e.g., `Range: bytes=0-1023` to fetch the first 1024 bytes of the object.

### 3. **Multipart Upload**

Multipart upload in S3 allows you to upload large objects in multiple parts. This approach offers several advantages:

**Benefits:**

- **Parallel Uploads:** You can upload parts in parallel to speed up the upload process.
- **Resume Uploads:** If an upload fails, you only need to re-upload the failed part, not the entire object.
- **Optimized Network Utilization:** Multipart uploads can be optimized for network conditions by adjusting the part size and parallelization level.

**How it Works:**

1. **Initiate a Multipart Upload:** You start by sending an initiate multipart upload request to S3.
2. **Upload Parts:** Upload each part individually using a unique part number. Parts can be uploaded in parallel.
3. **Complete Multipart Upload:** After all parts are uploaded, send a complete multipart upload request, and S3 assembles the parts into the final object.

**Example:** You might divide a 5GB file into 100MB parts and upload each part separately. If part 5 fails, you only need to re-upload part 5 rather than starting over.

### 4. **S3 Transfer Acceleration**

S3 Transfer Acceleration is a feature that enables fast, secure, and reliable transfer of files over long distances between your client and an S3 bucket. It leverages Amazon CloudFront's globally distributed edge locations.

![[S3-transfer-acceleration.png]]

**How It Works:**

- **Global Edge Locations:** When you upload or download data to S3 using Transfer Acceleration, the data is first sent to the nearest CloudFront edge location. The data is then routed to S3 over Amazon’s optimized network paths, which can significantly improve transfer speeds compared to standard internet routes.
- **Ideal for Distributed Teams:** Especially useful when transferring data across continents or from distributed clients to a centralized S3 bucket.

**Enabling Transfer Acceleration:**

- You can enable Transfer Acceleration on a bucket level. Once enabled, you access the bucket via a specific endpoint (`bucketname.s3-accelerate.amazonaws.com`).

**Use Cases:**

- **Large File Uploads/Downloads:** Accelerate transfers of large files (e.g., media files, backups) from remote locations.
- **Latency-Sensitive Applications:** Applications requiring fast data upload/download times from global locations.

By leveraging these features, you can optimize your S3 usage for performance, scalability, and reliability, whether you're managing large files, processing data in chunks, or handling transfers across long distances.