from constructs import Construct
from aws_cdk import aws_iam
from aws_cdk import aws_eks
from aws_cdk import aws_ec2


class EksClusterConstruct(Construct):
    def __init__(self,
                 scope: Construct,
                 id: str,
                 vpc: aws_ec2.Vpc
                 ) -> None:
        super().__init__(scope, id)

        # Create owner role for EKS Cluster
        owner_role = aws_iam.Role(
            scope=self,
            id='EksClusterOwnerRole',
            role_name='EksClusterOwnerRole',
            assumed_by=aws_iam.AccountRootPrincipal()
        )

        # Creating EKS Cluster
        self._cluster = aws_eks.Cluster(
            scope=self,
            id='EksCluster',
            cluster_name='EksCluster',
            output_cluster_name=True,
            version=aws_eks.KubernetesVersion.V1_21,
            endpoint_access=aws_eks.EndpointAccess.PUBLIC,
            vpc=vpc,
            vpc_subnets=vpc.private_subnets,
            masters_role=owner_role,
            default_capacity=2,
        )

    @property
    def cluster(self):
        return self._cluster
