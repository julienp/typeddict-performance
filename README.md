# MyPy Performance

This example is slow to typecheck using mypy.

`pulumi_types.py` contains simplified types to model a pulumi input, from https://github.com/pulumi/pulumi/blob/0f191ee8695b7716bd9a334074cc40d4c4c5e4f9/sdk/python/lib/pulumi/output.py#L54

`k8s_types.py` contains types using TypedDict that model a K8S deployment.
