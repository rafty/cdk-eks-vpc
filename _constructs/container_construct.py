import os
import glob
import yaml
from aws_cdk import core as cdk
from aws_cdk import aws_eks


class ContainerConstruct(cdk.Construct):
    def __init__(self,
                 scope: cdk.Construct,
                 id: str,
                 cluster: aws_eks.Cluster,
                 ) -> None:
        super().__init__(scope, id)

        self._cluster = cluster
        self.add_manifests_from_yaml('./manifests/')

    def add_manifests_from_yaml(self, directory: str):

        manifest_files = self.get_manifest_files(directory)

        for manifest_file in manifest_files:
            name = self.file_name_without_extension(manifest_file)
            docs = self.load_docs_from_manifest_file(manifest_file)

            previous_k8s_resource = None
            for i, doc in enumerate(docs):
                k8s_resource = self._cluster.add_manifest(f'{name}_{i}', doc)
                if previous_k8s_resource:
                    k8s_resource.node.add_dependency(previous_k8s_resource)
                previous_k8s_resource = k8s_resource

    @staticmethod
    def file_name_without_extension(manifest_file_path):
        file_name = os.path.basename(manifest_file_path)
        file_name_without_ext = os.path.splitext(file_name)[0]
        return file_name_without_ext

    @staticmethod
    def load_docs_from_manifest_file(manifest_file):
        with open(manifest_file, 'r', encoding='utf-8') as stream:
            manifest_docs = list(
                yaml.load_all(stream, Loader=yaml.FullLoader))
        return manifest_docs

    @staticmethod
    def get_manifest_files(directory: str) -> list:
        files = glob.glob(directory+'*.yaml')
        return files
