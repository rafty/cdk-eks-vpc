#!/usr/bin/env python3
import os
import aws_cdk  as cdk
from stacks.eks_stack import EksStack
from stacks.vpc_stack import VpcStack
from stacks.container_stack import ContainerStack


environment = cdk.Environment(
    account=os.environ.get('CDK_DEPLOY_ACCOUNT', os.environ['CDK_DEFAULT_ACCOUNT']),
    region=os.environ.get('CDK_DEPLOY_REGION', os.environ['CDK_DEFAULT_REGION']),
)

app = cdk.App()

vpc_stack = VpcStack(app, "VpcStack", env=environment)

eks_stack = EksStack(app, "EksStack", vpc=vpc_stack.vpc, env=environment)
eks_stack.add_dependency(vpc_stack)

container_stack = ContainerStack(app, "ContainerStack", cluster=eks_stack.cluster, env=environment)
container_stack.add_dependency(eks_stack)

app.synth()
