from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_eks
from _constructs.container_construct import ContainerConstruct
from _constructs.container_argocd_construct import ContainerToolConstruct


class ContainerStack(Stack):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 cluster: aws_eks.Cluster,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ArgoCD
        self._container_tool_construct = ContainerToolConstruct(
            self, 'ContainerToolConstruct', cluster)
        # eginx
        self._container_construct = ContainerConstruct(
            self, 'ContainerConstruct', cluster)
