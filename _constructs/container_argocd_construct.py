from aws_cdk import core as cdk
from aws_cdk import aws_eks


class ContainerToolConstruct(cdk.Construct):
    def __init__(self,
                 scope: cdk.Construct,
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
