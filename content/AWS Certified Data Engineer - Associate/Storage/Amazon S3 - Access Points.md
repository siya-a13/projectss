---
longform:
  format: single
  title: Amazon S3 - Access Points
title: Amazon S3 - Access Points
---
**Amazon S3 Access Points** are a feature that simplify managing access to S3 buckets. They provide a way to create specific access permissions for applications that need to interact with your S3 bucket, allowing you to manage access at a granular level.

![[s3-access-point.png]]

### Key Concepts of S3 Access Points:

1. **Access Points Overview**:
    
    - An S3 Access Point is associated with a single bucket, and each access point has a unique DNS name that applications use to access the bucket.
    - You can create multiple access points for a single S3 bucket, each with its own permissions and network controls.
2. **Purpose**:
    
    - Simplifies access management for large-scale S3 buckets that serve different applications or users.
    - Allows you to define specific policies and network controls per access point, rather than using bucket policies or IAM policies alone.
3. **Access Point Policies**:
    
    - Each access point can have its own resource policy, specifying who can access the data and under what conditions.
    - Policies can control access based on user identity, IP address, VPC, or other conditions.
4. **VPC Integration**:
    
    - You can create VPC-only access points, restricting access to S3 data to only those requests coming from a specific VPC.
    - This is particularly useful for controlling access from within your AWS environment and securing your data from external access.
5. **DNS Naming**:
    
    - Each access point gets a unique DNS name, which is used in place of the bucket name in S3 requests. This helps in isolating access paths to your bucket.
    - Example: If your bucket name is `my-bucket` and your access point is named `my-access-point`, the DNS name might look like `my-access-point-123456789012.s3-accesspoint.region.amazonaws.com`.
6. **Use Cases**:
    
    - **Isolated Environments**: Providing different applications or teams access to the same bucket without giving them access to the entire bucket or needing complex bucket policies.
    - **Network Control**: Restricting access to S3 buckets to certain VPCs or specific IP ranges, improving security by enforcing network-based access restrictions.
    - **Delegated Permissions**: Allowing you to delegate access controls to different teams or departments by providing them with access points, rather than managing permissions centrally.
7. **Lifecycle Management**:
    
    - Access points can also be used with S3 features like Object Lock, versioning, and lifecycle policies, allowing you to manage data according to your organization's requirements.

### Example Use Case:

Suppose you have a data lake stored in an S3 bucket, and different teams need access to different parts of this data. You can create multiple access points with distinct policies:

- **Data Engineering Access Point**: Grants full access to all data.
- **Analytics Team Access Point**: Restricts access to only certain prefixes in the bucket.
- **External Partner Access Point**: Allows read-only access from specific IP addresses or a VPC.

This approach provides a more flexible, secure, and scalable way to manage S3 bucket access in complex environments.