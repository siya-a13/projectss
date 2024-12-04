---
longform:
  format: single
  title: Task Discovery
title: Celery Task Decorators Perameters
---
## Introduction

`@shared_task` enables you to create Celery tasks that are decoupled from the Celery app instance, making them portable across different projects or apps. This also eliminates the need to import the Celery app instance, reducing boilerplate code and making task definitions simpler.

Before defining tasks, consider the following:

- **Task execution frequency**: Should the task run multiple times or just once?
- **Retry policy**: Does the task need to retry in case of failure? If so, how many times?
- **Task result**: Is storing the task's result required?
- **Task status**: Do you need to track the task's status externally?
- **Task start information**: Do you need to know when the task actually starts?

Answering these questions will guide you in choosing the appropriate parameters for the `@shared_task` decorator.

### Task Naming Advice

Always explicitly name your tasks to avoid name clashes between different parts of the app or with other libraries. For example:

```
@shared_task(name="api_check_availability")
def check_availability():
    pass
```

### Importing Tasks

Tasks can be imported and called using the `delay()` or `apply_async()` methods:

```
from our_api.tasks import check_availability

check_availability.delay()
check_availability.apply_async()
```

To avoid circular import issues, especially when tasks are invoked from other apps, you can call the task by its name:

```
# In models.py
from celery import current_app
from django.db import transaction

class Post(models.Model):
    title = models.CharField(max_length=255)

    def generate_og_images(self):
        pass

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        transaction.on_commit(lambda: current_app.send_task("content_generate_og_images", kwargs={"post_pk": self.pk}))

```

In this example, the task `content_generate_og_images` is sent by name to avoid circular imports.

## Defining Tasks

### The Simplest Shared Task

If the task result is not important, and you want to reduce the performance impact, you can define the task like this:

```
@shared_task(
    name="simple_task",
    ignore_result=True
)
def simple_task():
    pass

```

Here, `ignore_result=True` prevents the task from connecting to the result backend, and there is no retry strategy as `bind=False`.

### Shared Task with Retry Policy

To implement a retry policy for tasks, such as calling an external API, you can use parameters like `max_retries`, `autoretry_for`, and `retry_backoff`:

```
@shared_task(
    name="read_from_external_api",
    bind=True,
    acks_late=True,
    autoretry_for=(Exception,),
    max_retries=5,
    retry_backoff=True,
    retry_backoff_max=500,
    retry_jitter=True
)
def read_from_external_api(url):
    result = requests.get(url)
    return result.json()
```

This example retries the task up to 5 times if an exception occurs, with a backoff strategy for retries.

### Shared Task That Must Run At Most Once

For tasks that should only run once (e.g., an expensive API call), you can define a task that acknowledges early to prevent re-execution if the worker fails:

```
@shared_task(
    name="expensive_api_call",
    bind=True,
    acks_late=False,
)
def expensive_api_call(url):
    result = requests.post(url, {})
    return result.json()

```

In this case, `acks_late=False` ensures that the task is acknowledged before completion, and the request will not be retried if the worker fails.

### Sample codebase for practice

#### Link - [Refer](https://github.com/dnisha/Django-celery-redis-on-local.git)







