from aws_cdk import core as cdk
from _constructs.vpc_construct import VpcConstruct


class VpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc_construct = VpcConstruct(self, 'VpcConstruct')

    @property
    def vpc(self):
        return self.vpc_construct.vpc
