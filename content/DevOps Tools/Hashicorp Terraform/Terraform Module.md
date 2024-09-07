---
longform:
  format: single
  title: Terraform Module
title: Terraform Module
---
Terraform modules are a fundamental concept in Terraform, a popular infrastructure-as-code tool developed by HashiCorp. Modules help organize and reuse code for creating and managing infrastructure resources. Here’s a breakdown of what Terraform modules are and how they work:

![[module.png]]

### What is a Terraform Module?

1. **Definition**:
    
    - A Terraform module is a container for multiple resources that are used together. It allows you to encapsulate and abstract a set of resources and their configuration into a reusable and manageable unit.
2. **Structure**:
    
    - A module typically contains:
        - **`main.tf`**: Defines the primary resources and their configurations.
        - **`variables.tf`**: Specifies the input variables for the module.
        - **`outputs.tf`**: Defines the output values that other configurations can use.
        - **`providers.tf`**: (Optional) Specifies providers needed by the module.
3. **Types of Modules**:
    
    - **Root Module**: The configuration in the main working directory where you execute `terraform apply`. This module includes all the Terraform configurations in that directory.
    - **Child Modules**: Modules that are called by other modules (which can be either root or other child modules). These modules are usually located in separate directories and referenced by the root or other modules.

### Benefits of Using Modules

1. **Reusability**:
    
    - Modules allow you to reuse code across multiple configurations. For example, if you have a module to create an AWS VPC, you can use that same module in different environments (like staging and production) with different configurations.
2. **Maintainability**:
    
    - By encapsulating related resources into a module, you can manage and update them in one place. This makes your Terraform configuration more modular and easier to maintain.
3. **Organization**:
    
    - Modules help in organizing complex configurations by breaking them into smaller, more manageable pieces. This improves readability and makes it easier to understand and manage your infrastructure.
4. **Consistency**:
    
    - Using modules helps ensure consistent configurations across different environments and projects. Since the module code is reused, you reduce the risk of discrepancies and errors.

### How to Use a Module

1. **Create a Module**:
    
    - Define a module by creating a directory with the necessary `.tf` files (e.g., `main.tf`, `variables.tf`, `outputs.tf`).
2. **Call a Module**:
    
    - Use the `module` block in your root configuration to call and use the module. For example:
    
```
module "my_vpc" {
  source = "./modules/vpc"
  vpc_name = "my-vpc"
  cidr_block = "10.0.0.0/16"
}
```

- **Source**:
    
    - The `source` argument in the `module` block specifies the location of the module. This can be a local path (like `./modules/vpc`), a Git repository, or a Terraform Registry.
- **Pass Variables**:
    
    - Provide values for the module’s input variables when calling it. These variables are defined in `variables.tf` within the module.
- **Use Outputs**:
    
    - Access the outputs defined in the module by referencing them in your root configuration. For example:

```
output "vpc_id" {
  value = module.my_vpc.vpc_id
}
```

### Example

Here's a simple example of how you might define and use a module:

**Module Directory (`modules/vpc/main.tf`)**:

```
resource "aws_vpc" "this" {
  cidr_block = var.cidr_block
  tags = {
    Name = var.vpc_name
  }
}
```

**Module Variables (`modules/vpc/variables.tf`)**:

```
variable "vpc_name" {
  type = string
}

variable "cidr_block" {
  type = string
}
```

**Root Configuration (`main.tf`)**:

```
module "my_vpc" {
  source     = "./modules/vpc"
  vpc_name   = "my-vpc"
  cidr_block = "10.0.0.0/16"
}
```

In summary, Terraform modules are a powerful way to structure and manage your infrastructure code, allowing for better organization, reusability, and maintainability.