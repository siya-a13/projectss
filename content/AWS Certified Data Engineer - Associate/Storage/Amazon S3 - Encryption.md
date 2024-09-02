---
longform:
  format: single
  title: Amazon S3 - Encryption
---
### 1. **S3 Encryption Overview**

Amazon S3 (Simple Storage Service) provides various encryption methods to protect your data at rest. These methods can be broadly categorized into **Server-Side Encryption (SSE)** and **Client-Side Encryption (CSE)**.

### 2. **Server-Side Encryption (SSE)**

With Server-Side Encryption, Amazon S3 handles the encryption and decryption process automatically. There are three options under SSE:

#### a. **S3 Server-Side Encryption with S3 Managed Keys (SSE-S3)**

- **Description:** AWS manages the encryption keys entirely. Each object is encrypted with a unique key. Amazon S3 then encrypts this unique key with a master key that it regularly rotates.
- **Key Management:** Handled by AWS.
- **Use Case:** When you want encryption to be managed entirely by AWS with no additional configuration.

#### b. **S3 Server-Side Encryption with AWS KMS Managed Keys (SSE-KMS)**

- **Description:** Similar to SSE-S3, but AWS Key Management Service (KMS) manages the keys. This option allows more control over the keys and auditing capabilities.
- **Key Management:** Handled by AWS KMS, which offers features like key rotation and fine-grained access control.
- **Use Case:** When you need tighter control over encryption keys, such as defining access control policies and auditing key usage.

#### c. **S3 Server-Side Encryption with Customer-Provided Keys (SSE-C)**

- **Description:** You provide your own encryption keys, and AWS uses them to encrypt your data. AWS does not store these keys.
- **Key Management:** You manage and provide the encryption keys with each request. AWS only uses them temporarily to perform encryption/decryption.
- **Use Case:** When you want complete control over the encryption keys but still want AWS to manage the encryption process.

### 3. **Client-Side Encryption (CSE)**

In Client-Side Encryption, data is encrypted before it is uploaded to S3. This means that encryption and decryption occur on the client-side, and the encrypted data is stored in S3.

#### a. **S3 Client-Side Encryption with AWS KMS Managed Keys**

- **Description:** You use AWS SDKs to encrypt your data before uploading it to S3. The encryption keys are managed by AWS KMS.
- **Key Management:** AWS KMS manages the keys, but encryption and decryption happen on the client side.
- **Use Case:** When you need to ensure that data is encrypted before leaving your environment, but still want AWS to manage the keys.

#### b. **S3 Client-Side Encryption with Customer-Provided Keys**

- **Description:** You manage your encryption keys entirely and use them to encrypt data before uploading it to S3. The data is already encrypted when it reaches S3.
- **Key Management:** Fully managed by you. AWS has no access to the keys.
- **Use Case:** When you need full control over the encryption process and want to ensure that AWS has no access to the unencrypted data or keys.

### Summary of Use Cases:

- **SSE-S3**: Best for default encryption with minimal management overhead.
- **SSE-KMS**: Ideal for use cases requiring strict access control and audit logging.
- **SSE-C**: Suitable when you need AWS to encrypt data with your provided keys.
- **CSE**: Required when encryption must happen entirely within your control, especially when data must remain encrypted before it reaches AWS infrastructure.