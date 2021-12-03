from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_ec2
from _constructs.eks_cluster_construct import EksClusterConstruct


class EksStack(Stack):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 vpc: aws_ec2.Vpc,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._eks_cluster_construct = EksClusterConstruct(
            self, 'EksClusterConstruct', vpc)

    @property
    def cluster(self):
        return self._eks_cluster_construct.cluster
