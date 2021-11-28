from aws_cdk import core as cdk
from aws_cdk import aws_iam
from aws_cdk import aws_eks
from aws_cdk import aws_ec2
from _constructs.eks_cluster_construct import EksClusterConstruct


class EksStack(cdk.Stack):

    def __init__(self,
                 scope: cdk.Construct,
                 construct_id: str,
                 vpc: aws_ec2.Vpc,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._eks_cluster_construct = EksClusterConstruct(
            self, 'EksClusterConstruct', vpc)

        # # Create owner role for EKS Cluster
        # owner_role = aws_iam.Role(
        #     scope=self,
        #     id='EksClusterOwnerRole',
        #     role_name='EksClusterOwnerRole',
        #     assumed_by=aws_iam.AccountRootPrincipal()
        # )
        #
        # # Creating Cluster with EKS
        # self._cluster = aws_eks.Cluster(
        #     scope=self,
        #     id='EksCluster',
        #     cluster_name='EksCluster',
        #     output_cluster_name=True,
        #     version=aws_eks.KubernetesVersion.V1_21,
        #     endpoint_access=aws_eks.EndpointAccess.PUBLIC,
        #     vpc=vpc,
        #     vpc_subnets=vpc.private_subnets,
        #     masters_role=owner_role,
        #     default_capacity=2,
        # )

    @property
    def cluster(self):
        return self._eks_cluster_construct.cluster
