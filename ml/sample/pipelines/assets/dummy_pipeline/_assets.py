# THIS IS AN AUTO GENERATED FILE.
# PLEASE DO NOT MODIFY MANUALLY.
# Components included in this generated file:
#  - data_process::0.0.10
from pathlib import Path
from typing import Union

from azure.ml.component import Component
from azure.ml.component.component import Input, Output


SOURCE_DIRECTORY = Path(__file__).parent / ".."


class _CommandComponentRunsettingDockerConfiguration:
    """Docker configuration section specify the docker runtime properties for the Run.."""
    arguments: Union[str, list]
    """Extra arguments to the Docker run command. The extra docker container options like --cpus=2, --memory=1024"""
    shm_size: str
    """The size of the Docker container's shared memory block. If not set, the default 2g is used."""


class _CommandComponentRunsettingEnvironment:
    """Environment section set runtime environment."""
    conda: str
    """Defines conda dependencies"""
    docker: str
    """Defines settings to customize the Docker image built to the environment's specifications."""
    os: str
    """Defines the operating system the component running on. Could be Windows or Linux. Defaults to Linux if not specified. (enum: ['Windows', 'Linux'])"""


class _CommandComponentRunsettingResourceLayout:
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    instance_count: int
    """Number of instances in the compute target used for training. (min: 1)"""
    instance_type: str
    """Instance type used for training."""
    node_count: int
    """Number of nodes in the compute target used for training. (min: 1)"""


class _CommandComponentRunsettingTargetSelector:
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""
    cluster_block_list: Union[str, list]
    """User specified block list of Cluster."""
    compute_type: str
    """Compute type that target selector could route job to. (enum: ['AmlCompute', 'AmlK8s'])"""
    instance_types: Union[str, list]
    """List of instance_type that job could use. If no instance_type specified, all sizes are allowed."""
    regions: Union[str, list]
    """List of region that would like to submit job to. If no region specified, all regions are allowed."""
    vc_block_list: Union[str, list]
    """User specified block list of VC."""


class _CommandComponentRunsetting:
    """Run setting configuration for CommandComponent"""
    environment_variables: Union[str, dict]
    """Environment variables can be used to specify environment variables to be passed. It is a dictionary of environment name to environment value mapping. User can use this to adjust some component runtime behavior which is not exposed as component parameter, e.g. enable some debug switch."""
    priority: int
    """The priority of a job which is a integer. For AmlK8s Compute, User can set it to 100~200. Any value larger than 200 or less than 100 will be treated as 200. For Aml Compute, User can set it to 1~1000. Any value larger than 1000 or less than 1 will be treated as 1000."""
    target: str
    """The compute target to use"""
    docker_configuration: _CommandComponentRunsettingDockerConfiguration
    """Docker configuration section specify the docker runtime properties for the Run.."""
    environment: _CommandComponentRunsettingEnvironment
    """Environment section set runtime environment."""
    resource_layout: _CommandComponentRunsettingResourceLayout
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    target_selector: _CommandComponentRunsettingTargetSelector
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""


class _DataProcessInput:
    input_data: Input = None
    """path"""


class _DataProcessOutput:
    output_data: Output = None
    """path"""


class _DataProcessComponent(Component):
    inputs: _DataProcessInput
    outputs: _DataProcessOutput
    runsettings: _CommandComponentRunsetting


_data_process = None


def data_process(
    input_data: Path = None,
) -> _DataProcessComponent:
    """data_process
    
    :param input_data: path
    :type input_data: Path
    :output output_data: path
    :type: output_data: Output
    """
    global _data_process
    if _data_process is None:
        _data_process = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/data_process/0.0.10/component.yaml")
    return _data_process(
            input_data=input_data,)


# No datasets class is generated.
