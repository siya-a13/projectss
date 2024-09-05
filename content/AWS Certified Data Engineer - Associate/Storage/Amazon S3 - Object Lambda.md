---
longform:
  format: single
  title: Amazon S3 - Object Lambda
title: Amazon S3 - Object Lambda
---
Amazon S3 Object Lambda is a feature that allows you to customize and process objects as they are retrieved from Amazon S3. With S3 Object Lambda, you can run Lambda functions on your S3 objects in real-time as part of the retrieval process, transforming the data or enriching it before it is returned to the requester.

![[s3 object lambda.png]]

### Key Features:

1. **On-the-Fly Data Transformation:**
    
    - You can use Lambda functions to modify the contents of S3 objects when they are requested. For example, you could resize an image, convert a file format, or redact sensitive information.
2. **Customizable Responses:**
    
    - Customize the content and metadata of objects returned from S3 without altering the original object stored in S3. This is useful for applications that need to present data in different formats or with additional processing.
3. **Integration with Existing S3 Buckets:**
    
    - You can add S3 Object Lambda access points to your existing S3 buckets. These access points let you define Lambda functions that process data on retrieval, allowing you to easily integrate with your existing storage solutions.