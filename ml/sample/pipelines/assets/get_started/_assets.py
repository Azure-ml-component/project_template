# THIS IS AN AUTO GENERATED FILE.
# PLEASE DO NOT MODIFY MANUALLY.
# Components included in this generated file:
#  - microsoft.com.azureml.samples.compare_2_models::0.0.2
#  - samples.evaluate::0.0.5
#  - samples.mpi_train::0.0.7
#  - samples.score::0.0.4
#  - samples.train::0.0.5
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


class _DistributedComponentRunsettingDockerConfiguration:
    """Docker configuration section specify the docker runtime properties for the Run.."""
    arguments: Union[str, list]
    """Extra arguments to the Docker run command. The extra docker container options like --cpus=2, --memory=1024"""
    shm_size: str
    """The size of the Docker container's shared memory block. If not set, the default 2g is used."""


class _DistributedComponentRunsettingEnvironment:
    """Environment section set runtime environment."""
    conda: str
    """Defines conda dependencies"""
    docker: str
    """Defines settings to customize the Docker image built to the environment's specifications."""
    os: str
    """Defines the operating system the component running on. Could be Windows or Linux. Defaults to Linux if not specified. (enum: ['Windows', 'Linux'])"""


class _DistributedComponentRunsettingResourceLayout:
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    instance_count: int
    """Number of instances in the compute target used for training. (min: 1)"""
    instance_type: str
    """Instance type used for training."""
    node_count: int
    """Number of nodes in the compute target used for training. (min: 1)"""
    process_count_per_instance: int
    """Number of processes per instance. If greater than 1, mpi distributed job will be run. Only AmlCompute compute target is supported for distributed jobs. (min: 1, max: 8)"""


class _DistributedComponentRunsettingTargetSelector:
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


class _DistributedComponentRunsetting:
    """Run setting configuration for DistributedComponent"""
    environment_variables: Union[str, dict]
    """Environment variables can be used to specify environment variables to be passed. It is a dictionary of environment name to environment value mapping. User can use this to adjust some component runtime behavior which is not exposed as component parameter, e.g. enable some debug switch."""
    priority: int
    """The priority of a job which is a integer. For AmlK8s Compute, User can set it to 100~200. Any value larger than 200 or less than 100 will be treated as 200. For Aml Compute, User can set it to 1~1000. Any value larger than 1000 or less than 1 will be treated as 1000."""
    target: str
    """The compute target to use"""
    docker_configuration: _DistributedComponentRunsettingDockerConfiguration
    """Docker configuration section specify the docker runtime properties for the Run.."""
    environment: _DistributedComponentRunsettingEnvironment
    """Environment section set runtime environment."""
    resource_layout: _DistributedComponentRunsettingResourceLayout
    """resource section controls the number of nodes, cpus, gpus the job will consume."""
    target_selector: _DistributedComponentRunsettingTargetSelector
    """Specify desired target properties, instead of specifying a cluster name. When target is set, target_selector will be ignored."""


class _MicrosoftComAzuremlSamplesCompare2ModelsInput:
    model1: Input = None
    """The first model to compare with(optional)"""
    eval_result1: Input = None
    """The evaluation result of first model(optional)"""
    model2: Input = None
    """The second model to compare(optional)"""
    eval_result2: Input = None
    """The evaluation result of second model(optional)"""


class _MicrosoftComAzuremlSamplesCompare2ModelsOutput:
    best_model: Output = None
    """The better model among the two"""
    best_result: Output = None
    """The better model evaluation result among the two"""


class _MicrosoftComAzuremlSamplesCompare2ModelsComponent(Component):
    inputs: _MicrosoftComAzuremlSamplesCompare2ModelsInput
    outputs: _MicrosoftComAzuremlSamplesCompare2ModelsOutput
    runsettings: _CommandComponentRunsetting


_microsoft_com_azureml_samples_compare_2_models = None


def microsoft_com_azureml_samples_compare_2_models(
    model1: Path = None,
    eval_result1: Path = None,
    model2: Path = None,
    eval_result2: Path = None,
) -> _MicrosoftComAzuremlSamplesCompare2ModelsComponent:
    """A dummy comparison module takes two models as input and outputs the better one
    
    :param model1: The first model to compare with(optional)
    :type model1: Path
    :param eval_result1: The evaluation result of first model(optional)
    :type eval_result1: Path
    :param model2: The second model to compare(optional)
    :type model2: Path
    :param eval_result2: The evaluation result of second model(optional)
    :type eval_result2: Path
    :output best_model: The better model among the two
    :type: best_model: Output
    :output best_result: The better model evaluation result among the two
    :type: best_result: Output
    """
    global _microsoft_com_azureml_samples_compare_2_models
    if _microsoft_com_azureml_samples_compare_2_models is None:
        _microsoft_com_azureml_samples_compare_2_models = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/microsoft_com_azureml_samples_compare_2_models/0.0.2/compare2.yaml")
    return _microsoft_com_azureml_samples_compare_2_models(
            model1=model1,
            eval_result1=eval_result1,
            model2=model2,
            eval_result2=eval_result2,)


