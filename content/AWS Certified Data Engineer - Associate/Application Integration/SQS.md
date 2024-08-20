---
longform:
  format: single
  title: SQS
title: SQS
---
**Amazon Simple Queue Service (SQS)** is a fully managed message queuing service that enables decoupling and scaling of microservices, distributed systems, and serverless applications. It helps to buffer and manage the flow of messages between producers (components that generate data) and consumers (components that process data), ensuring that they can operate independently and at their own pace.

![[SQS.png]]

### AWS SQS Message Size Limitations

- **Standard Queue** and **FIFO Queue**: By default, SQS messages can be up to 256 KB in size (including both the message body and any metadata or attributes).

### Key Features of AWS SQS:

- **Message Queues**:
    
    - **Standard Queue**: Offers unlimited throughput, at-least-once delivery, and best-effort ordering. This means that messages might be delivered more than once and out of order.
    - **FIFO Queue**: (First-In-First-Out) ensures that messages are processed exactly once and in the exact order they are sent. FIFO queues have a limited throughput compared to standard queues.
    
- **Decoupling Components**: SQS allows different parts of an application to communicate with each other asynchronously, enabling each part to operate independently and at its own pace.
    
- **Scalability**: SQS automatically scales to handle an increase in the volume of messages without the need for any manual intervention.
    
- **Security**: Messages in SQS are encrypted at rest using AWS Key Management Service (KMS), and you can use policies to control who can send and receive messages.
    
- **Reliability**: SQS stores messages redundantly across multiple Availability Zones (AZs) to ensure durability.
    
- **Message Visibility Timeout**: This is the period during which a message is invisible to other consumers after it has been retrieved by a consumer. If the message isn't deleted within this time, it becomes visible again and can be received by another consumer. This ensures that if a task fails, the message can be processed again.
    
- **Long Polling and Short Polling**:
    
    - **Short Polling**: Immediately returns a response with any available messages or an empty response if none are available.
    - **Long Polling**: Waits until a message is available or until a timeout is reached, reducing the number of empty responses and potentially lowering costs.
    
- **Dead-Letter Queues**: SQS can move messages that can't be processed successfully after a specified number of attempts to a dead-letter queue for further analysis or debugging.
    
- **Delayed Delivery**: Messages can be delayed for a specified amount of time before they are available to be processed.
    
- **Message Attributes**: SQS allows you to attach metadata to messages in the form of attributes, which can be used by consumers to filter messages or process them based on specific criteria.

### Common Use Cases:

- **Decoupling Microservices**: SQS allows microservices to communicate asynchronously, reducing the dependency between them and improving the overall fault tolerance of the system.

- **Batch Processing**: SQS can be used to collect tasks and then process them in batches, which is useful in data processing pipelines.

- **Load Leveling**: It helps in managing the load on a service by buffering requests and smoothing out spikes.

- **Event-Driven Architecture**: SQS can trigger processes based on events, making it useful for building event-driven applications.

SQS is widely used for building scalable, fault-tolerant, and highly available systems in the cloud.