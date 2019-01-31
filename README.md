---
layout: docs
title: Hooks
---

# Overview

The purpose of this hook is to enable and disable the stack
termination protection.

A common use case is integrate this hook with your CI/CD
system. In that case you may need to execute this on every
build.  That's where the
[sceptre-date-resolver](https://github.com/zaro0508/sceptre-date-resolver)
may help. It will allow you to force AWS to execute the template on
on every commit.


## Available Hooks

### StackTermination

Enables and disables stack termination.

Syntax:

```yaml
parameter|sceptre_user_data:
    <name>: !stack_termination_protection 'enabled'/'disabled'
```

Example:

Enable stack termination protection after creating stack
and disable stack termination protection before stack deletion:
```
hooks:
  after_create:
    - !stack_termination_protection 'enabled'
  before_delete:
    - !stack_termination_protection 'disabled'
```
