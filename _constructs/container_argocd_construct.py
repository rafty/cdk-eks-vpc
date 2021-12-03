from constructs import Construct
from aws_cdk import aws_eks


class ContainerToolConstruct(Construct):
    def __init__(self,
                 scope: Construct,
                 id: str,
                 cluster: aws_eks.Cluster,
                 ) -> None:
        super().__init__(scope, id)

        self._cluster = cluster

        cluster.add_helm_chart(
            id='ArgoCD',
            repository='https://argoproj.github.io/argo-helm',
            chart='argo-cd',
            release='my-argocd',
            namespace='argocd',
        )
