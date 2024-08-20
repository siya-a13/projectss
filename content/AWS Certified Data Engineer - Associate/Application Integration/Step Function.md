---
longform:
  format: single
  title: Step Function
title: Step Function
---
AWS Step Functions is a serverless orchestration service that allows you to coordinate multiple AWS services into flexible workflows, enabling complex operations to be managed and executed in a reliable and scalable manner. These workflows are defined using a JSON-based Amazon States Language (ASL).

![[step-function.png]]
## Key Concepts of AWS Step Functions

**State Machines**: A state machine is a workflow definition in Step Functions, which consists of a series of steps, known as states, that define how data is passed between them. You can think of it as a flowchart that controls the execution of your application's logic.

**States**: Each step in a workflow is referred to as a state. AWS Step Functions supports different types of states, each with its own behavior. Common state types include:

- **Task State**: Executes a task, such as invoking a Lambda function, an AWS Batch job, or integrating with other AWS services.
- **Pass State**: Passes its input to its output, without performing any work. Useful for testing or modifying data in the workflow.
- **Choice State**: Adds branching logic to your workflow, allowing for conditional execution of different paths based on the input data.
- **Wait State**: Pauses the execution for a specified amount of time or until a specific time is reached.
- **Succeed State**: Marks the successful completion of the state machine.
- **Fail State**: Terminates the state machine execution with a failure, allowing you to handle errors.
- **Parallel State**: Branches out into multiple paths that run in parallel, which can then be joined back together.
- **Map State**: Executes the same set of steps for each element of an input array.
- **Catch and Retry**: Not a state per se, but mechanisms to handle errors and retries within states.

**Transitions**: These are the rules that determine which state should be executed next, based on the result of the previous state.

**Execution**: When you start a state machine, an execution is created. Executions can be tracked and managed to see the current state, history, and outcome of the workflow.