class _SamplesEvaluateInput:
    scoring_result: Input = None
    """Scoring result file in TSV format"""


class _SamplesEvaluateOutput:
    eval_output: Output = None
    """Evaluation result"""


class _SamplesEvaluateComponent(Component):
    inputs: _SamplesEvaluateInput
    outputs: _SamplesEvaluateOutput
    runsettings: _CommandComponentRunsetting


_samples_evaluate = None


def samples_evaluate(
    scoring_result: Path = None,
) -> _SamplesEvaluateComponent:
    """A dummy evaluate module
    
    :param scoring_result: Scoring result file in TSV format
    :type scoring_result: Path
    :output eval_output: Evaluation result
    :type: eval_output: Output
    """
    global _samples_evaluate
    if _samples_evaluate is None:
        _samples_evaluate = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/samples_evaluate/0.0.5/eval.yaml")
    return _samples_evaluate(
            scoring_result=scoring_result,)


class _SamplesMpiTrainInput:
    training_data: Input = None
    """Training data organized in the torchvision format/structure"""
    max_epochs: int = None
    """Maximum number of epochs for the training"""
    learning_rate: float = 0.01
    """Learning rate, default is 0.01"""


class _SamplesMpiTrainOutput:
    model_output: Output = None
    """The output model"""


class _SamplesMpiTrainComponent(Component):
    inputs: _SamplesMpiTrainInput
    outputs: _SamplesMpiTrainOutput
    runsettings: _DistributedComponentRunsetting


_samples_mpi_train = None


def samples_mpi_train(
    training_data: Path = None,
    max_epochs: int = None,
    learning_rate: float = 0.01,
) -> _SamplesMpiTrainComponent:
    """A dummy component to show how to describe MPI component with custom component spec.
    
    :param training_data: Training data organized in the torchvision format/structure
    :type training_data: Path
    :param max_epochs: Maximum number of epochs for the training
    :type max_epochs: int
    :param learning_rate: Learning rate, default is 0.01
    :type learning_rate: float
    :output model_output: The output model
    :type: model_output: Output
    """
    global _samples_mpi_train
    if _samples_mpi_train is None:
        _samples_mpi_train = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/samples_mpi_train/0.0.7/mpi_train.distributed.component.yaml")
    return _samples_mpi_train(
            training_data=training_data,
            max_epochs=max_epochs,
            learning_rate=learning_rate,)


class _SamplesScoreInput:
    model_input: Input = None
    """Zipped model file"""
    test_data: Input = None
    """Test data organized in the torchvision format/structure"""


class _SamplesScoreOutput:
    score_output: Output = None
    """The scoring result in TSV"""


class _SamplesScoreComponent(Component):
    inputs: _SamplesScoreInput
    outputs: _SamplesScoreOutput
    runsettings: _CommandComponentRunsetting


_samples_score = None


def samples_score(
    model_input: Path = None,
    test_data: Path = None,
) -> _SamplesScoreComponent:
    """A dummy scoring module
    
    :param model_input: Zipped model file
    :type model_input: Path
    :param test_data: Test data organized in the torchvision format/structure
    :type test_data: Path
    :output score_output: The scoring result in TSV
    :type: score_output: Output
    """
    global _samples_score
    if _samples_score is None:
        _samples_score = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/samples_score/0.0.4/score.yaml")
    return _samples_score(
            model_input=model_input,
            test_data=test_data,)


class _SamplesTrainInput:
    training_data: Input = None
    """Training data organized in the torchvision format/structure"""
    max_epochs: int = None
    """Maximum number of epochs for the training"""
    learning_rate: float = 0.01
    """Learning rate, default is 0.01"""


class _SamplesTrainOutput:
    model_output: Output = None
    """The output model"""


class _SamplesTrainComponent(Component):
    inputs: _SamplesTrainInput
    outputs: _SamplesTrainOutput
    runsettings: _CommandComponentRunsetting


_samples_train = None


def samples_train(
    training_data: Path = None,
    max_epochs: int = None,
    learning_rate: float = 0.01,
) -> _SamplesTrainComponent:
    """A dummy training module
    
    :param training_data: Training data organized in the torchvision format/structure
    :type training_data: Path
    :param max_epochs: Maximum number of epochs for the training
    :type max_epochs: int
    :param learning_rate: Learning rate, default is 0.01
    :type learning_rate: float
    :output model_output: The output model
    :type: model_output: Output
    """
    global _samples_train
    if _samples_train is None:
        _samples_train = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/samples_train/0.0.5/train.yaml")
    return _samples_train(
            training_data=training_data,
            max_epochs=max_epochs,
            learning_rate=learning_rate,)


# No datasets class is generated.
