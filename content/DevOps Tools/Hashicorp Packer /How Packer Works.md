---
longform:
  format: single
  title: How Packer Works
title: How Packer Works
---
**Packer** is an open-source tool developed by HashiCorp that is used to automate the creation of machine images. It allows you to define and build images for various platforms, such as AWS, Azure, Google Cloud, VirtualBox, Docker, and more, using a single, consistent configuration. Packer is particularly useful in DevOps workflows to ensure that infrastructure environments are consistent and reproducible.

### How Packer Works

Packer uses a JSON or HCL (HashiCorp Configuration Language) configuration file to define the build process. This file specifies the base image, the provisioners (scripts or tools to install software and perform configuration), and the output format or image that will be created.

Here's a breakdown of the Packer workflow:

1. **Template Configuration**: You define a Packer template that includes various components like builders, provisioners, and post-processors.
    
2. **Builders**: Builders are responsible for creating the initial image. This could be an AWS AMI, a Google Cloud image, a Docker image, etc. Each builder requires specific parameters like source image, instance type, region, etc.
    
3. **Provisioners**: Once the image is built, provisioners are used to install and configure software within the image. This can be done using shell scripts, Ansible, Chef, Puppet, etc.
    
4. **Post-Processors**: These are optional and are used to perform additional actions on the image after it has been created. For example, you could compress the image, upload it to a cloud storage, or create a Vagrant box from it.
    
5. **Image Creation**: Packer orchestrates the process, starting with the base image, applying provisioners, and then outputting the final image.
    
6. **Artifact Storage**: The final image is stored in the specified destination, like an AWS AMI, Docker registry, etc.

### Example Packer Configuration

Here's a simple example of a Packer configuration that creates an AWS AMI:

```
{
  "variables": {
    "aws_region": "us-west-2",
    "aws_instance_type": "t2.micro",
    "ami_name": "my-custom-ami"
  },
  "builders": [
    {
      "type": "amazon-ebs",
      "region": "{{user `aws_region`}}",
      "instance_type": "{{user `aws_instance_type`}}",
      "source_ami": "ami-0c55b159cbfafe1f0",
      "ssh_username": "ubuntu",
      "ami_name": "{{user `ami_name`}}"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "sudo apt-get update",
        "sudo apt-get install -y nginx"
      ]
    }
  ]
}
```

### Explanation of Components

1. **Variables**: Allows you to define reusable values that can be referenced in the configuration. Here, `aws_region`, `aws_instance_type`, and `ami_name` are defined as variables.
    
2. **Builders**: In this example, the `amazon-ebs` builder is used to create an Amazon Elastic Block Store (EBS)-backed AMI. The `region`, `instance_type`, and `source_ami` are specified, along with the SSH username and the name of the final AMI.
    
3. **Provisioners**: A shell provisioner is used here to update the package list and install Nginx on the image.
    
4. **Post-Processors**: There are no post-processors in this example, but they could be added to perform actions like compressing the image or uploading it to a repository.

### Running Packer

To run the above configuration, save it as `example.json` and execute the following command:

```
packer build example.json
```