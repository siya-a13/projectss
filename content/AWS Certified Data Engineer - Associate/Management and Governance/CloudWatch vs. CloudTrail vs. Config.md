---
longform:
  format: single
  title: CloudWatch vs. CloudTrail vs. Config
title: CloudWatch vs. CloudTrail vs. Config
---
Amazon CloudWatch, AWS CloudTrail, and AWS Config are all monitoring and logging tools provided by AWS, but they serve different purposes and are used for different types of monitoring and auditing within your AWS environment.

### **Amazon CloudWatch**

**Purpose**: Monitoring and observability.

- **Use Case**: CloudWatch is used to monitor the performance and operational health of AWS resources and applications. It collects and tracks metrics, logs, and events, providing visibility into resource utilization, application performance, and operational health.
    
- **Features**:
    - **Metrics Monitoring**: Collects and tracks various metrics from AWS services (e.g., CPU utilization of EC2 instances, latency of ELBs).
    - **Log Monitoring**: Aggregates and monitors log files from AWS resources, custom applications, and on-premises systems.
    - **Alarms and Notifications**: Set alarms based on thresholds for metrics and logs, and receive notifications via SNS (Simple Notification Service).
    - **Dashboards**: Create custom dashboards to visualize metrics and logs for better monitoring and insights.

- **Example**: Monitor the CPU utilization of an EC2 instance and set up an alarm to notify you when it exceeds a certain threshold.

### **AWS CloudTrail**

**Purpose**: Audit and governance.

- **Use Case**: CloudTrail is used to log, monitor, and retain account activity related to actions across your AWS infrastructure. It provides visibility into API calls and actions performed by users, services, and roles, making it essential for security auditing and compliance.
    
- **Features**:
    
    - **Event Logging**: Captures detailed event logs of API calls made in your AWS account, including the identity of the caller, time of the call, and parameters passed.
    - **Multi-Region and Multi-Account Support**: Aggregate logs across multiple regions and accounts.
    - **Event History**: View a history of AWS API calls to understand changes to resources or investigate security incidents.

- **Example**: Track and log all API calls made to create, modify, or delete S3 buckets to ensure compliance and audit trails.

### **AWS Config**

**Purpose**: Configuration monitoring and compliance.

- **Use Case**: AWS Config is used to assess, audit, and evaluate the configurations of AWS resources. It continuously monitors and records AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations.
    
- **Features**:
    
    - **Resource Inventory**: Maintains an inventory of all your AWS resources and their configuration details.
    - **Configuration History**: Records and tracks changes to resource configurations over time.
    - **Compliance Management**: Evaluate the configuration of resources against policies or best practices to ensure compliance.
    - **Remediation**: Automate actions to bring resources back into compliance if they drift from the desired state.

- **Example**: Ensure that all EC2 instances have a specific tag (e.g., "Environment: Production") and automatically remediate instances that do not comply.