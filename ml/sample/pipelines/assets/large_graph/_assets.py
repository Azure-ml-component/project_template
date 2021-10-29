# THIS IS AN AUTO GENERATED FILE.
# PLEASE DO NOT MODIFY MANUALLY.
# Components included in this generated file:
#  - image_dl_and_convert_to_base64::0.0.1
#  - copy_cosmospath_to_cosmospathtsv::0.0.1
#  - create_generic_tsv_file_for_transformer_on_py3_5::0.0.1
#  - taprioritizedclustering::0.0.1
#  - outings_source_url_id_generator::0.0.1
#  - outings_dominant_type_classifier::0.0.1
#  - outings_ta_sid_mapping_generator::0.0.1
#  - rbf_svm_prediction_ongraph::0.0.1
#  - cosmospathcreator_rundate::0.0.1
#  - namesimilaritybasedcandidatepairgeneration::0.0.1
#  - parameter_to_control_output::0.0.1
#  - outings_cast_one_table_remove_from_other_union_both::0.0.1
#  - is_file_empty_to_controloutput::0.0.1
#  - cosmos_split_1_tsv_to_10::0.0.1
#  - buildentitynamevectors::0.0.1
#  - guid_ta_wiki_sid_prmeasure::0.0.1
#  - cosmos_mirror_with_inputs_and_overwrite::0.0.1
#  - get_image_attractiveness_score_using_base64_encoded_image::0.0.1
#  - flattenclusters::0.0.1
#  - or_conditional_decision_logic::0.0.1
#  - reversegeocoder::0.0.1
#  - outings_remove_columns_from_structured_stream::0.0.1
#  - replacecosmospath::0.0.1
#  - scope_basics_union_intersect_except_sstream::0.0.1
#  - concat_generictsv::0.0.1
#  - tsv_to_html::0.0.1
#  - attractions_conflation_website_similarity_calculation_scope_module::0.0.1
#  - attractions_entity_similarity_data_merge_scope_module::0.0.1
#  - copy_aether_cosmos_with_fixed_destination::0.0.1
#  - top_reducer_ss::0.0.1
#  - sstreamunion2::0.0.1
#  - attractions_ground_truth_candidates_attributes_generator::0.0.1
#  - generalselectcosmos::0.0.1
#  - createcosmospathfreely::0.0.1
#  - entity_graph_generation::0.0.1
#  - buildentitynamedictionary::0.0.1
#  - namepairsimilaritylookuptableupdates::0.0.1
#  - generatetripple_record_ta_wiki_alltrails::0.0.1
#  - attractions_entity_conflation_image_url_extractor_scope_module::0.0.1
#  - entity_conflation_data_status_monitor::0.0.1
#  - landmark_datacollection_utils_rmacextractor_outings_vc::0.0.1
#  - attractions_conflation_phone_number_similarity_calculation_scope_module::0.0.1
#  - outings_ta_sid_mapping_bvt::0.0.1
#  - cosmos_split_1_tsv_to_5::0.0.1
#  - attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module::0.0.1
#  - conditional_passthrough_anyfile::0.0.1
#  - upload_to_vc_with_inputs_generictsv::0.0.1
#  - outings_entity_conflation_publishing_statistics::0.0.1
#  - flattenwikiclusters::0.0.1
#  - copy_intermediate_data_tsv_to_specific_vc_with_overwrite::0.0.1
#  - outing_distance_metric::0.0.1
#  - cast_anyfile_to_generictsv::0.0.1
#  - attractions_conflation_entity_type_similarity_calculation_scope_module::0.0.1
#  - aetheremailmodule::0.0.1
#  - aml_itp_module::0.0.1
#  - outings_cosine_similarity::0.0.1
#  - outings_get_xpath_value::0.0.1
#  - outings_description_ner::0.0.1
#  - wikicenteredclustering::0.0.1
#  - attractions_conflation_topics_similarity_calculation_scope_module::0.0.1
#  - copy_cosmos_stream_to_intermediate_resource::0.0.1
#  - copy_intermediate_directory_or_file_to_fixed_cosmos_path::0.0.1
#  - copy_cosmospath_to_generictsv::0.0.1
#  - cosmos_split_1_stream_to_10::0.0.1
#  - scope_basics_union_any_type_between_sstreams::0.0.1
#  - create_generic_tsv::0.0.1
#  - not_conditional_decision_logic::0.0.1
#  - outings_topic_extraction::0.0.1
#  - sstream_to_tsv_aether::0.0.1
#  - alltrailscenteredclustering::0.0.1
#  - radio_split_sstream::0.0.1
from pathlib import Path
from typing import Union

from azure.ml.component import Component
from azure.ml.component.component import Input, Output


SOURCE_DIRECTORY = Path(__file__).parent / ".."


class _CommandComponentRunsettingDockerConfiguration:
    """Docker configuration section specify the docker runtime properties for the Run.."""
    arguments: Union[str, list]
    """Extra arguments to the Docker run command. The extra docker container options like --cpus=2, --memory=1024"""
    shared_volumes: bool
    """Indicates whether to use shared volumes. Set to False if necessary to work around shared volume bugs on Windows. The default is True."""
    shm_size: str
    """The size of the Docker container's shared memory block. If not set, the default 2g is used."""
    use_docker: bool
    """Specifies whether the environment to run the experiment should be Docker-based. Amlcompute linux clusters require that jobs running inside Docker containers. The backend will override the value to be true for Amlcompute linux clusters."""


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
    allow_spot_vm: bool
    """Flag to enable target selector service to send job to low priority VM. Currently it only works for AmlK8s."""
    cluster_block_list: Union[str, list]
    """User specified block list of Cluster."""
    compute_type: str
    """Compute type that target selector could route job to. (enum: ['AmlCompute', 'AmlK8s'])"""
    instance_types: Union[str, list]
    """List of instance_type that job could use. If no instance_type specified, all sizes are allowed."""
    my_resource_only: bool
    """Flag to control whether the job should be sent to the cluster owned by user. If False, target selector may send the job to shared cluster. Currently it only works for AmlK8s."""
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


class _ImageDlAndConvertToBase64Input:
    input: Input = None
    """path(optional)"""
    max_size: str = None
    """String (optional)"""


class _ImageDlAndConvertToBase64Output:
    output_out: Output = None
    """path"""


class _ImageDlAndConvertToBase64Component(Component):
    inputs: _ImageDlAndConvertToBase64Input
    outputs: _ImageDlAndConvertToBase64Output
    runsettings: _CommandComponentRunsetting


_image_dl_and_convert_to_base64 = None


def image_dl_and_convert_to_base64(
    input: Path = None,
    max_size: str = None,
) -> _ImageDlAndConvertToBase64Component:
    """image_dl_and_convert_to_base64
    
    :param input: path(optional)
    :type input: Path
    :param max_size: String (optional)
    :type max_size: str
    :output output_out: path
    :type: output_out: Output
    """
    global _image_dl_and_convert_to_base64
    if _image_dl_and_convert_to_base64 is None:
        _image_dl_and_convert_to_base64 = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/image_dl_and_convert_to_base64/0.0.1/0383c80b-7cf5-4a57-8594-25e2bbcba629.spec.yaml")
    return _image_dl_and_convert_to_base64(
            input=input,
            max_size=max_size,)


class _CopyCosmospathToCosmospathtsvInput:
    path: Input = None
    """path(optional)"""
    shouldrespectlineboundaries: str = None
    """String (optional)"""


class _CopyCosmospathToCosmospathtsvOutput:
    tsv_out: Output = None
    """path"""


class _CopyCosmospathToCosmospathtsvComponent(Component):
    inputs: _CopyCosmospathToCosmospathtsvInput
    outputs: _CopyCosmospathToCosmospathtsvOutput
    runsettings: _CommandComponentRunsetting


_copy_cosmospath_to_cosmospathtsv = None


def copy_cosmospath_to_cosmospathtsv(
    path: Path = None,
    shouldrespectlineboundaries: str = None,
) -> _CopyCosmospathToCosmospathtsvComponent:
    """copy_cosmospath_to_cosmospathtsv
    
    :param path: path(optional)
    :type path: Path
    :param shouldrespectlineboundaries: String (optional)
    :type shouldrespectlineboundaries: str
    :output tsv_out: path
    :type: tsv_out: Output
    """
    global _copy_cosmospath_to_cosmospathtsv
    if _copy_cosmospath_to_cosmospathtsv is None:
        _copy_cosmospath_to_cosmospathtsv = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/copy_cosmospath_to_cosmospathtsv/0.0.1/042f53f8-101c-454a-8734-04cddc027959.spec.yaml")
    return _copy_cosmospath_to_cosmospathtsv(
            path=path,
            shouldrespectlineboundaries=shouldrespectlineboundaries,)


class _CreateGenericTsvFileForTransformerOnPy35Input:
    l1: str = None
    """String (optional)"""
    l2: str = None
    """String (optional)"""
    l3: str = None
    """String (optional)"""
    l4: str = None
    """String (optional)"""
    l5: str = None
    """String (optional)"""
    l6: str = None
    """String (optional)"""
    l7: str = None
    """String (optional)"""
    l8: str = None
    """String (optional)"""
    l9: str = None
    """String (optional)"""
    l11: str = None
    """String (optional)"""
    l12: str = None
    """String (optional)"""
    l13: str = None
    """String (optional)"""
    l14: str = None
    """String (optional)"""
    l15: str = None
    """String (optional)"""
    l16: str = None
    """String (optional)"""
    l17: str = None
    """String (optional)"""
    l18: str = None
    """String (optional)"""
    l19: str = None
    """String (optional)"""
    l20: str = None
    """String (optional)"""
    l21: str = None
    """String (optional)"""
    l22: str = None
    """String (optional)"""
    l23: str = None
    """String (optional)"""
    l24: str = None
    """String (optional)"""
    l25: str = None
    """String (optional)"""
    l26: str = None
    """String (optional)"""
    l27: str = None
    """String (optional)"""
    l28: str = None
    """String (optional)"""
    l29: str = None
    """String (optional)"""
    l30: str = None
    """String (optional)"""
    l31: str = None
    """String (optional)"""
    l32: str = None
    """String (optional)"""
    l33: str = None
    """String (optional)"""
    l34: str = None
    """String (optional)"""
    l35: str = None
    """String (optional)"""
    l36: str = None
    """String (optional)"""
    l37: str = None
    """String (optional)"""
    l38: str = None
    """String (optional)"""
    l39: str = None
    """String (optional)"""
    l40: str = None
    """String (optional)"""
    l41: str = None
    """String (optional)"""
    l42: str = None
    """String (optional)"""
    l43: str = None
    """String (optional)"""
    l44: str = None
    """String (optional)"""
    l45: str = None
    """String (optional)"""
    l46: str = None
    """String (optional)"""
    l47: str = None
    """String (optional)"""
    l48: str = None
    """String (optional)"""
    l49: str = None
    """String (optional)"""
    l50: str = None
    """String (optional)"""
    l51: str = None
    """String (optional)"""
    l52: str = None
    """String (optional)"""
    l53: str = None
    """String (optional)"""
    l54: str = None
    """String (optional)"""
    l55: str = None
    """String (optional)"""
    l56: str = None
    """String (optional)"""
    l57: str = None
    """String (optional)"""
    l58: str = None
    """String (optional)"""
    l59: str = None
    """String (optional)"""
    l60: str = None
    """String (optional)"""


class _CreateGenericTsvFileForTransformerOnPy35Output:
    tsvfile_out: Output = None
    """path"""


class _CreateGenericTsvFileForTransformerOnPy35Component(Component):
    inputs: _CreateGenericTsvFileForTransformerOnPy35Input
    outputs: _CreateGenericTsvFileForTransformerOnPy35Output
    runsettings: _CommandComponentRunsetting


_create_generic_tsv_file_for_transformer_on_py3_5 = None


def create_generic_tsv_file_for_transformer_on_py3_5(
    l1: str = None,
    l2: str = None,
    l3: str = None,
    l4: str = None,
    l5: str = None,
    l6: str = None,
    l7: str = None,
    l8: str = None,
    l9: str = None,
    l11: str = None,
    l12: str = None,
    l13: str = None,
    l14: str = None,
    l15: str = None,
    l16: str = None,
    l17: str = None,
    l18: str = None,
    l19: str = None,
    l20: str = None,
    l21: str = None,
    l22: str = None,
    l23: str = None,
    l24: str = None,
    l25: str = None,
    l26: str = None,
    l27: str = None,
    l28: str = None,
    l29: str = None,
    l30: str = None,
    l31: str = None,
    l32: str = None,
    l33: str = None,
    l34: str = None,
    l35: str = None,
    l36: str = None,
    l37: str = None,
    l38: str = None,
    l39: str = None,
    l40: str = None,
    l41: str = None,
    l42: str = None,
    l43: str = None,
    l44: str = None,
    l45: str = None,
    l46: str = None,
    l47: str = None,
    l48: str = None,
    l49: str = None,
    l50: str = None,
    l51: str = None,
    l52: str = None,
    l53: str = None,
    l54: str = None,
    l55: str = None,
    l56: str = None,
    l57: str = None,
    l58: str = None,
    l59: str = None,
    l60: str = None,
) -> _CreateGenericTsvFileForTransformerOnPy35Component:
    """create_generic_tsv_file_for_transformer_on_py3_5
    
    :param l1: String (optional)
    :type l1: str
    :param l2: String (optional)
    :type l2: str
    :param l3: String (optional)
    :type l3: str
    :param l4: String (optional)
    :type l4: str
    :param l5: String (optional)
    :type l5: str
    :param l6: String (optional)
    :type l6: str
    :param l7: String (optional)
    :type l7: str
    :param l8: String (optional)
    :type l8: str
    :param l9: String (optional)
    :type l9: str
    :param l11: String (optional)
    :type l11: str
    :param l12: String (optional)
    :type l12: str
    :param l13: String (optional)
    :type l13: str
    :param l14: String (optional)
    :type l14: str
    :param l15: String (optional)
    :type l15: str
    :param l16: String (optional)
    :type l16: str
    :param l17: String (optional)
    :type l17: str
    :param l18: String (optional)
    :type l18: str
    :param l19: String (optional)
    :type l19: str
    :param l20: String (optional)
    :type l20: str
    :param l21: String (optional)
    :type l21: str
    :param l22: String (optional)
    :type l22: str
    :param l23: String (optional)
    :type l23: str
    :param l24: String (optional)
    :type l24: str
    :param l25: String (optional)
    :type l25: str
    :param l26: String (optional)
    :type l26: str
    :param l27: String (optional)
    :type l27: str
    :param l28: String (optional)
    :type l28: str
    :param l29: String (optional)
    :type l29: str
    :param l30: String (optional)
    :type l30: str
    :param l31: String (optional)
    :type l31: str
    :param l32: String (optional)
    :type l32: str
    :param l33: String (optional)
    :type l33: str
    :param l34: String (optional)
    :type l34: str
    :param l35: String (optional)
    :type l35: str
    :param l36: String (optional)
    :type l36: str
    :param l37: String (optional)
    :type l37: str
    :param l38: String (optional)
    :type l38: str
    :param l39: String (optional)
    :type l39: str
    :param l40: String (optional)
    :type l40: str
    :param l41: String (optional)
    :type l41: str
    :param l42: String (optional)
    :type l42: str
    :param l43: String (optional)
    :type l43: str
    :param l44: String (optional)
    :type l44: str
    :param l45: String (optional)
    :type l45: str
    :param l46: String (optional)
    :type l46: str
    :param l47: String (optional)
    :type l47: str
    :param l48: String (optional)
    :type l48: str
    :param l49: String (optional)
    :type l49: str
    :param l50: String (optional)
    :type l50: str
    :param l51: String (optional)
    :type l51: str
    :param l52: String (optional)
    :type l52: str
    :param l53: String (optional)
    :type l53: str
    :param l54: String (optional)
    :type l54: str
    :param l55: String (optional)
    :type l55: str
    :param l56: String (optional)
    :type l56: str
    :param l57: String (optional)
    :type l57: str
    :param l58: String (optional)
    :type l58: str
    :param l59: String (optional)
    :type l59: str
    :param l60: String (optional)
    :type l60: str
    :output tsvfile_out: path
    :type: tsvfile_out: Output
    """
    global _create_generic_tsv_file_for_transformer_on_py3_5
    if _create_generic_tsv_file_for_transformer_on_py3_5 is None:
        _create_generic_tsv_file_for_transformer_on_py3_5 = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/create_generic_tsv_file_for_transformer_on_py3_5/0.0.1/049d4bf7-3c80-40fc-84c4-6fc24f17e464.spec.yaml")
    return _create_generic_tsv_file_for_transformer_on_py3_5(
            l1=l1,
            l2=l2,
            l3=l3,
            l4=l4,
            l5=l5,
            l6=l6,
            l7=l7,
            l8=l8,
            l9=l9,
            l11=l11,
            l12=l12,
            l13=l13,
            l14=l14,
            l15=l15,
            l16=l16,
            l17=l17,
            l18=l18,
            l19=l19,
            l20=l20,
            l21=l21,
            l22=l22,
            l23=l23,
            l24=l24,
            l25=l25,
            l26=l26,
            l27=l27,
            l28=l28,
            l29=l29,
            l30=l30,
            l31=l31,
            l32=l32,
            l33=l33,
            l34=l34,
            l35=l35,
            l36=l36,
            l37=l37,
            l38=l38,
            l39=l39,
            l40=l40,
            l41=l41,
            l42=l42,
            l43=l43,
            l44=l44,
            l45=l45,
            l46=l46,
            l47=l47,
            l48=l48,
            l49=l49,
            l50=l50,
            l51=l51,
            l52=l52,
            l53=l53,
            l54=l54,
            l55=l55,
            l56=l56,
            l57=l57,
            l58=l58,
            l59=l59,
            l60=l60,)


class _TaprioritizedclusteringInput:
    inputfile: Input = None
    """path(optional)"""


class _TaprioritizedclusteringOutput:
    outputfile_out: Output = None
    """path"""


class _TaprioritizedclusteringComponent(Component):
    inputs: _TaprioritizedclusteringInput
    outputs: _TaprioritizedclusteringOutput
    runsettings: _CommandComponentRunsetting


_taprioritizedclustering = None


def taprioritizedclustering(
    inputfile: Path = None,
) -> _TaprioritizedclusteringComponent:
    """taprioritizedclustering
    
    :param inputfile: path(optional)
    :type inputfile: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _taprioritizedclustering
    if _taprioritizedclustering is None:
        _taprioritizedclustering = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/taprioritizedclustering/0.0.1/06547379-ae1b-40fc-9f51-376d20a7cbd8.spec.yaml")
    return _taprioritizedclustering(
            inputfile=inputfile,)


class _OutingsSourceUrlIdGeneratorInput:
    input: Input = None
    """path(optional)"""
    url_col: str = None
    """String (optional)"""
    url_id_col: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsSourceUrlIdGeneratorOutput:
    output_ss_out: Output = None
    """path"""


class _OutingsSourceUrlIdGeneratorComponent(Component):
    inputs: _OutingsSourceUrlIdGeneratorInput
    outputs: _OutingsSourceUrlIdGeneratorOutput
    runsettings: _CommandComponentRunsetting


_outings_source_url_id_generator = None


def outings_source_url_id_generator(
    input: Path = None,
    url_col: str = None,
    url_id_col: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsSourceUrlIdGeneratorComponent:
    """outings_source_url_id_generator
    
    :param input: path(optional)
    :type input: Path
    :param url_col: String (optional)
    :type url_col: str
    :param url_id_col: String (optional)
    :type url_id_col: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output output_ss_out: path
    :type: output_ss_out: Output
    """
    global _outings_source_url_id_generator
    if _outings_source_url_id_generator is None:
        _outings_source_url_id_generator = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_source_url_id_generator/0.0.1/06596454-cb88-4ab1-bc65-7f13f87127bb.spec.yaml")
    return _outings_source_url_id_generator(
            input=input,
            url_col=url_col,
            url_id_col=url_id_col,
            vc=vc,
            scopeparams=scopeparams,)


class _OutingsDominantTypeClassifierInput:
    inputdata: Input = None
    """path(optional)"""


class _OutingsDominantTypeClassifierOutput:
    countsofentitytypes_out: Output = None
    """path"""
    dominantentitytypes_out: Output = None
    """path"""


class _OutingsDominantTypeClassifierComponent(Component):
    inputs: _OutingsDominantTypeClassifierInput
    outputs: _OutingsDominantTypeClassifierOutput
    runsettings: _CommandComponentRunsetting


_outings_dominant_type_classifier = None


def outings_dominant_type_classifier(
    inputdata: Path = None,
) -> _OutingsDominantTypeClassifierComponent:
    """outings_dominant_type_classifier
    
    :param inputdata: path(optional)
    :type inputdata: Path
    :output countsofentitytypes_out: path
    :type: countsofentitytypes_out: Output
    :output dominantentitytypes_out: path
    :type: dominantentitytypes_out: Output
    """
    global _outings_dominant_type_classifier
    if _outings_dominant_type_classifier is None:
        _outings_dominant_type_classifier = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_dominant_type_classifier/0.0.1/0b19b1dc-733b-4a91-a439-42d9c567d727.spec.yaml")
    return _outings_dominant_type_classifier(
            inputdata=inputdata,)


class _OutingsTaSidMappingGeneratorInput:
    all_trails_feed: Input = None
    """path(optional)"""
    ta_satori_map: Input = None
    """path(optional)"""
    wiki_satori_map: Input = None
    """path(optional)"""
    triples_ss: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""


class _OutingsTaSidMappingGeneratorOutput:
    record_ta_sid_triples_out: Output = None
    """path"""
    ta_sid_mapping_out: Output = None
    """path"""


class _OutingsTaSidMappingGeneratorComponent(Component):
    inputs: _OutingsTaSidMappingGeneratorInput
    outputs: _OutingsTaSidMappingGeneratorOutput
    runsettings: _CommandComponentRunsetting


_outings_ta_sid_mapping_generator = None


def outings_ta_sid_mapping_generator(
    all_trails_feed: Path = None,
    ta_satori_map: Path = None,
    wiki_satori_map: Path = None,
    triples_ss: Path = None,
    vc: str = None,
) -> _OutingsTaSidMappingGeneratorComponent:
    """outings_ta_sid_mapping_generator
    
    :param all_trails_feed: path(optional)
    :type all_trails_feed: Path
    :param ta_satori_map: path(optional)
    :type ta_satori_map: Path
    :param wiki_satori_map: path(optional)
    :type wiki_satori_map: Path
    :param triples_ss: path(optional)
    :type triples_ss: Path
    :param vc: String (optional)
    :type vc: str
    :output record_ta_sid_triples_out: path
    :type: record_ta_sid_triples_out: Output
    :output ta_sid_mapping_out: path
    :type: ta_sid_mapping_out: Output
    """
    global _outings_ta_sid_mapping_generator
    if _outings_ta_sid_mapping_generator is None:
        _outings_ta_sid_mapping_generator = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_ta_sid_mapping_generator/0.0.1/0bd01fd0-b531-41aa-aa02-ba12d1227d43.spec.yaml")
    return _outings_ta_sid_mapping_generator(
            all_trails_feed=all_trails_feed,
            ta_satori_map=ta_satori_map,
            wiki_satori_map=wiki_satori_map,
            triples_ss=triples_ss,
            vc=vc,)


class _RbfSvmPredictionOngraphInput:
    inputfile1: Input = None
    """path(optional)"""
    inputfile2: Input = None
    """path(optional)"""
    inputfile3: Input = None
    """path(optional)"""
    inputfile4: Input = None
    """path(optional)"""


class _RbfSvmPredictionOngraphOutput:
    outputfile1_out: Output = None
    """path"""
    outputfile2_out: Output = None
    """path"""


class _RbfSvmPredictionOngraphComponent(Component):
    inputs: _RbfSvmPredictionOngraphInput
    outputs: _RbfSvmPredictionOngraphOutput
    runsettings: _CommandComponentRunsetting


_rbf_svm_prediction_ongraph = None


def rbf_svm_prediction_ongraph(
    inputfile1: Path = None,
    inputfile2: Path = None,
    inputfile3: Path = None,
    inputfile4: Path = None,
) -> _RbfSvmPredictionOngraphComponent:
    """rbf_svm_prediction_ongraph
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :param inputfile2: path(optional)
    :type inputfile2: Path
    :param inputfile3: path(optional)
    :type inputfile3: Path
    :param inputfile4: path(optional)
    :type inputfile4: Path
    :output outputfile1_out: path
    :type: outputfile1_out: Output
    :output outputfile2_out: path
    :type: outputfile2_out: Output
    """
    global _rbf_svm_prediction_ongraph
    if _rbf_svm_prediction_ongraph is None:
        _rbf_svm_prediction_ongraph = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/rbf_svm_prediction_ongraph/0.0.1/0d429895-b7cb-4273-b868-ce5e636ed320.spec.yaml")
    return _rbf_svm_prediction_ongraph(
            inputfile1=inputfile1,
            inputfile2=inputfile2,
            inputfile3=inputfile3,
            inputfile4=inputfile4,)


class _CosmospathcreatorRundateInput:
    relativepath: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    rundate: str = None
    """String (optional)"""


class _CosmospathcreatorRundateOutput:
    createdpath_out: Output = None
    """path"""


class _CosmospathcreatorRundateComponent(Component):
    inputs: _CosmospathcreatorRundateInput
    outputs: _CosmospathcreatorRundateOutput
    runsettings: _CommandComponentRunsetting


_cosmospathcreator_rundate = None


def cosmospathcreator_rundate(
    relativepath: str = None,
    vc: str = None,
    rundate: str = None,
) -> _CosmospathcreatorRundateComponent:
    """cosmospathcreator_rundate
    
    :param relativepath: String (optional)
    :type relativepath: str
    :param vc: String (optional)
    :type vc: str
    :param rundate: String (optional)
    :type rundate: str
    :output createdpath_out: path
    :type: createdpath_out: Output
    """
    global _cosmospathcreator_rundate
    if _cosmospathcreator_rundate is None:
        _cosmospathcreator_rundate = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/cosmospathcreator_rundate/0.0.1/163ac5f4-d269-4221-9cd4-9e319459bace.spec.yaml")
    return _cosmospathcreator_rundate(
            relativepath=relativepath,
            vc=vc,
            rundate=rundate,)


class _NamesimilaritybasedcandidatepairgenerationInput:
    inputfile1: Input = None
    """path(optional)"""
    inputfile2: Input = None
    """path(optional)"""
    inputfile3: Input = None
    """path(optional)"""


class _NamesimilaritybasedcandidatepairgenerationOutput:
    outputfile_out: Output = None
    """path"""


class _NamesimilaritybasedcandidatepairgenerationComponent(Component):
    inputs: _NamesimilaritybasedcandidatepairgenerationInput
    outputs: _NamesimilaritybasedcandidatepairgenerationOutput
    runsettings: _CommandComponentRunsetting


_namesimilaritybasedcandidatepairgeneration = None


def namesimilaritybasedcandidatepairgeneration(
    inputfile1: Path = None,
    inputfile2: Path = None,
    inputfile3: Path = None,
) -> _NamesimilaritybasedcandidatepairgenerationComponent:
    """namesimilaritybasedcandidatepairgeneration
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :param inputfile2: path(optional)
    :type inputfile2: Path
    :param inputfile3: path(optional)
    :type inputfile3: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _namesimilaritybasedcandidatepairgeneration
    if _namesimilaritybasedcandidatepairgeneration is None:
        _namesimilaritybasedcandidatepairgeneration = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/namesimilaritybasedcandidatepairgeneration/0.0.1/1fcfbd2f-9a4d-4fa8-a881-1f93bfc31c58.spec.yaml")
    return _namesimilaritybasedcandidatepairgeneration(
            inputfile1=inputfile1,
            inputfile2=inputfile2,
            inputfile3=inputfile3,)


class _ParameterToControlOutputInput:
    control_output: str = None
    """String (optional)"""


class _ParameterToControlOutputOutput:
    control_out: Output = None
    """path"""


class _ParameterToControlOutputComponent(Component):
    inputs: _ParameterToControlOutputInput
    outputs: _ParameterToControlOutputOutput
    runsettings: _CommandComponentRunsetting


_parameter_to_control_output = None


def parameter_to_control_output(
    control_output: str = None,
) -> _ParameterToControlOutputComponent:
    """parameter_to_control_output
    
    :param control_output: String (optional)
    :type control_output: str
    :output control_out: path
    :type: control_out: Output
    """
    global _parameter_to_control_output
    if _parameter_to_control_output is None:
        _parameter_to_control_output = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/parameter_to_control_output/0.0.1/2bf17db2-288d-4cdb-a007-e26851879d5e.spec.yaml")
    return _parameter_to_control_output(
            control_output=control_output,)


class _OutingsCastOneTableRemoveFromOtherUnionBothInput:
    remove_input: Input = None
    """path(optional)"""
    cast_input: Input = None
    """path(optional)"""
    cast_list: str = None
    """String (optional)"""
    remove_list: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsCastOneTableRemoveFromOtherUnionBothOutput:
    output_ss_out: Output = None
    """path"""


class _OutingsCastOneTableRemoveFromOtherUnionBothComponent(Component):
    inputs: _OutingsCastOneTableRemoveFromOtherUnionBothInput
    outputs: _OutingsCastOneTableRemoveFromOtherUnionBothOutput
    runsettings: _CommandComponentRunsetting


_outings_cast_one_table_remove_from_other_union_both = None


def outings_cast_one_table_remove_from_other_union_both(
    remove_input: Path = None,
    cast_input: Path = None,
    cast_list: str = None,
    remove_list: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsCastOneTableRemoveFromOtherUnionBothComponent:
    """outings_cast_one_table_remove_from_other_union_both
    
    :param remove_input: path(optional)
    :type remove_input: Path
    :param cast_input: path(optional)
    :type cast_input: Path
    :param cast_list: String (optional)
    :type cast_list: str
    :param remove_list: String (optional)
    :type remove_list: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output output_ss_out: path
    :type: output_ss_out: Output
    """
    global _outings_cast_one_table_remove_from_other_union_both
    if _outings_cast_one_table_remove_from_other_union_both is None:
        _outings_cast_one_table_remove_from_other_union_both = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_cast_one_table_remove_from_other_union_both/0.0.1/2c5fa142-4b6e-4e3d-afac-6289f686ef8d.spec.yaml")
    return _outings_cast_one_table_remove_from_other_union_both(
            remove_input=remove_input,
            cast_input=cast_input,
            cast_list=cast_list,
            remove_list=remove_list,
            vc=vc,
            scopeparams=scopeparams,)


class _IsFileEmptyToControloutputInput:
    input: Input = None
    """path(optional)"""


class _IsFileEmptyToControloutputOutput:
    control_out: Output = None
    """path"""


class _IsFileEmptyToControloutputComponent(Component):
    inputs: _IsFileEmptyToControloutputInput
    outputs: _IsFileEmptyToControloutputOutput
    runsettings: _CommandComponentRunsetting


_is_file_empty_to_controloutput = None


def is_file_empty_to_controloutput(
    input: Path = None,
) -> _IsFileEmptyToControloutputComponent:
    """is_file_empty_to_controloutput
    
    :param input: path(optional)
    :type input: Path
    :output control_out: path
    :type: control_out: Output
    """
    global _is_file_empty_to_controloutput
    if _is_file_empty_to_controloutput is None:
        _is_file_empty_to_controloutput = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/is_file_empty_to_controloutput/0.0.1/3979514d-c94e-4e1a-a705-8ddccd34d3ff.spec.yaml")
    return _is_file_empty_to_controloutput(
            input=input,)


class _CosmosSplit1TsvTo10Input:
    inputfile: Input = None
    """path(optional)"""
    scopeparams: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _CosmosSplit1TsvTo10Output:
    part0_out: Output = None
    """path"""
    part1_out: Output = None
    """path"""
    part2_out: Output = None
    """path"""
    part3_out: Output = None
    """path"""
    part4_out: Output = None
    """path"""
    part5_out: Output = None
    """path"""
    part6_out: Output = None
    """path"""
    part7_out: Output = None
    """path"""
    part8_out: Output = None
    """path"""
    part9_out: Output = None
    """path"""


class _CosmosSplit1TsvTo10Component(Component):
    inputs: _CosmosSplit1TsvTo10Input
    outputs: _CosmosSplit1TsvTo10Output
    runsettings: _CommandComponentRunsetting


_cosmos_split_1_tsv_to_10 = None


def cosmos_split_1_tsv_to_10(
    inputfile: Path = None,
    scopeparams: str = None,
    vc: str = None,
) -> _CosmosSplit1TsvTo10Component:
    """cosmos_split_1_tsv_to_10
    
    :param inputfile: path(optional)
    :type inputfile: Path
    :param scopeparams: String (optional)
    :type scopeparams: str
    :param vc: String (optional)
    :type vc: str
    :output part0_out: path
    :type: part0_out: Output
    :output part1_out: path
    :type: part1_out: Output
    :output part2_out: path
    :type: part2_out: Output
    :output part3_out: path
    :type: part3_out: Output
    :output part4_out: path
    :type: part4_out: Output
    :output part5_out: path
    :type: part5_out: Output
    :output part6_out: path
    :type: part6_out: Output
    :output part7_out: path
    :type: part7_out: Output
    :output part8_out: path
    :type: part8_out: Output
    :output part9_out: path
    :type: part9_out: Output
    """
    global _cosmos_split_1_tsv_to_10
    if _cosmos_split_1_tsv_to_10 is None:
        _cosmos_split_1_tsv_to_10 = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/cosmos_split_1_tsv_to_10/0.0.1/3abddb52-2043-45c1-ab3f-47adfcd765db.spec.yaml")
    return _cosmos_split_1_tsv_to_10(
            inputfile=inputfile,
            scopeparams=scopeparams,
            vc=vc,)


class _BuildentitynamevectorsInput:
    inputfile1: Input = None
    """path(optional)"""
    inputfile2: Input = None
    """path(optional)"""


class _BuildentitynamevectorsOutput:
    outputfile_out: Output = None
    """path"""


class _BuildentitynamevectorsComponent(Component):
    inputs: _BuildentitynamevectorsInput
    outputs: _BuildentitynamevectorsOutput
    runsettings: _CommandComponentRunsetting


_buildentitynamevectors = None


def buildentitynamevectors(
    inputfile1: Path = None,
    inputfile2: Path = None,
) -> _BuildentitynamevectorsComponent:
    """buildentitynamevectors
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :param inputfile2: path(optional)
    :type inputfile2: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _buildentitynamevectors
    if _buildentitynamevectors is None:
        _buildentitynamevectors = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/buildentitynamevectors/0.0.1/3e4bc052-8cbb-4e1b-9362-b97a99b0487a.spec.yaml")
    return _buildentitynamevectors(
            inputfile1=inputfile1,
            inputfile2=inputfile2,)


class _GuidTaWikiSidPrmeasureInput:
    dataset_pr_measure: Input = None
    """path(optional)"""
    master_ta_storyid: Input = None
    """path(optional)"""
    master_wiki_storyid: Input = None
    """path(optional)"""
    master_attribute: Input = None
    """path(optional)"""
    master_sid_storyid: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""


class _GuidTaWikiSidPrmeasureOutput:
    stat_guid_ta_wiki_sid_out: Output = None
    """path"""


class _GuidTaWikiSidPrmeasureComponent(Component):
    inputs: _GuidTaWikiSidPrmeasureInput
    outputs: _GuidTaWikiSidPrmeasureOutput
    runsettings: _CommandComponentRunsetting


_guid_ta_wiki_sid_prmeasure = None


def guid_ta_wiki_sid_prmeasure(
    dataset_pr_measure: Path = None,
    master_ta_storyid: Path = None,
    master_wiki_storyid: Path = None,
    master_attribute: Path = None,
    master_sid_storyid: Path = None,
    vc: str = None,
) -> _GuidTaWikiSidPrmeasureComponent:
    """guid_ta_wiki_sid_prmeasure
    
    :param dataset_pr_measure: path(optional)
    :type dataset_pr_measure: Path
    :param master_ta_storyid: path(optional)
    :type master_ta_storyid: Path
    :param master_wiki_storyid: path(optional)
    :type master_wiki_storyid: Path
    :param master_attribute: path(optional)
    :type master_attribute: Path
    :param master_sid_storyid: path(optional)
    :type master_sid_storyid: Path
    :param vc: String (optional)
    :type vc: str
    :output stat_guid_ta_wiki_sid_out: path
    :type: stat_guid_ta_wiki_sid_out: Output
    """
    global _guid_ta_wiki_sid_prmeasure
    if _guid_ta_wiki_sid_prmeasure is None:
        _guid_ta_wiki_sid_prmeasure = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/guid_ta_wiki_sid_prmeasure/0.0.1/3f41220d-51d5-48d7-9c35-df7c97e50a9c.spec.yaml")
    return _guid_ta_wiki_sid_prmeasure(
            dataset_pr_measure=dataset_pr_measure,
            master_ta_storyid=master_ta_storyid,
            master_wiki_storyid=master_wiki_storyid,
            master_attribute=master_attribute,
            master_sid_storyid=master_sid_storyid,
            vc=vc,)


class _CosmosMirrorWithInputsAndOverwriteInput:
    sourcepath: Input = None
    """path(optional)"""
    destinationpath: Input = None
    """path(optional)"""
    expiration: str = None
    """String (optional)"""
    datamanagementenabled: str = None
    """String (optional)"""
    shouldoverrideifexists: str = None
    """String (optional)"""


class _CosmosMirrorWithInputsAndOverwriteOutput:
    destinationpath_out: Output = None
    """path"""


class _CosmosMirrorWithInputsAndOverwriteComponent(Component):
    inputs: _CosmosMirrorWithInputsAndOverwriteInput
    outputs: _CosmosMirrorWithInputsAndOverwriteOutput
    runsettings: _CommandComponentRunsetting


_cosmos_mirror_with_inputs_and_overwrite = None


def cosmos_mirror_with_inputs_and_overwrite(
    sourcepath: Path = None,
    destinationpath: Path = None,
    expiration: str = None,
    datamanagementenabled: str = None,
    shouldoverrideifexists: str = None,
) -> _CosmosMirrorWithInputsAndOverwriteComponent:
    """cosmos_mirror_with_inputs_and_overwrite
    
    :param sourcepath: path(optional)
    :type sourcepath: Path
    :param destinationpath: path(optional)
    :type destinationpath: Path
    :param expiration: String (optional)
    :type expiration: str
    :param datamanagementenabled: String (optional)
    :type datamanagementenabled: str
    :param shouldoverrideifexists: String (optional)
    :type shouldoverrideifexists: str
    :output destinationpath_out: path
    :type: destinationpath_out: Output
    """
    global _cosmos_mirror_with_inputs_and_overwrite
    if _cosmos_mirror_with_inputs_and_overwrite is None:
        _cosmos_mirror_with_inputs_and_overwrite = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/cosmos_mirror_with_inputs_and_overwrite/0.0.1/3fc840ea-4ab2-42d6-b877-050bbcc24574.spec.yaml")
    return _cosmos_mirror_with_inputs_and_overwrite(
            sourcepath=sourcepath,
            destinationpath=destinationpath,
            expiration=expiration,
            datamanagementenabled=datamanagementenabled,
            shouldoverrideifexists=shouldoverrideifexists,)


class _GetImageAttractivenessScoreUsingBase64EncodedImageInput:
    input1: Input = None
    """path(optional)"""
    param1: str = None
    """String (optional)"""


class _GetImageAttractivenessScoreUsingBase64EncodedImageOutput:
    output1_out: Output = None
    """path"""


class _GetImageAttractivenessScoreUsingBase64EncodedImageComponent(Component):
    inputs: _GetImageAttractivenessScoreUsingBase64EncodedImageInput
    outputs: _GetImageAttractivenessScoreUsingBase64EncodedImageOutput
    runsettings: _CommandComponentRunsetting


_get_image_attractiveness_score_using_base64_encoded_image = None


def get_image_attractiveness_score_using_base64_encoded_image(
    input1: Path = None,
    param1: str = None,
) -> _GetImageAttractivenessScoreUsingBase64EncodedImageComponent:
    """get_image_attractiveness_score_using_base64_encoded_image
    
    :param input1: path(optional)
    :type input1: Path
    :param param1: String (optional)
    :type param1: str
    :output output1_out: path
    :type: output1_out: Output
    """
    global _get_image_attractiveness_score_using_base64_encoded_image
    if _get_image_attractiveness_score_using_base64_encoded_image is None:
        _get_image_attractiveness_score_using_base64_encoded_image = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/get_image_attractiveness_score_using_base64_encoded_image/0.0.1/45f9989b-4340-422f-a66e-cfaea87a941e.spec.yaml")
    return _get_image_attractiveness_score_using_base64_encoded_image(
            input1=input1,
            param1=param1,)


class _FlattenclustersInput:
    inputfile1: Input = None
    """path(optional)"""
    inputfile2: Input = None
    """path(optional)"""


class _FlattenclustersOutput:
    outputfile_out: Output = None
    """path"""


class _FlattenclustersComponent(Component):
    inputs: _FlattenclustersInput
    outputs: _FlattenclustersOutput
    runsettings: _CommandComponentRunsetting


_flattenclusters = None


def flattenclusters(
    inputfile1: Path = None,
    inputfile2: Path = None,
) -> _FlattenclustersComponent:
    """flattenclusters
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :param inputfile2: path(optional)
    :type inputfile2: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _flattenclusters
    if _flattenclusters is None:
        _flattenclusters = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/flattenclusters/0.0.1/4b540432-92e0-4752-84ee-e45abbc893e4.spec.yaml")
    return _flattenclusters(
            inputfile1=inputfile1,
            inputfile2=inputfile2,)


class _OrConditionalDecisionLogicInput:
    controla: Input = None
    """path(optional)"""
    controlb: Input = None
    """path(optional)"""


class _OrConditionalDecisionLogicOutput:
    control_out: Output = None
    """path"""


class _OrConditionalDecisionLogicComponent(Component):
    inputs: _OrConditionalDecisionLogicInput
    outputs: _OrConditionalDecisionLogicOutput
    runsettings: _CommandComponentRunsetting


_or_conditional_decision_logic = None


def or_conditional_decision_logic(
    controla: Path = None,
    controlb: Path = None,
) -> _OrConditionalDecisionLogicComponent:
    """or_conditional_decision_logic
    
    :param controla: path(optional)
    :type controla: Path
    :param controlb: path(optional)
    :type controlb: Path
    :output control_out: path
    :type: control_out: Output
    """
    global _or_conditional_decision_logic
    if _or_conditional_decision_logic is None:
        _or_conditional_decision_logic = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/or_conditional_decision_logic/0.0.1/4e9bd62a-b00e-4d41-9c20-86fd62d103a3.spec.yaml")
    return _or_conditional_decision_logic(
            controla=controla,
            controlb=controlb,)


class _ReversegeocoderInput:
    inputfile: Input = None
    """path(optional)"""


class _ReversegeocoderOutput:
    outputfile_out: Output = None
    """path"""


class _ReversegeocoderComponent(Component):
    inputs: _ReversegeocoderInput
    outputs: _ReversegeocoderOutput
    runsettings: _CommandComponentRunsetting


_reversegeocoder = None


def reversegeocoder(
    inputfile: Path = None,
) -> _ReversegeocoderComponent:
    """reversegeocoder
    
    :param inputfile: path(optional)
    :type inputfile: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _reversegeocoder
    if _reversegeocoder is None:
        _reversegeocoder = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/reversegeocoder/0.0.1/54c38391-1fc5-4f70-9329-7d5c3e02d121.spec.yaml")
    return _reversegeocoder(
            inputfile=inputfile,)


class _OutingsRemoveColumnsFromStructuredStreamInput:
    input_stream: Input = None
    """path(optional)"""
    columns_to_remove: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsRemoveColumnsFromStructuredStreamOutput:
    output_stream_out: Output = None
    """path"""


class _OutingsRemoveColumnsFromStructuredStreamComponent(Component):
    inputs: _OutingsRemoveColumnsFromStructuredStreamInput
    outputs: _OutingsRemoveColumnsFromStructuredStreamOutput
    runsettings: _CommandComponentRunsetting


_outings_remove_columns_from_structured_stream = None


def outings_remove_columns_from_structured_stream(
    input_stream: Path = None,
    columns_to_remove: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsRemoveColumnsFromStructuredStreamComponent:
    """outings_remove_columns_from_structured_stream
    
    :param input_stream: path(optional)
    :type input_stream: Path
    :param columns_to_remove: String (optional)
    :type columns_to_remove: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output output_stream_out: path
    :type: output_stream_out: Output
    """
    global _outings_remove_columns_from_structured_stream
    if _outings_remove_columns_from_structured_stream is None:
        _outings_remove_columns_from_structured_stream = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_remove_columns_from_structured_stream/0.0.1/5869d767-fcb7-44f7-8f81-c19f0ab49f5f.spec.yaml")
    return _outings_remove_columns_from_structured_stream(
            input_stream=input_stream,
            columns_to_remove=columns_to_remove,
            vc=vc,
            scopeparams=scopeparams,)


class _ReplacecosmospathInput:
    input: Input = None
    """path(optional)"""
    srcstring: str = None
    """String (optional)"""
    deststring: str = None
    """String (optional)"""


class _ReplacecosmospathOutput:
    count_out: Output = None
    """path"""


class _ReplacecosmospathComponent(Component):
    inputs: _ReplacecosmospathInput
    outputs: _ReplacecosmospathOutput
    runsettings: _CommandComponentRunsetting


_replacecosmospath = None


def replacecosmospath(
    input: Path = None,
    srcstring: str = None,
    deststring: str = None,
) -> _ReplacecosmospathComponent:
    """replacecosmospath
    
    :param input: path(optional)
    :type input: Path
    :param srcstring: String (optional)
    :type srcstring: str
    :param deststring: String (optional)
    :type deststring: str
    :output count_out: path
    :type: count_out: Output
    """
    global _replacecosmospath
    if _replacecosmospath is None:
        _replacecosmospath = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/replacecosmospath/0.0.1/5b8fac9e-318b-4139-a274-9f8c2ec5e3eb.spec.yaml")
    return _replacecosmospath(
            input=input,
            srcstring=srcstring,
            deststring=deststring,)


class _ScopeBasicsUnionIntersectExceptSstreamInput:
    first: Input = None
    """path(optional)"""
    second: Input = None
    """path(optional)"""
    third: Input = None
    """path(optional)"""
    fourth: Input = None
    """path(optional)"""
    fifth: Input = None
    """path(optional)"""
    sixth: Input = None
    """path(optional)"""
    seventh: Input = None
    """path(optional)"""
    eight: Input = None
    """path(optional)"""
    ninth: Input = None
    """path(optional)"""
    tenth: Input = None
    """path(optional)"""
    eleventh: Input = None
    """path(optional)"""
    twelveth: Input = None
    """path(optional)"""
    uniontype: str = None
    """String (optional)"""
    clusteredbycolumns: str = None
    """String (optional)"""
    sortedbycolumns: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _ScopeBasicsUnionIntersectExceptSstreamOutput:
    outputss_out: Output = None
    """path"""


class _ScopeBasicsUnionIntersectExceptSstreamComponent(Component):
    inputs: _ScopeBasicsUnionIntersectExceptSstreamInput
    outputs: _ScopeBasicsUnionIntersectExceptSstreamOutput
    runsettings: _CommandComponentRunsetting


_scope_basics_union_intersect_except_sstream = None


def scope_basics_union_intersect_except_sstream(
    first: Path = None,
    second: Path = None,
    third: Path = None,
    fourth: Path = None,
    fifth: Path = None,
    sixth: Path = None,
    seventh: Path = None,
    eight: Path = None,
    ninth: Path = None,
    tenth: Path = None,
    eleventh: Path = None,
    twelveth: Path = None,
    uniontype: str = None,
    clusteredbycolumns: str = None,
    sortedbycolumns: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _ScopeBasicsUnionIntersectExceptSstreamComponent:
    """scope_basics_union_intersect_except_sstream
    
    :param first: path(optional)
    :type first: Path
    :param second: path(optional)
    :type second: Path
    :param third: path(optional)
    :type third: Path
    :param fourth: path(optional)
    :type fourth: Path
    :param fifth: path(optional)
    :type fifth: Path
    :param sixth: path(optional)
    :type sixth: Path
    :param seventh: path(optional)
    :type seventh: Path
    :param eight: path(optional)
    :type eight: Path
    :param ninth: path(optional)
    :type ninth: Path
    :param tenth: path(optional)
    :type tenth: Path
    :param eleventh: path(optional)
    :type eleventh: Path
    :param twelveth: path(optional)
    :type twelveth: Path
    :param uniontype: String (optional)
    :type uniontype: str
    :param clusteredbycolumns: String (optional)
    :type clusteredbycolumns: str
    :param sortedbycolumns: String (optional)
    :type sortedbycolumns: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output outputss_out: path
    :type: outputss_out: Output
    """
    global _scope_basics_union_intersect_except_sstream
    if _scope_basics_union_intersect_except_sstream is None:
        _scope_basics_union_intersect_except_sstream = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/scope_basics_union_intersect_except_sstream/0.0.1/5f03c307-f326-4381-a5d1-e980b7307a57.spec.yaml")
    return _scope_basics_union_intersect_except_sstream(
            first=first,
            second=second,
            third=third,
            fourth=fourth,
            fifth=fifth,
            sixth=sixth,
            seventh=seventh,
            eight=eight,
            ninth=ninth,
            tenth=tenth,
            eleventh=eleventh,
            twelveth=twelveth,
            uniontype=uniontype,
            clusteredbycolumns=clusteredbycolumns,
            sortedbycolumns=sortedbycolumns,
            vc=vc,
            scopeparams=scopeparams,)


class _ConcatGenerictsvInput:
    input_1: Input = None
    """path(optional)"""
    input_2: Input = None
    """path(optional)"""
    input2hasheader: str = None
    """String (optional)"""


class _ConcatGenerictsvOutput:
    output_out: Output = None
    """path"""


class _ConcatGenerictsvComponent(Component):
    inputs: _ConcatGenerictsvInput
    outputs: _ConcatGenerictsvOutput
    runsettings: _CommandComponentRunsetting


_concat_generictsv = None


def concat_generictsv(
    input_1: Path = None,
    input_2: Path = None,
    input2hasheader: str = None,
) -> _ConcatGenerictsvComponent:
    """concat_generictsv
    
    :param input_1: path(optional)
    :type input_1: Path
    :param input_2: path(optional)
    :type input_2: Path
    :param input2hasheader: String (optional)
    :type input2hasheader: str
    :output output_out: path
    :type: output_out: Output
    """
    global _concat_generictsv
    if _concat_generictsv is None:
        _concat_generictsv = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/concat_generictsv/0.0.1/64d96c01-d024-42dc-aae3-b18e2e243fb5.spec.yaml")
    return _concat_generictsv(
            input_1=input_1,
            input_2=input_2,
            input2hasheader=input2hasheader,)


class _TsvToHtmlInput:
    tsv: Input = None
    """path(optional)"""
    generatehlinkforurl: str = None
    """String (optional)"""


class _TsvToHtmlOutput:
    htmlreport_out: Output = None
    """path"""


class _TsvToHtmlComponent(Component):
    inputs: _TsvToHtmlInput
    outputs: _TsvToHtmlOutput
    runsettings: _CommandComponentRunsetting


_tsv_to_html = None


def tsv_to_html(
    tsv: Path = None,
    generatehlinkforurl: str = None,
) -> _TsvToHtmlComponent:
    """tsv_to_html
    
    :param tsv: path(optional)
    :type tsv: Path
    :param generatehlinkforurl: String (optional)
    :type generatehlinkforurl: str
    :output htmlreport_out: path
    :type: htmlreport_out: Output
    """
    global _tsv_to_html
    if _tsv_to_html is None:
        _tsv_to_html = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/tsv_to_html/0.0.1/6ae4bfca-221c-4a32-9423-9a658fd3ba1c.spec.yaml")
    return _tsv_to_html(
            tsv=tsv,
            generatehlinkforurl=generatehlinkforurl,)


class _AttractionsConflationWebsiteSimilarityCalculationScopeModuleInput:
    master_attributes: Input = None
    """path(optional)"""
    master_candidate_pairs_filtered_stream: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _AttractionsConflationWebsiteSimilarityCalculationScopeModuleOutput:
    website_similarity_stream_out: Output = None
    """path"""


class _AttractionsConflationWebsiteSimilarityCalculationScopeModuleComponent(Component):
    inputs: _AttractionsConflationWebsiteSimilarityCalculationScopeModuleInput
    outputs: _AttractionsConflationWebsiteSimilarityCalculationScopeModuleOutput
    runsettings: _CommandComponentRunsetting


_attractions_conflation_website_similarity_calculation_scope_module = None


def attractions_conflation_website_similarity_calculation_scope_module(
    master_attributes: Path = None,
    master_candidate_pairs_filtered_stream: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _AttractionsConflationWebsiteSimilarityCalculationScopeModuleComponent:
    """attractions_conflation_website_similarity_calculation_scope_module
    
    :param master_attributes: path(optional)
    :type master_attributes: Path
    :param master_candidate_pairs_filtered_stream: path(optional)
    :type master_candidate_pairs_filtered_stream: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output website_similarity_stream_out: path
    :type: website_similarity_stream_out: Output
    """
    global _attractions_conflation_website_similarity_calculation_scope_module
    if _attractions_conflation_website_similarity_calculation_scope_module is None:
        _attractions_conflation_website_similarity_calculation_scope_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_conflation_website_similarity_calculation_scope_module/0.0.1/6f428994-c529-4386-9789-9725abed384e.spec.yaml")
    return _attractions_conflation_website_similarity_calculation_scope_module(
            master_attributes=master_attributes,
            master_candidate_pairs_filtered_stream=master_candidate_pairs_filtered_stream,
            vc=vc,
            scopeparams=scopeparams,)


class _AttractionsEntitySimilarityDataMergeScopeModuleInput:
    master_candidate_pairs_filtered_stream: Input = None
    """path(optional)"""
    location_similarity_stream: Input = None
    """path(optional)"""
    entity_type_similarity_stream: Input = None
    """path(optional)"""
    topics_similarity_stream: Input = None
    """path(optional)"""
    image_similarity_stream: Input = None
    """path(optional)"""
    name_similarity_stream: Input = None
    """path(optional)"""
    ner_json_similarity_stream: Input = None
    """path(optional)"""
    website_similarity_stream: Input = None
    """path(optional)"""
    phonenumber_similarity_stream: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _AttractionsEntitySimilarityDataMergeScopeModuleOutput:
    merged_similarity_stream_out: Output = None
    """path"""


class _AttractionsEntitySimilarityDataMergeScopeModuleComponent(Component):
    inputs: _AttractionsEntitySimilarityDataMergeScopeModuleInput
    outputs: _AttractionsEntitySimilarityDataMergeScopeModuleOutput
    runsettings: _CommandComponentRunsetting


_attractions_entity_similarity_data_merge_scope_module = None


def attractions_entity_similarity_data_merge_scope_module(
    master_candidate_pairs_filtered_stream: Path = None,
    location_similarity_stream: Path = None,
    entity_type_similarity_stream: Path = None,
    topics_similarity_stream: Path = None,
    image_similarity_stream: Path = None,
    name_similarity_stream: Path = None,
    ner_json_similarity_stream: Path = None,
    website_similarity_stream: Path = None,
    phonenumber_similarity_stream: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _AttractionsEntitySimilarityDataMergeScopeModuleComponent:
    """attractions_entity_similarity_data_merge_scope_module
    
    :param master_candidate_pairs_filtered_stream: path(optional)
    :type master_candidate_pairs_filtered_stream: Path
    :param location_similarity_stream: path(optional)
    :type location_similarity_stream: Path
    :param entity_type_similarity_stream: path(optional)
    :type entity_type_similarity_stream: Path
    :param topics_similarity_stream: path(optional)
    :type topics_similarity_stream: Path
    :param image_similarity_stream: path(optional)
    :type image_similarity_stream: Path
    :param name_similarity_stream: path(optional)
    :type name_similarity_stream: Path
    :param ner_json_similarity_stream: path(optional)
    :type ner_json_similarity_stream: Path
    :param website_similarity_stream: path(optional)
    :type website_similarity_stream: Path
    :param phonenumber_similarity_stream: path(optional)
    :type phonenumber_similarity_stream: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output merged_similarity_stream_out: path
    :type: merged_similarity_stream_out: Output
    """
    global _attractions_entity_similarity_data_merge_scope_module
    if _attractions_entity_similarity_data_merge_scope_module is None:
        _attractions_entity_similarity_data_merge_scope_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_entity_similarity_data_merge_scope_module/0.0.1/70d274f5-dde8-4d25-b90b-c0a12b432688.spec.yaml")
    return _attractions_entity_similarity_data_merge_scope_module(
            master_candidate_pairs_filtered_stream=master_candidate_pairs_filtered_stream,
            location_similarity_stream=location_similarity_stream,
            entity_type_similarity_stream=entity_type_similarity_stream,
            topics_similarity_stream=topics_similarity_stream,
            image_similarity_stream=image_similarity_stream,
            name_similarity_stream=name_similarity_stream,
            ner_json_similarity_stream=ner_json_similarity_stream,
            website_similarity_stream=website_similarity_stream,
            phonenumber_similarity_stream=phonenumber_similarity_stream,
            vc=vc,
            scopeparams=scopeparams,)


class _CopyAetherCosmosWithFixedDestinationInput:
    infile: Input = None
    """path(optional)"""
    destlocation: Input = None
    """path(optional)"""
    shouldoverrideifexists: str = None
    """String (optional)"""


class _CopyAetherCosmosWithFixedDestinationOutput:
    outfile_out: Output = None
    """path"""


class _CopyAetherCosmosWithFixedDestinationComponent(Component):
    inputs: _CopyAetherCosmosWithFixedDestinationInput
    outputs: _CopyAetherCosmosWithFixedDestinationOutput
    runsettings: _CommandComponentRunsetting


_copy_aether_cosmos_with_fixed_destination = None


def copy_aether_cosmos_with_fixed_destination(
    infile: Path = None,
    destlocation: Path = None,
    shouldoverrideifexists: str = None,
) -> _CopyAetherCosmosWithFixedDestinationComponent:
    """copy_aether_cosmos_with_fixed_destination
    
    :param infile: path(optional)
    :type infile: Path
    :param destlocation: path(optional)
    :type destlocation: Path
    :param shouldoverrideifexists: String (optional)
    :type shouldoverrideifexists: str
    :output outfile_out: path
    :type: outfile_out: Output
    """
    global _copy_aether_cosmos_with_fixed_destination
    if _copy_aether_cosmos_with_fixed_destination is None:
        _copy_aether_cosmos_with_fixed_destination = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/copy_aether_cosmos_with_fixed_destination/0.0.1/755ca473-df24-4aa1-aa88-603aa0a30e4a.spec.yaml")
    return _copy_aether_cosmos_with_fixed_destination(
            infile=infile,
            destlocation=destlocation,
            shouldoverrideifexists=shouldoverrideifexists,)


class _TopReducerSsInput:
    input: Input = None
    """path(optional)"""
    sortcol: str = None
    """String (optional)"""
    sortdir: str = None
    """String (optional)"""
    reducecol: str = None
    """String (optional)"""
    numtokeep: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _TopReducerSsOutput:
    output_out: Output = None
    """path"""


class _TopReducerSsComponent(Component):
    inputs: _TopReducerSsInput
    outputs: _TopReducerSsOutput
    runsettings: _CommandComponentRunsetting


_top_reducer_ss = None


def top_reducer_ss(
    input: Path = None,
    sortcol: str = None,
    sortdir: str = None,
    reducecol: str = None,
    numtokeep: str = None,
    vc: str = None,
) -> _TopReducerSsComponent:
    """top_reducer_ss
    
    :param input: path(optional)
    :type input: Path
    :param sortcol: String (optional)
    :type sortcol: str
    :param sortdir: String (optional)
    :type sortdir: str
    :param reducecol: String (optional)
    :type reducecol: str
    :param numtokeep: String (optional)
    :type numtokeep: str
    :param vc: String (optional)
    :type vc: str
    :output output_out: path
    :type: output_out: Output
    """
    global _top_reducer_ss
    if _top_reducer_ss is None:
        _top_reducer_ss = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/top_reducer_ss/0.0.1/767f4087-fc50-409e-90fc-bd0b102da143.spec.yaml")
    return _top_reducer_ss(
            input=input,
            sortcol=sortcol,
            sortdir=sortdir,
            reducecol=reducecol,
            numtokeep=numtokeep,
            vc=vc,)


class _Sstreamunion2Input:
    in1: Input = None
    """path(optional)"""
    in2: Input = None
    """path(optional)"""
    clusterbycolumn: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _Sstreamunion2Output:
    output_out: Output = None
    """path"""


class _Sstreamunion2Component(Component):
    inputs: _Sstreamunion2Input
    outputs: _Sstreamunion2Output
    runsettings: _CommandComponentRunsetting


_sstreamunion2 = None


def sstreamunion2(
    in1: Path = None,
    in2: Path = None,
    clusterbycolumn: str = None,
    vc: str = None,
) -> _Sstreamunion2Component:
    """sstreamunion2
    
    :param in1: path(optional)
    :type in1: Path
    :param in2: path(optional)
    :type in2: Path
    :param clusterbycolumn: String (optional)
    :type clusterbycolumn: str
    :param vc: String (optional)
    :type vc: str
    :output output_out: path
    :type: output_out: Output
    """
    global _sstreamunion2
    if _sstreamunion2 is None:
        _sstreamunion2 = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/sstreamunion2/0.0.1/779bb829-3e47-4c95-8d18-99745221c1d0.spec.yaml")
    return _sstreamunion2(
            in1=in1,
            in2=in2,
            clusterbycolumn=clusterbycolumn,
            vc=vc,)


class _AttractionsGroundTruthCandidatesAttributesGeneratorInput:
    master_candidates_output_stream: Input = None
    """path(optional)"""
    ground_truth_stream: Input = None
    """path(optional)"""
    ground_truth_domain: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _AttractionsGroundTruthCandidatesAttributesGeneratorOutput:
    ground_truth_candidates_attributes_stream_out: Output = None
    """path"""


class _AttractionsGroundTruthCandidatesAttributesGeneratorComponent(Component):
    inputs: _AttractionsGroundTruthCandidatesAttributesGeneratorInput
    outputs: _AttractionsGroundTruthCandidatesAttributesGeneratorOutput
    runsettings: _CommandComponentRunsetting


_attractions_ground_truth_candidates_attributes_generator = None


def attractions_ground_truth_candidates_attributes_generator(
    master_candidates_output_stream: Path = None,
    ground_truth_stream: Path = None,
    ground_truth_domain: str = None,
    vc: str = None,
) -> _AttractionsGroundTruthCandidatesAttributesGeneratorComponent:
    """attractions_ground_truth_candidates_attributes_generator
    
    :param master_candidates_output_stream: path(optional)
    :type master_candidates_output_stream: Path
    :param ground_truth_stream: path(optional)
    :type ground_truth_stream: Path
    :param ground_truth_domain: String (optional)
    :type ground_truth_domain: str
    :param vc: String (optional)
    :type vc: str
    :output ground_truth_candidates_attributes_stream_out: path
    :type: ground_truth_candidates_attributes_stream_out: Output
    """
    global _attractions_ground_truth_candidates_attributes_generator
    if _attractions_ground_truth_candidates_attributes_generator is None:
        _attractions_ground_truth_candidates_attributes_generator = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_ground_truth_candidates_attributes_generator/0.0.1/7af6619b-1c02-4faa-ba95-cd98a7ae020f.spec.yaml")
    return _attractions_ground_truth_candidates_attributes_generator(
            master_candidates_output_stream=master_candidates_output_stream,
            ground_truth_stream=ground_truth_stream,
            ground_truth_domain=ground_truth_domain,
            vc=vc,)


class _GeneralselectcosmosInput:
    in1: Input = None
    """path(optional)"""
    in2: Input = None
    """path(optional)"""
    in3: Input = None
    """path(optional)"""
    in4: Input = None
    """path(optional)"""
    extractcols1: str = None
    """String (optional)"""
    extractcols2: str = None
    """String (optional)"""
    extractcols3: str = None
    """String (optional)"""
    extractcols4: str = None
    """String (optional)"""
    select1: str = None
    """String (optional)"""
    select2: str = None
    """String (optional)"""
    select3: str = None
    """String (optional)"""
    select4: str = None
    """String (optional)"""
    select5: str = None
    """String (optional)"""
    ssclause: str = None
    """String (optional)"""
    tsvclause: str = None
    """String (optional)"""
    resourcestmts: str = None
    """String (optional)"""
    referencestmts: str = None
    """String (optional)"""
    comment: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _GeneralselectcosmosOutput:
    outputstream_out: Output = None
    """path"""
    outputtsv_out: Output = None
    """path"""
    outputcount_out: Output = None
    """path"""


class _GeneralselectcosmosComponent(Component):
    inputs: _GeneralselectcosmosInput
    outputs: _GeneralselectcosmosOutput
    runsettings: _CommandComponentRunsetting


_generalselectcosmos = None


def generalselectcosmos(
    in1: Path = None,
    in2: Path = None,
    in3: Path = None,
    in4: Path = None,
    extractcols1: str = None,
    extractcols2: str = None,
    extractcols3: str = None,
    extractcols4: str = None,
    select1: str = None,
    select2: str = None,
    select3: str = None,
    select4: str = None,
    select5: str = None,
    ssclause: str = None,
    tsvclause: str = None,
    resourcestmts: str = None,
    referencestmts: str = None,
    comment: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _GeneralselectcosmosComponent:
    """generalselectcosmos
    
    :param in1: path(optional)
    :type in1: Path
    :param in2: path(optional)
    :type in2: Path
    :param in3: path(optional)
    :type in3: Path
    :param in4: path(optional)
    :type in4: Path
    :param extractcols1: String (optional)
    :type extractcols1: str
    :param extractcols2: String (optional)
    :type extractcols2: str
    :param extractcols3: String (optional)
    :type extractcols3: str
    :param extractcols4: String (optional)
    :type extractcols4: str
    :param select1: String (optional)
    :type select1: str
    :param select2: String (optional)
    :type select2: str
    :param select3: String (optional)
    :type select3: str
    :param select4: String (optional)
    :type select4: str
    :param select5: String (optional)
    :type select5: str
    :param ssclause: String (optional)
    :type ssclause: str
    :param tsvclause: String (optional)
    :type tsvclause: str
    :param resourcestmts: String (optional)
    :type resourcestmts: str
    :param referencestmts: String (optional)
    :type referencestmts: str
    :param comment: String (optional)
    :type comment: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output outputstream_out: path
    :type: outputstream_out: Output
    :output outputtsv_out: path
    :type: outputtsv_out: Output
    :output outputcount_out: path
    :type: outputcount_out: Output
    """
    global _generalselectcosmos
    if _generalselectcosmos is None:
        _generalselectcosmos = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/generalselectcosmos/0.0.1/899c10b2-173d-4780-9e06-497f8f017ead.spec.yaml")
    return _generalselectcosmos(
            in1=in1,
            in2=in2,
            in3=in3,
            in4=in4,
            extractcols1=extractcols1,
            extractcols2=extractcols2,
            extractcols3=extractcols3,
            extractcols4=extractcols4,
            select1=select1,
            select2=select2,
            select3=select3,
            select4=select4,
            select5=select5,
            ssclause=ssclause,
            tsvclause=tsvclause,
            resourcestmts=resourcestmts,
            referencestmts=referencestmts,
            comment=comment,
            vc=vc,
            scopeparams=scopeparams,)


class _CreatecosmospathfreelyInput:
    vc: str = None
    """String (optional)"""
    relativepath: str = None
    """String (optional)"""


class _CreatecosmospathfreelyOutput:
    createdpath_out: Output = None
    """path"""


class _CreatecosmospathfreelyComponent(Component):
    inputs: _CreatecosmospathfreelyInput
    outputs: _CreatecosmospathfreelyOutput
    runsettings: _CommandComponentRunsetting


_createcosmospathfreely = None


def createcosmospathfreely(
    vc: str = None,
    relativepath: str = None,
) -> _CreatecosmospathfreelyComponent:
    """createcosmospathfreely
    
    :param vc: String (optional)
    :type vc: str
    :param relativepath: String (optional)
    :type relativepath: str
    :output createdpath_out: path
    :type: createdpath_out: Output
    """
    global _createcosmospathfreely
    if _createcosmospathfreely is None:
        _createcosmospathfreely = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/createcosmospathfreely/0.0.1/8b790039-2e6c-4987-9b19-c03c7e6ae83b.spec.yaml")
    return _createcosmospathfreely(
            vc=vc,
            relativepath=relativepath,)


class _EntityGraphGenerationInput:
    inputfile: Input = None
    """path(optional)"""


class _EntityGraphGenerationOutput:
    outputfile_out: Output = None
    """path"""
    outputfile2_out: Output = None
    """path"""
    outputfile3_out: Output = None
    """path"""


class _EntityGraphGenerationComponent(Component):
    inputs: _EntityGraphGenerationInput
    outputs: _EntityGraphGenerationOutput
    runsettings: _CommandComponentRunsetting


_entity_graph_generation = None


def entity_graph_generation(
    inputfile: Path = None,
) -> _EntityGraphGenerationComponent:
    """entity_graph_generation
    
    :param inputfile: path(optional)
    :type inputfile: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    :output outputfile2_out: path
    :type: outputfile2_out: Output
    :output outputfile3_out: path
    :type: outputfile3_out: Output
    """
    global _entity_graph_generation
    if _entity_graph_generation is None:
        _entity_graph_generation = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/entity_graph_generation/0.0.1/8c666d0d-4d74-43b8-b101-b858b89bc44c.spec.yaml")
    return _entity_graph_generation(
            inputfile=inputfile,)


class _BuildentitynamedictionaryInput:
    inputfile: Input = None
    """path(optional)"""


class _BuildentitynamedictionaryOutput:
    outputfile1_out: Output = None
    """path"""
    outputfile2_out: Output = None
    """path"""


class _BuildentitynamedictionaryComponent(Component):
    inputs: _BuildentitynamedictionaryInput
    outputs: _BuildentitynamedictionaryOutput
    runsettings: _CommandComponentRunsetting


_buildentitynamedictionary = None


def buildentitynamedictionary(
    inputfile: Path = None,
) -> _BuildentitynamedictionaryComponent:
    """buildentitynamedictionary
    
    :param inputfile: path(optional)
    :type inputfile: Path
    :output outputfile1_out: path
    :type: outputfile1_out: Output
    :output outputfile2_out: path
    :type: outputfile2_out: Output
    """
    global _buildentitynamedictionary
    if _buildentitynamedictionary is None:
        _buildentitynamedictionary = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/buildentitynamedictionary/0.0.1/8dc02c3e-6ccc-45a4-9b88-4a4ab1c38316.spec.yaml")
    return _buildentitynamedictionary(
            inputfile=inputfile,)


class _NamepairsimilaritylookuptableupdatesInput:
    inputfile1: Input = None
    """path(optional)"""


class _NamepairsimilaritylookuptableupdatesOutput:
    outputfile1_out: Output = None
    """path"""


class _NamepairsimilaritylookuptableupdatesComponent(Component):
    inputs: _NamepairsimilaritylookuptableupdatesInput
    outputs: _NamepairsimilaritylookuptableupdatesOutput
    runsettings: _CommandComponentRunsetting


_namepairsimilaritylookuptableupdates = None


def namepairsimilaritylookuptableupdates(
    inputfile1: Path = None,
) -> _NamepairsimilaritylookuptableupdatesComponent:
    """namepairsimilaritylookuptableupdates
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :output outputfile1_out: path
    :type: outputfile1_out: Output
    """
    global _namepairsimilaritylookuptableupdates
    if _namepairsimilaritylookuptableupdates is None:
        _namepairsimilaritylookuptableupdates = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/namepairsimilaritylookuptableupdates/0.0.1/92c343a8-ecf4-4e1d-b4bd-f7236ace6de3.spec.yaml")
    return _namepairsimilaritylookuptableupdates(
            inputfile1=inputfile1,)


class _GeneratetrippleRecordTaWikiAlltrailsInput:
    record_alltrails: Input = None
    """path(optional)"""
    record_ta: Input = None
    """path(optional)"""
    record_wiki: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""


class _GeneratetrippleRecordTaWikiAlltrailsOutput:
    record_ta_wiki_alltrails_out: Output = None
    """path"""


class _GeneratetrippleRecordTaWikiAlltrailsComponent(Component):
    inputs: _GeneratetrippleRecordTaWikiAlltrailsInput
    outputs: _GeneratetrippleRecordTaWikiAlltrailsOutput
    runsettings: _CommandComponentRunsetting


_generatetripple_record_ta_wiki_alltrails = None


def generatetripple_record_ta_wiki_alltrails(
    record_alltrails: Path = None,
    record_ta: Path = None,
    record_wiki: Path = None,
    vc: str = None,
) -> _GeneratetrippleRecordTaWikiAlltrailsComponent:
    """generatetripple_record_ta_wiki_alltrails
    
    :param record_alltrails: path(optional)
    :type record_alltrails: Path
    :param record_ta: path(optional)
    :type record_ta: Path
    :param record_wiki: path(optional)
    :type record_wiki: Path
    :param vc: String (optional)
    :type vc: str
    :output record_ta_wiki_alltrails_out: path
    :type: record_ta_wiki_alltrails_out: Output
    """
    global _generatetripple_record_ta_wiki_alltrails
    if _generatetripple_record_ta_wiki_alltrails is None:
        _generatetripple_record_ta_wiki_alltrails = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/generatetripple_record_ta_wiki_alltrails/0.0.1/968059e2-027f-4e83-87f6-c3a770e8b1ff.spec.yaml")
    return _generatetripple_record_ta_wiki_alltrails(
            record_alltrails=record_alltrails,
            record_ta=record_ta,
            record_wiki=record_wiki,
            vc=vc,)


class _AttractionsEntityConflationImageUrlExtractorScopeModuleInput:
    master_features_stream: Input = None
    """path(optional)"""
    max_image_count: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _AttractionsEntityConflationImageUrlExtractorScopeModuleOutput:
    image_urls_out: Output = None
    """path"""


class _AttractionsEntityConflationImageUrlExtractorScopeModuleComponent(Component):
    inputs: _AttractionsEntityConflationImageUrlExtractorScopeModuleInput
    outputs: _AttractionsEntityConflationImageUrlExtractorScopeModuleOutput
    runsettings: _CommandComponentRunsetting


_attractions_entity_conflation_image_url_extractor_scope_module = None


def attractions_entity_conflation_image_url_extractor_scope_module(
    master_features_stream: Path = None,
    max_image_count: str = None,
    vc: str = None,
) -> _AttractionsEntityConflationImageUrlExtractorScopeModuleComponent:
    """attractions_entity_conflation_image_url_extractor_scope_module
    
    :param master_features_stream: path(optional)
    :type master_features_stream: Path
    :param max_image_count: String (optional)
    :type max_image_count: str
    :param vc: String (optional)
    :type vc: str
    :output image_urls_out: path
    :type: image_urls_out: Output
    """
    global _attractions_entity_conflation_image_url_extractor_scope_module
    if _attractions_entity_conflation_image_url_extractor_scope_module is None:
        _attractions_entity_conflation_image_url_extractor_scope_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_entity_conflation_image_url_extractor_scope_module/0.0.1/9aa5eb78-a73c-4f50-9904-ba33ca63bfd8.spec.yaml")
    return _attractions_entity_conflation_image_url_extractor_scope_module(
            master_features_stream=master_features_stream,
            max_image_count=max_image_count,
            vc=vc,)


class _EntityConflationDataStatusMonitorInput:
    master_attr: Input = None
    """path(optional)"""
    master_pairs: Input = None
    """path(optional)"""
    merged_sim: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _EntityConflationDataStatusMonitorOutput:
    stats_ecis_dm_out: Output = None
    """path"""
    stats_ecis_out: Output = None
    """path"""


class _EntityConflationDataStatusMonitorComponent(Component):
    inputs: _EntityConflationDataStatusMonitorInput
    outputs: _EntityConflationDataStatusMonitorOutput
    runsettings: _CommandComponentRunsetting


_entity_conflation_data_status_monitor = None


def entity_conflation_data_status_monitor(
    master_attr: Path = None,
    master_pairs: Path = None,
    merged_sim: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _EntityConflationDataStatusMonitorComponent:
    """entity_conflation_data_status_monitor
    
    :param master_attr: path(optional)
    :type master_attr: Path
    :param master_pairs: path(optional)
    :type master_pairs: Path
    :param merged_sim: path(optional)
    :type merged_sim: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output stats_ecis_dm_out: path
    :type: stats_ecis_dm_out: Output
    :output stats_ecis_out: path
    :type: stats_ecis_out: Output
    """
    global _entity_conflation_data_status_monitor
    if _entity_conflation_data_status_monitor is None:
        _entity_conflation_data_status_monitor = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/entity_conflation_data_status_monitor/0.0.1/9b7c1236-c479-49d4-9ad2-ca838bd451d2.spec.yaml")
    return _entity_conflation_data_status_monitor(
            master_attr=master_attr,
            master_pairs=master_pairs,
            merged_sim=merged_sim,
            vc=vc,
            scopeparams=scopeparams,)


class _LandmarkDatacollectionUtilsRmacextractorOutingsVcInput:
    inputimagebinaryfile: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _LandmarkDatacollectionUtilsRmacextractorOutingsVcOutput:
    outputfeaturefiletsv_out: Output = None
    """path"""
    statsfiletsv_out: Output = None
    """path"""
    outputfeaturefiless_out: Output = None
    """path"""


class _LandmarkDatacollectionUtilsRmacextractorOutingsVcComponent(Component):
    inputs: _LandmarkDatacollectionUtilsRmacextractorOutingsVcInput
    outputs: _LandmarkDatacollectionUtilsRmacextractorOutingsVcOutput
    runsettings: _CommandComponentRunsetting


_landmark_datacollection_utils_rmacextractor_outings_vc = None


def landmark_datacollection_utils_rmacextractor_outings_vc(
    inputimagebinaryfile: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _LandmarkDatacollectionUtilsRmacextractorOutingsVcComponent:
    """landmark_datacollection_utils_rmacextractor_outings_vc
    
    :param inputimagebinaryfile: path(optional)
    :type inputimagebinaryfile: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output outputfeaturefiletsv_out: path
    :type: outputfeaturefiletsv_out: Output
    :output statsfiletsv_out: path
    :type: statsfiletsv_out: Output
    :output outputfeaturefiless_out: path
    :type: outputfeaturefiless_out: Output
    """
    global _landmark_datacollection_utils_rmacextractor_outings_vc
    if _landmark_datacollection_utils_rmacextractor_outings_vc is None:
        _landmark_datacollection_utils_rmacextractor_outings_vc = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/landmark_datacollection_utils_rmacextractor_outings_vc/0.0.1/9e479cf5-0b15-49c2-81cf-3b5b45945984.spec.yaml")
    return _landmark_datacollection_utils_rmacextractor_outings_vc(
            inputimagebinaryfile=inputimagebinaryfile,
            vc=vc,
            scopeparams=scopeparams,)


class _AttractionsConflationPhoneNumberSimilarityCalculationScopeModuleInput:
    master_attributes: Input = None
    """path(optional)"""
    master_candidate_pairs_filtered_stream: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _AttractionsConflationPhoneNumberSimilarityCalculationScopeModuleOutput:
    phonenumber_similarity_stream_out: Output = None
    """path"""


class _AttractionsConflationPhoneNumberSimilarityCalculationScopeModuleComponent(Component):
    inputs: _AttractionsConflationPhoneNumberSimilarityCalculationScopeModuleInput
    outputs: _AttractionsConflationPhoneNumberSimilarityCalculationScopeModuleOutput
    runsettings: _CommandComponentRunsetting


_attractions_conflation_phone_number_similarity_calculation_scope_module = None


def attractions_conflation_phone_number_similarity_calculation_scope_module(
    master_attributes: Path = None,
    master_candidate_pairs_filtered_stream: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _AttractionsConflationPhoneNumberSimilarityCalculationScopeModuleComponent:
    """attractions_conflation_phone_number_similarity_calculation_scope_module
    
    :param master_attributes: path(optional)
    :type master_attributes: Path
    :param master_candidate_pairs_filtered_stream: path(optional)
    :type master_candidate_pairs_filtered_stream: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output phonenumber_similarity_stream_out: path
    :type: phonenumber_similarity_stream_out: Output
    """
    global _attractions_conflation_phone_number_similarity_calculation_scope_module
    if _attractions_conflation_phone_number_similarity_calculation_scope_module is None:
        _attractions_conflation_phone_number_similarity_calculation_scope_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_conflation_phone_number_similarity_calculation_scope_module/0.0.1/a0e570d8-6abd-4862-9b9d-f9e2697abd56.spec.yaml")
    return _attractions_conflation_phone_number_similarity_calculation_scope_module(
            master_attributes=master_attributes,
            master_candidate_pairs_filtered_stream=master_candidate_pairs_filtered_stream,
            vc=vc,
            scopeparams=scopeparams,)


class _OutingsTaSidMappingBvtInput:
    ta_ground_truth: Input = None
    """path(optional)"""
    bvt_file: Input = None
    """path(optional)"""
    ta_sid_mapping: Input = None
    """path(optional)"""
    date: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsTaSidMappingBvtOutput:
    bvt_results_out: Output = None
    """path"""
    bvt_stat_out: Output = None
    """path"""


class _OutingsTaSidMappingBvtComponent(Component):
    inputs: _OutingsTaSidMappingBvtInput
    outputs: _OutingsTaSidMappingBvtOutput
    runsettings: _CommandComponentRunsetting


_outings_ta_sid_mapping_bvt = None


def outings_ta_sid_mapping_bvt(
    ta_ground_truth: Path = None,
    bvt_file: Path = None,
    ta_sid_mapping: Path = None,
    date: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsTaSidMappingBvtComponent:
    """outings_ta_sid_mapping_bvt
    
    :param ta_ground_truth: path(optional)
    :type ta_ground_truth: Path
    :param bvt_file: path(optional)
    :type bvt_file: Path
    :param ta_sid_mapping: path(optional)
    :type ta_sid_mapping: Path
    :param date: String (optional)
    :type date: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output bvt_results_out: path
    :type: bvt_results_out: Output
    :output bvt_stat_out: path
    :type: bvt_stat_out: Output
    """
    global _outings_ta_sid_mapping_bvt
    if _outings_ta_sid_mapping_bvt is None:
        _outings_ta_sid_mapping_bvt = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_ta_sid_mapping_bvt/0.0.1/a2da318f-7e92-4e12-80f8-07aff02ffcf9.spec.yaml")
    return _outings_ta_sid_mapping_bvt(
            ta_ground_truth=ta_ground_truth,
            bvt_file=bvt_file,
            ta_sid_mapping=ta_sid_mapping,
            date=date,
            vc=vc,
            scopeparams=scopeparams,)


class _CosmosSplit1TsvTo5Input:
    inputfile: Input = None
    """path(optional)"""
    scopeparams: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _CosmosSplit1TsvTo5Output:
    part0_out: Output = None
    """path"""
    part1_out: Output = None
    """path"""
    part2_out: Output = None
    """path"""
    part3_out: Output = None
    """path"""
    part4_out: Output = None
    """path"""


class _CosmosSplit1TsvTo5Component(Component):
    inputs: _CosmosSplit1TsvTo5Input
    outputs: _CosmosSplit1TsvTo5Output
    runsettings: _CommandComponentRunsetting


_cosmos_split_1_tsv_to_5 = None


def cosmos_split_1_tsv_to_5(
    inputfile: Path = None,
    scopeparams: str = None,
    vc: str = None,
) -> _CosmosSplit1TsvTo5Component:
    """cosmos_split_1_tsv_to_5
    
    :param inputfile: path(optional)
    :type inputfile: Path
    :param scopeparams: String (optional)
    :type scopeparams: str
    :param vc: String (optional)
    :type vc: str
    :output part0_out: path
    :type: part0_out: Output
    :output part1_out: path
    :type: part1_out: Output
    :output part2_out: path
    :type: part2_out: Output
    :output part3_out: path
    :type: part3_out: Output
    :output part4_out: path
    :type: part4_out: Output
    """
    global _cosmos_split_1_tsv_to_5
    if _cosmos_split_1_tsv_to_5 is None:
        _cosmos_split_1_tsv_to_5 = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/cosmos_split_1_tsv_to_5/0.0.1/a82f279e-c6cf-47fb-9f07-f8540511c325.spec.yaml")
    return _cosmos_split_1_tsv_to_5(
            inputfile=inputfile,
            scopeparams=scopeparams,
            vc=vc,)


class _AttractionsConflationNamedEntityRecognitionSimilarityCalcuationScopeModuleInput:
    master_attributes: Input = None
    """path(optional)"""
    master_candidate_pairs_filtered_stream: Input = None
    """path(optional)"""
    deep_model: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _AttractionsConflationNamedEntityRecognitionSimilarityCalcuationScopeModuleOutput:
    ner_json_similarity_stream_out: Output = None
    """path"""


class _AttractionsConflationNamedEntityRecognitionSimilarityCalcuationScopeModuleComponent(Component):
    inputs: _AttractionsConflationNamedEntityRecognitionSimilarityCalcuationScopeModuleInput
    outputs: _AttractionsConflationNamedEntityRecognitionSimilarityCalcuationScopeModuleOutput
    runsettings: _CommandComponentRunsetting


_attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module = None


def attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module(
    master_attributes: Path = None,
    master_candidate_pairs_filtered_stream: Path = None,
    deep_model: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _AttractionsConflationNamedEntityRecognitionSimilarityCalcuationScopeModuleComponent:
    """attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module
    
    :param master_attributes: path(optional)
    :type master_attributes: Path
    :param master_candidate_pairs_filtered_stream: path(optional)
    :type master_candidate_pairs_filtered_stream: Path
    :param deep_model: String (optional)
    :type deep_model: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output ner_json_similarity_stream_out: path
    :type: ner_json_similarity_stream_out: Output
    """
    global _attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module
    if _attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module is None:
        _attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module/0.0.1/a89410bb-088d-4502-ab62-70273e661c81.spec.yaml")
    return _attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module(
            master_attributes=master_attributes,
            master_candidate_pairs_filtered_stream=master_candidate_pairs_filtered_stream,
            deep_model=deep_model,
            vc=vc,
            scopeparams=scopeparams,)


class _ConditionalPassthroughAnyfileInput:
    input: Input = None
    """path(optional)"""
    control: Input = None
    """path(optional)"""


class _ConditionalPassthroughAnyfileOutput:
    output_out: Output = None
    """path"""


class _ConditionalPassthroughAnyfileComponent(Component):
    inputs: _ConditionalPassthroughAnyfileInput
    outputs: _ConditionalPassthroughAnyfileOutput
    runsettings: _CommandComponentRunsetting


_conditional_passthrough_anyfile = None


def conditional_passthrough_anyfile(
    input: Path = None,
    control: Path = None,
) -> _ConditionalPassthroughAnyfileComponent:
    """conditional_passthrough_anyfile
    
    :param input: path(optional)
    :type input: Path
    :param control: path(optional)
    :type control: Path
    :output output_out: path
    :type: output_out: Output
    """
    global _conditional_passthrough_anyfile
    if _conditional_passthrough_anyfile is None:
        _conditional_passthrough_anyfile = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/conditional_passthrough_anyfile/0.0.1/ac920e0c-faa7-4648-963e-40b33b84c842.spec.yaml")
    return _conditional_passthrough_anyfile(
            input=input,
            control=control,)


class _UploadToVcWithInputsGenerictsvInput:
    tsv: Input = None
    """path(optional)"""
    destinationpath: Input = None
    """path(optional)"""
    shouldrespectlineboundaries: str = None
    """String (optional)"""
    overwrite: str = None
    """String (optional)"""
    expiration: str = None
    """String (optional)"""
    datamanagementenabled: str = None
    """String (optional)"""


class _UploadToVcWithInputsGenerictsvOutput:
    destinationpath_out: Output = None
    """path"""


class _UploadToVcWithInputsGenerictsvComponent(Component):
    inputs: _UploadToVcWithInputsGenerictsvInput
    outputs: _UploadToVcWithInputsGenerictsvOutput
    runsettings: _CommandComponentRunsetting


_upload_to_vc_with_inputs_generictsv = None


def upload_to_vc_with_inputs_generictsv(
    tsv: Path = None,
    destinationpath: Path = None,
    shouldrespectlineboundaries: str = None,
    overwrite: str = None,
    expiration: str = None,
    datamanagementenabled: str = None,
) -> _UploadToVcWithInputsGenerictsvComponent:
    """upload_to_vc_with_inputs_generictsv
    
    :param tsv: path(optional)
    :type tsv: Path
    :param destinationpath: path(optional)
    :type destinationpath: Path
    :param shouldrespectlineboundaries: String (optional)
    :type shouldrespectlineboundaries: str
    :param overwrite: String (optional)
    :type overwrite: str
    :param expiration: String (optional)
    :type expiration: str
    :param datamanagementenabled: String (optional)
    :type datamanagementenabled: str
    :output destinationpath_out: path
    :type: destinationpath_out: Output
    """
    global _upload_to_vc_with_inputs_generictsv
    if _upload_to_vc_with_inputs_generictsv is None:
        _upload_to_vc_with_inputs_generictsv = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/upload_to_vc_with_inputs_generictsv/0.0.1/b00c28f1-8006-4951-a766-2c3b0c61cf73.spec.yaml")
    return _upload_to_vc_with_inputs_generictsv(
            tsv=tsv,
            destinationpath=destinationpath,
            shouldrespectlineboundaries=shouldrespectlineboundaries,
            overwrite=overwrite,
            expiration=expiration,
            datamanagementenabled=datamanagementenabled,)


class _OutingsEntityConflationPublishingStatisticsInput:
    record_triples: Input = None
    """path(optional)"""
    master_attr: Input = None
    """path(optional)"""
    ta_satori_links: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsEntityConflationPublishingStatisticsOutput:
    stats_ss_out: Output = None
    """path"""
    stats_tsv_out: Output = None
    """path"""


class _OutingsEntityConflationPublishingStatisticsComponent(Component):
    inputs: _OutingsEntityConflationPublishingStatisticsInput
    outputs: _OutingsEntityConflationPublishingStatisticsOutput
    runsettings: _CommandComponentRunsetting


_outings_entity_conflation_publishing_statistics = None


def outings_entity_conflation_publishing_statistics(
    record_triples: Path = None,
    master_attr: Path = None,
    ta_satori_links: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsEntityConflationPublishingStatisticsComponent:
    """outings_entity_conflation_publishing_statistics
    
    :param record_triples: path(optional)
    :type record_triples: Path
    :param master_attr: path(optional)
    :type master_attr: Path
    :param ta_satori_links: path(optional)
    :type ta_satori_links: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output stats_ss_out: path
    :type: stats_ss_out: Output
    :output stats_tsv_out: path
    :type: stats_tsv_out: Output
    """
    global _outings_entity_conflation_publishing_statistics
    if _outings_entity_conflation_publishing_statistics is None:
        _outings_entity_conflation_publishing_statistics = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_entity_conflation_publishing_statistics/0.0.1/b894bb2b-e6ca-47ac-94af-8868b0c87ef9.spec.yaml")
    return _outings_entity_conflation_publishing_statistics(
            record_triples=record_triples,
            master_attr=master_attr,
            ta_satori_links=ta_satori_links,
            vc=vc,
            scopeparams=scopeparams,)


class _FlattenwikiclustersInput:
    inputfile1: Input = None
    """path(optional)"""


class _FlattenwikiclustersOutput:
    outputfile_out: Output = None
    """path"""


class _FlattenwikiclustersComponent(Component):
    inputs: _FlattenwikiclustersInput
    outputs: _FlattenwikiclustersOutput
    runsettings: _CommandComponentRunsetting


_flattenwikiclusters = None


def flattenwikiclusters(
    inputfile1: Path = None,
) -> _FlattenwikiclustersComponent:
    """flattenwikiclusters
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _flattenwikiclusters
    if _flattenwikiclusters is None:
        _flattenwikiclusters = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/flattenwikiclusters/0.0.1/b9239160-f299-4b14-a9ff-0fd92474bfcc.spec.yaml")
    return _flattenwikiclusters(
            inputfile1=inputfile1,)


class _CopyIntermediateDataTsvToSpecificVcWithOverwriteInput:
    tsv: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    relativepath: str = None
    """String (optional)"""
    overwrite: str = None
    """String (optional)"""
    datamanagementenabled: str = None
    """String (optional)"""
    expiration: str = None
    """String (optional)"""


class _CopyIntermediateDataTsvToSpecificVcWithOverwriteOutput:
    destinationpath_out: Output = None
    """path"""


class _CopyIntermediateDataTsvToSpecificVcWithOverwriteComponent(Component):
    inputs: _CopyIntermediateDataTsvToSpecificVcWithOverwriteInput
    outputs: _CopyIntermediateDataTsvToSpecificVcWithOverwriteOutput
    runsettings: _CommandComponentRunsetting


_copy_intermediate_data_tsv_to_specific_vc_with_overwrite = None


def copy_intermediate_data_tsv_to_specific_vc_with_overwrite(
    tsv: Path = None,
    vc: str = None,
    relativepath: str = None,
    overwrite: str = None,
    datamanagementenabled: str = None,
    expiration: str = None,
) -> _CopyIntermediateDataTsvToSpecificVcWithOverwriteComponent:
    """copy_intermediate_data_tsv_to_specific_vc_with_overwrite
    
    :param tsv: path(optional)
    :type tsv: Path
    :param vc: String (optional)
    :type vc: str
    :param relativepath: String (optional)
    :type relativepath: str
    :param overwrite: String (optional)
    :type overwrite: str
    :param datamanagementenabled: String (optional)
    :type datamanagementenabled: str
    :param expiration: String (optional)
    :type expiration: str
    :output destinationpath_out: path
    :type: destinationpath_out: Output
    """
    global _copy_intermediate_data_tsv_to_specific_vc_with_overwrite
    if _copy_intermediate_data_tsv_to_specific_vc_with_overwrite is None:
        _copy_intermediate_data_tsv_to_specific_vc_with_overwrite = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/copy_intermediate_data_tsv_to_specific_vc_with_overwrite/0.0.1/bbe5778b-3ae0-4ebd-ac2a-bda479c97d20.spec.yaml")
    return _copy_intermediate_data_tsv_to_specific_vc_with_overwrite(
            tsv=tsv,
            vc=vc,
            relativepath=relativepath,
            overwrite=overwrite,
            datamanagementenabled=datamanagementenabled,
            expiration=expiration,)


class _OutingDistanceMetricInput:
    input_ss: Input = None
    """path(optional)"""
    lat1: str = None
    """String (optional)"""
    lon1: str = None
    """String (optional)"""
    lat2: str = None
    """String (optional)"""
    lon2: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingDistanceMetricOutput:
    output_ss_out: Output = None
    """path"""


class _OutingDistanceMetricComponent(Component):
    inputs: _OutingDistanceMetricInput
    outputs: _OutingDistanceMetricOutput
    runsettings: _CommandComponentRunsetting


_outing_distance_metric = None


def outing_distance_metric(
    input_ss: Path = None,
    lat1: str = None,
    lon1: str = None,
    lat2: str = None,
    lon2: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingDistanceMetricComponent:
    """outing_distance_metric
    
    :param input_ss: path(optional)
    :type input_ss: Path
    :param lat1: String (optional)
    :type lat1: str
    :param lon1: String (optional)
    :type lon1: str
    :param lat2: String (optional)
    :type lat2: str
    :param lon2: String (optional)
    :type lon2: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output output_ss_out: path
    :type: output_ss_out: Output
    """
    global _outing_distance_metric
    if _outing_distance_metric is None:
        _outing_distance_metric = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outing_distance_metric/0.0.1/be04f4dd-0068-4277-97c1-b444305d3bb2.spec.yaml")
    return _outing_distance_metric(
            input_ss=input_ss,
            lat1=lat1,
            lon1=lon1,
            lat2=lat2,
            lon2=lon2,
            vc=vc,
            scopeparams=scopeparams,)


class _CastAnyfileToGenerictsvInput:
    input: Input = None
    """path(optional)"""


class _CastAnyfileToGenerictsvOutput:
    outputtsv_out: Output = None
    """path"""


class _CastAnyfileToGenerictsvComponent(Component):
    inputs: _CastAnyfileToGenerictsvInput
    outputs: _CastAnyfileToGenerictsvOutput
    runsettings: _CommandComponentRunsetting


_cast_anyfile_to_generictsv = None


def cast_anyfile_to_generictsv(
    input: Path = None,
) -> _CastAnyfileToGenerictsvComponent:
    """cast_anyfile_to_generictsv
    
    :param input: path(optional)
    :type input: Path
    :output outputtsv_out: path
    :type: outputtsv_out: Output
    """
    global _cast_anyfile_to_generictsv
    if _cast_anyfile_to_generictsv is None:
        _cast_anyfile_to_generictsv = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/cast_anyfile_to_generictsv/0.0.1/c03b0a34-5b9e-42a7-bd47-e5c1d2cb0b2c.spec.yaml")
    return _cast_anyfile_to_generictsv(
            input=input,)


class _AttractionsConflationEntityTypeSimilarityCalculationScopeModuleInput:
    master_attributes: Input = None
    """path(optional)"""
    master_candidate_pairs_filtered_stream: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _AttractionsConflationEntityTypeSimilarityCalculationScopeModuleOutput:
    entity_type_similarity_stream_out: Output = None
    """path"""


class _AttractionsConflationEntityTypeSimilarityCalculationScopeModuleComponent(Component):
    inputs: _AttractionsConflationEntityTypeSimilarityCalculationScopeModuleInput
    outputs: _AttractionsConflationEntityTypeSimilarityCalculationScopeModuleOutput
    runsettings: _CommandComponentRunsetting


_attractions_conflation_entity_type_similarity_calculation_scope_module = None


def attractions_conflation_entity_type_similarity_calculation_scope_module(
    master_attributes: Path = None,
    master_candidate_pairs_filtered_stream: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _AttractionsConflationEntityTypeSimilarityCalculationScopeModuleComponent:
    """attractions_conflation_entity_type_similarity_calculation_scope_module
    
    :param master_attributes: path(optional)
    :type master_attributes: Path
    :param master_candidate_pairs_filtered_stream: path(optional)
    :type master_candidate_pairs_filtered_stream: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output entity_type_similarity_stream_out: path
    :type: entity_type_similarity_stream_out: Output
    """
    global _attractions_conflation_entity_type_similarity_calculation_scope_module
    if _attractions_conflation_entity_type_similarity_calculation_scope_module is None:
        _attractions_conflation_entity_type_similarity_calculation_scope_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_conflation_entity_type_similarity_calculation_scope_module/0.0.1/c6eeac1f-3104-4063-a0d3-06bd230a0322.spec.yaml")
    return _attractions_conflation_entity_type_similarity_calculation_scope_module(
            master_attributes=master_attributes,
            master_candidate_pairs_filtered_stream=master_candidate_pairs_filtered_stream,
            vc=vc,
            scopeparams=scopeparams,)


class _AetheremailmoduleInput:
    body: Input = None
    """path(optional)"""
    attachments: Input = None
    """path(optional)"""
    recipients: str = None
    """String (optional)"""
    subject: str = None
    """String (optional)"""


class _AetheremailmoduleOutput:
    out_out: Output = None
    """path"""


class _AetheremailmoduleComponent(Component):
    inputs: _AetheremailmoduleInput
    outputs: _AetheremailmoduleOutput
    runsettings: _CommandComponentRunsetting


_aetheremailmodule = None


def aetheremailmodule(
    body: Path = None,
    attachments: Path = None,
    recipients: str = None,
    subject: str = None,
) -> _AetheremailmoduleComponent:
    """aetheremailmodule
    
    :param body: path(optional)
    :type body: Path
    :param attachments: path(optional)
    :type attachments: Path
    :param recipients: String (optional)
    :type recipients: str
    :param subject: String (optional)
    :type subject: str
    :output out_out: path
    :type: out_out: Output
    """
    global _aetheremailmodule
    if _aetheremailmodule is None:
        _aetheremailmodule = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/aetheremailmodule/0.0.1/c85f3433-1f0f-4037-b720-e58f53639d7c.spec.yaml")
    return _aetheremailmodule(
            body=body,
            attachments=attachments,
            recipients=recipients,
            subject=subject,)


class _AmlItpModuleInput:
    input1: Input = None
    """path(optional)"""
    input2: Input = None
    """path(optional)"""
    input3: Input = None
    """path(optional)"""
    input4: Input = None
    """path(optional)"""
    input5: Input = None
    """path(optional)"""
    input6: Input = None
    """path(optional)"""
    input7: Input = None
    """path(optional)"""
    input8: Input = None
    """path(optional)"""
    input9: Input = None
    """path(optional)"""
    input10: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    cluster: str = None
    """String (optional)"""
    clustergroupname: str = None
    """String (optional)"""
    sku: str = None
    """String (optional)"""
    vcblocklist: str = None
    """String (optional)"""
    clusterblocklist: str = None
    """String (optional)"""
    jobname_new: str = None
    """String (optional)"""
    jobtype: str = None
    """String (optional)"""
    preemptiblejob: str = None
    """String (optional)"""
    nodecount_new: str = None
    """String (optional)"""
    gpucount: str = None
    """String (optional)"""
    registry: str = None
    """String (optional)"""
    dockerimage: str = None
    """String (optional)"""
    command_new: str = None
    """String (optional)"""
    homepathmount: str = None
    """String (optional)"""
    nodecountset: str = None
    """String (optional)"""
    minimumscaleintervalinminute: str = None
    """String (optional)"""
    blobaccountname: str = None
    """String (optional)"""
    blobcontainername: str = None
    """String (optional)"""
    blobmountpath: str = None
    """String (optional)"""
    blobmountoptions: str = None
    """String (optional)"""
    datadownloadreuse: str = None
    """String (optional)"""
    tonfsfolder: str = None
    """String (optional)"""
    fromnfsfolder: str = None
    """String (optional)"""
    tocosmospath: str = None
    """String (optional)"""
    environmentvariables_new: str = None
    """String (optional)"""
    retrypolicy: str = None
    """String (optional)"""
    tensorboardenabled: str = None
    """String (optional)"""
    indicator: str = None
    """String (optional)"""


class _AmlItpModuleOutput:
    output1_out: Output = None
    """path"""
    output2_out: Output = None
    """path"""
    output3_out: Output = None
    """path"""
    output4_out: Output = None
    """path"""
    output5_out: Output = None
    """path"""
    joboutput_out: Output = None
    """path"""


class _AmlItpModuleComponent(Component):
    inputs: _AmlItpModuleInput
    outputs: _AmlItpModuleOutput
    runsettings: _CommandComponentRunsetting


_aml_itp_module = None


def aml_itp_module(
    input1: Path = None,
    input2: Path = None,
    input3: Path = None,
    input4: Path = None,
    input5: Path = None,
    input6: Path = None,
    input7: Path = None,
    input8: Path = None,
    input9: Path = None,
    input10: Path = None,
    vc: str = None,
    cluster: str = None,
    clustergroupname: str = None,
    sku: str = None,
    vcblocklist: str = None,
    clusterblocklist: str = None,
    jobname_new: str = None,
    jobtype: str = None,
    preemptiblejob: str = None,
    nodecount_new: str = None,
    gpucount: str = None,
    registry: str = None,
    dockerimage: str = None,
    command_new: str = None,
    homepathmount: str = None,
    nodecountset: str = None,
    minimumscaleintervalinminute: str = None,
    blobaccountname: str = None,
    blobcontainername: str = None,
    blobmountpath: str = None,
    blobmountoptions: str = None,
    datadownloadreuse: str = None,
    tonfsfolder: str = None,
    fromnfsfolder: str = None,
    tocosmospath: str = None,
    environmentvariables_new: str = None,
    retrypolicy: str = None,
    tensorboardenabled: str = None,
    indicator: str = None,
) -> _AmlItpModuleComponent:
    """aml_itp_module
    
    :param input1: path(optional)
    :type input1: Path
    :param input2: path(optional)
    :type input2: Path
    :param input3: path(optional)
    :type input3: Path
    :param input4: path(optional)
    :type input4: Path
    :param input5: path(optional)
    :type input5: Path
    :param input6: path(optional)
    :type input6: Path
    :param input7: path(optional)
    :type input7: Path
    :param input8: path(optional)
    :type input8: Path
    :param input9: path(optional)
    :type input9: Path
    :param input10: path(optional)
    :type input10: Path
    :param vc: String (optional)
    :type vc: str
    :param cluster: String (optional)
    :type cluster: str
    :param clustergroupname: String (optional)
    :type clustergroupname: str
    :param sku: String (optional)
    :type sku: str
    :param vcblocklist: String (optional)
    :type vcblocklist: str
    :param clusterblocklist: String (optional)
    :type clusterblocklist: str
    :param jobname_new: String (optional)
    :type jobname_new: str
    :param jobtype: String (optional)
    :type jobtype: str
    :param preemptiblejob: String (optional)
    :type preemptiblejob: str
    :param nodecount_new: String (optional)
    :type nodecount_new: str
    :param gpucount: String (optional)
    :type gpucount: str
    :param registry: String (optional)
    :type registry: str
    :param dockerimage: String (optional)
    :type dockerimage: str
    :param command_new: String (optional)
    :type command_new: str
    :param homepathmount: String (optional)
    :type homepathmount: str
    :param nodecountset: String (optional)
    :type nodecountset: str
    :param minimumscaleintervalinminute: String (optional)
    :type minimumscaleintervalinminute: str
    :param blobaccountname: String (optional)
    :type blobaccountname: str
    :param blobcontainername: String (optional)
    :type blobcontainername: str
    :param blobmountpath: String (optional)
    :type blobmountpath: str
    :param blobmountoptions: String (optional)
    :type blobmountoptions: str
    :param datadownloadreuse: String (optional)
    :type datadownloadreuse: str
    :param tonfsfolder: String (optional)
    :type tonfsfolder: str
    :param fromnfsfolder: String (optional)
    :type fromnfsfolder: str
    :param tocosmospath: String (optional)
    :type tocosmospath: str
    :param environmentvariables_new: String (optional)
    :type environmentvariables_new: str
    :param retrypolicy: String (optional)
    :type retrypolicy: str
    :param tensorboardenabled: String (optional)
    :type tensorboardenabled: str
    :param indicator: String (optional)
    :type indicator: str
    :output output1_out: path
    :type: output1_out: Output
    :output output2_out: path
    :type: output2_out: Output
    :output output3_out: path
    :type: output3_out: Output
    :output output4_out: path
    :type: output4_out: Output
    :output output5_out: path
    :type: output5_out: Output
    :output joboutput_out: path
    :type: joboutput_out: Output
    """
    global _aml_itp_module
    if _aml_itp_module is None:
        _aml_itp_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/aml_itp_module/0.0.1/c8a78d12-4f36-4774-9c6b-8746fa066b5d.spec.yaml")
    return _aml_itp_module(
            input1=input1,
            input2=input2,
            input3=input3,
            input4=input4,
            input5=input5,
            input6=input6,
            input7=input7,
            input8=input8,
            input9=input9,
            input10=input10,
            vc=vc,
            cluster=cluster,
            clustergroupname=clustergroupname,
            sku=sku,
            vcblocklist=vcblocklist,
            clusterblocklist=clusterblocklist,
            jobname_new=jobname_new,
            jobtype=jobtype,
            preemptiblejob=preemptiblejob,
            nodecount_new=nodecount_new,
            gpucount=gpucount,
            registry=registry,
            dockerimage=dockerimage,
            command_new=command_new,
            homepathmount=homepathmount,
            nodecountset=nodecountset,
            minimumscaleintervalinminute=minimumscaleintervalinminute,
            blobaccountname=blobaccountname,
            blobcontainername=blobcontainername,
            blobmountpath=blobmountpath,
            blobmountoptions=blobmountoptions,
            datadownloadreuse=datadownloadreuse,
            tonfsfolder=tonfsfolder,
            fromnfsfolder=fromnfsfolder,
            tocosmospath=tocosmospath,
            environmentvariables_new=environmentvariables_new,
            retrypolicy=retrypolicy,
            tensorboardenabled=tensorboardenabled,
            indicator=indicator,)


class _OutingsCosineSimilarityInput:
    stream_in: Input = None
    """path(optional)"""
    vec1: str = None
    """String (optional)"""
    vec2: str = None
    """String (optional)"""
    delim: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsCosineSimilarityOutput:
    output_ss_out: Output = None
    """path"""
    output_tsv_out: Output = None
    """path"""


class _OutingsCosineSimilarityComponent(Component):
    inputs: _OutingsCosineSimilarityInput
    outputs: _OutingsCosineSimilarityOutput
    runsettings: _CommandComponentRunsetting


_outings_cosine_similarity = None


def outings_cosine_similarity(
    stream_in: Path = None,
    vec1: str = None,
    vec2: str = None,
    delim: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsCosineSimilarityComponent:
    """outings_cosine_similarity
    
    :param stream_in: path(optional)
    :type stream_in: Path
    :param vec1: String (optional)
    :type vec1: str
    :param vec2: String (optional)
    :type vec2: str
    :param delim: String (optional)
    :type delim: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output output_ss_out: path
    :type: output_ss_out: Output
    :output output_tsv_out: path
    :type: output_tsv_out: Output
    """
    global _outings_cosine_similarity
    if _outings_cosine_similarity is None:
        _outings_cosine_similarity = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_cosine_similarity/0.0.1/caffcf18-a374-485d-a473-c384e6d83777.spec.yaml")
    return _outings_cosine_similarity(
            stream_in=stream_in,
            vec1=vec1,
            vec2=vec2,
            delim=delim,
            vc=vc,
            scopeparams=scopeparams,)


class _OutingsGetXpathValueInput:
    input_stream: Input = None
    """path(optional)"""
    output_col: str = None
    """String (optional)"""
    xml_column: str = None
    """String (optional)"""
    xpath: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsGetXpathValueOutput:
    output_stream_out: Output = None
    """path"""


class _OutingsGetXpathValueComponent(Component):
    inputs: _OutingsGetXpathValueInput
    outputs: _OutingsGetXpathValueOutput
    runsettings: _CommandComponentRunsetting


_outings_get_xpath_value = None


def outings_get_xpath_value(
    input_stream: Path = None,
    output_col: str = None,
    xml_column: str = None,
    xpath: str = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsGetXpathValueComponent:
    """outings_get_xpath_value
    
    :param input_stream: path(optional)
    :type input_stream: Path
    :param output_col: String (optional)
    :type output_col: str
    :param xml_column: String (optional)
    :type xml_column: str
    :param xpath: String (optional)
    :type xpath: str
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output output_stream_out: path
    :type: output_stream_out: Output
    """
    global _outings_get_xpath_value
    if _outings_get_xpath_value is None:
        _outings_get_xpath_value = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_get_xpath_value/0.0.1/cf6c3fff-c539-4409-8550-2fc975850823.spec.yaml")
    return _outings_get_xpath_value(
            input_stream=input_stream,
            output_col=output_col,
            xml_column=xml_column,
            xpath=xpath,
            vc=vc,
            scopeparams=scopeparams,)


class _OutingsDescriptionNerInput:
    inputfile: Input = None
    """path(optional)"""


class _OutingsDescriptionNerOutput:
    outputfile_out: Output = None
    """path"""


class _OutingsDescriptionNerComponent(Component):
    inputs: _OutingsDescriptionNerInput
    outputs: _OutingsDescriptionNerOutput
    runsettings: _CommandComponentRunsetting


_outings_description_ner = None


def outings_description_ner(
    inputfile: Path = None,
) -> _OutingsDescriptionNerComponent:
    """outings_description_ner
    
    :param inputfile: path(optional)
    :type inputfile: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _outings_description_ner
    if _outings_description_ner is None:
        _outings_description_ner = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_description_ner/0.0.1/cfc8bb2d-212c-4122-9368-5a4314796e82.spec.yaml")
    return _outings_description_ner(
            inputfile=inputfile,)


class _WikicenteredclusteringInput:
    inputfile1: Input = None
    """path(optional)"""
    inputfile2: Input = None
    """path(optional)"""


class _WikicenteredclusteringOutput:
    outputfile_out: Output = None
    """path"""


class _WikicenteredclusteringComponent(Component):
    inputs: _WikicenteredclusteringInput
    outputs: _WikicenteredclusteringOutput
    runsettings: _CommandComponentRunsetting


_wikicenteredclustering = None


def wikicenteredclustering(
    inputfile1: Path = None,
    inputfile2: Path = None,
) -> _WikicenteredclusteringComponent:
    """wikicenteredclustering
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :param inputfile2: path(optional)
    :type inputfile2: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _wikicenteredclustering
    if _wikicenteredclustering is None:
        _wikicenteredclustering = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/wikicenteredclustering/0.0.1/d02472ce-3397-4876-a08a-68e5785da194.spec.yaml")
    return _wikicenteredclustering(
            inputfile1=inputfile1,
            inputfile2=inputfile2,)


class _AttractionsConflationTopicsSimilarityCalculationScopeModuleInput:
    master_attributes: Input = None
    """path(optional)"""
    master_candidate_pairs_filtered_stream: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _AttractionsConflationTopicsSimilarityCalculationScopeModuleOutput:
    topics_similarity_stream_out: Output = None
    """path"""


class _AttractionsConflationTopicsSimilarityCalculationScopeModuleComponent(Component):
    inputs: _AttractionsConflationTopicsSimilarityCalculationScopeModuleInput
    outputs: _AttractionsConflationTopicsSimilarityCalculationScopeModuleOutput
    runsettings: _CommandComponentRunsetting


_attractions_conflation_topics_similarity_calculation_scope_module = None


def attractions_conflation_topics_similarity_calculation_scope_module(
    master_attributes: Path = None,
    master_candidate_pairs_filtered_stream: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _AttractionsConflationTopicsSimilarityCalculationScopeModuleComponent:
    """attractions_conflation_topics_similarity_calculation_scope_module
    
    :param master_attributes: path(optional)
    :type master_attributes: Path
    :param master_candidate_pairs_filtered_stream: path(optional)
    :type master_candidate_pairs_filtered_stream: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output topics_similarity_stream_out: path
    :type: topics_similarity_stream_out: Output
    """
    global _attractions_conflation_topics_similarity_calculation_scope_module
    if _attractions_conflation_topics_similarity_calculation_scope_module is None:
        _attractions_conflation_topics_similarity_calculation_scope_module = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/attractions_conflation_topics_similarity_calculation_scope_module/0.0.1/d8520338-0b99-4016-8e39-67f8ecf14936.spec.yaml")
    return _attractions_conflation_topics_similarity_calculation_scope_module(
            master_attributes=master_attributes,
            master_candidate_pairs_filtered_stream=master_candidate_pairs_filtered_stream,
            vc=vc,
            scopeparams=scopeparams,)


class _CopyCosmosStreamToIntermediateResourceInput:
    cosmospath: Input = None
    """path(optional)"""
    shouldrespectlineboundaries: str = None
    """String (optional)"""


class _CopyCosmosStreamToIntermediateResourceOutput:
    anyfile_out: Output = None
    """path"""


class _CopyCosmosStreamToIntermediateResourceComponent(Component):
    inputs: _CopyCosmosStreamToIntermediateResourceInput
    outputs: _CopyCosmosStreamToIntermediateResourceOutput
    runsettings: _CommandComponentRunsetting


_copy_cosmos_stream_to_intermediate_resource = None


def copy_cosmos_stream_to_intermediate_resource(
    cosmospath: Path = None,
    shouldrespectlineboundaries: str = None,
) -> _CopyCosmosStreamToIntermediateResourceComponent:
    """copy_cosmos_stream_to_intermediate_resource
    
    :param cosmospath: path(optional)
    :type cosmospath: Path
    :param shouldrespectlineboundaries: String (optional)
    :type shouldrespectlineboundaries: str
    :output anyfile_out: path
    :type: anyfile_out: Output
    """
    global _copy_cosmos_stream_to_intermediate_resource
    if _copy_cosmos_stream_to_intermediate_resource is None:
        _copy_cosmos_stream_to_intermediate_resource = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/copy_cosmos_stream_to_intermediate_resource/0.0.1/d99568f2-0d39-432a-b07c-3e49d989df3a.spec.yaml")
    return _copy_cosmos_stream_to_intermediate_resource(
            cosmospath=cosmospath,
            shouldrespectlineboundaries=shouldrespectlineboundaries,)


class _CopyIntermediateDirectoryOrFileToFixedCosmosPathInput:
    directoryresource: Input = None
    """path(optional)"""
    destinationpath: Input = None
    """path(optional)"""
    shouldrespectlineboundaries: str = None
    """String (optional)"""
    shouldoverrideifexists: str = None
    """String (optional)"""


class _CopyIntermediateDirectoryOrFileToFixedCosmosPathOutput:
    cosmospath_out: Output = None
    """path"""


class _CopyIntermediateDirectoryOrFileToFixedCosmosPathComponent(Component):
    inputs: _CopyIntermediateDirectoryOrFileToFixedCosmosPathInput
    outputs: _CopyIntermediateDirectoryOrFileToFixedCosmosPathOutput
    runsettings: _CommandComponentRunsetting


_copy_intermediate_directory_or_file_to_fixed_cosmos_path = None


def copy_intermediate_directory_or_file_to_fixed_cosmos_path(
    directoryresource: Path = None,
    destinationpath: Path = None,
    shouldrespectlineboundaries: str = None,
    shouldoverrideifexists: str = None,
) -> _CopyIntermediateDirectoryOrFileToFixedCosmosPathComponent:
    """copy_intermediate_directory_or_file_to_fixed_cosmos_path
    
    :param directoryresource: path(optional)
    :type directoryresource: Path
    :param destinationpath: path(optional)
    :type destinationpath: Path
    :param shouldrespectlineboundaries: String (optional)
    :type shouldrespectlineboundaries: str
    :param shouldoverrideifexists: String (optional)
    :type shouldoverrideifexists: str
    :output cosmospath_out: path
    :type: cosmospath_out: Output
    """
    global _copy_intermediate_directory_or_file_to_fixed_cosmos_path
    if _copy_intermediate_directory_or_file_to_fixed_cosmos_path is None:
        _copy_intermediate_directory_or_file_to_fixed_cosmos_path = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/copy_intermediate_directory_or_file_to_fixed_cosmos_path/0.0.1/dc2baef8-d3b9-4c42-b425-a5108c295361.spec.yaml")
    return _copy_intermediate_directory_or_file_to_fixed_cosmos_path(
            directoryresource=directoryresource,
            destinationpath=destinationpath,
            shouldrespectlineboundaries=shouldrespectlineboundaries,
            shouldoverrideifexists=shouldoverrideifexists,)


class _CopyCosmospathToGenerictsvInput:
    path: Input = None
    """path(optional)"""
    shouldrespectlineboundaries: str = None
    """String (optional)"""


class _CopyCosmospathToGenerictsvOutput:
    tsv_out: Output = None
    """path"""


class _CopyCosmospathToGenerictsvComponent(Component):
    inputs: _CopyCosmospathToGenerictsvInput
    outputs: _CopyCosmospathToGenerictsvOutput
    runsettings: _CommandComponentRunsetting


_copy_cosmospath_to_generictsv = None


def copy_cosmospath_to_generictsv(
    path: Path = None,
    shouldrespectlineboundaries: str = None,
) -> _CopyCosmospathToGenerictsvComponent:
    """copy_cosmospath_to_generictsv
    
    :param path: path(optional)
    :type path: Path
    :param shouldrespectlineboundaries: String (optional)
    :type shouldrespectlineboundaries: str
    :output tsv_out: path
    :type: tsv_out: Output
    """
    global _copy_cosmospath_to_generictsv
    if _copy_cosmospath_to_generictsv is None:
        _copy_cosmospath_to_generictsv = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/copy_cosmospath_to_generictsv/0.0.1/de546e8a-e8c8-4bc9-b632-745afbe1136f.spec.yaml")
    return _copy_cosmospath_to_generictsv(
            path=path,
            shouldrespectlineboundaries=shouldrespectlineboundaries,)


class _CosmosSplit1StreamTo10Input:
    inputstream: Input = None
    """path(optional)"""
    scopeparams: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _CosmosSplit1StreamTo10Output:
    part0_out: Output = None
    """path"""
    part1_out: Output = None
    """path"""
    part2_out: Output = None
    """path"""
    part3_out: Output = None
    """path"""
    part4_out: Output = None
    """path"""
    part5_out: Output = None
    """path"""
    part6_out: Output = None
    """path"""
    part7_out: Output = None
    """path"""
    part8_out: Output = None
    """path"""
    part9_out: Output = None
    """path"""


class _CosmosSplit1StreamTo10Component(Component):
    inputs: _CosmosSplit1StreamTo10Input
    outputs: _CosmosSplit1StreamTo10Output
    runsettings: _CommandComponentRunsetting


_cosmos_split_1_stream_to_10 = None


def cosmos_split_1_stream_to_10(
    inputstream: Path = None,
    scopeparams: str = None,
    vc: str = None,
) -> _CosmosSplit1StreamTo10Component:
    """cosmos_split_1_stream_to_10
    
    :param inputstream: path(optional)
    :type inputstream: Path
    :param scopeparams: String (optional)
    :type scopeparams: str
    :param vc: String (optional)
    :type vc: str
    :output part0_out: path
    :type: part0_out: Output
    :output part1_out: path
    :type: part1_out: Output
    :output part2_out: path
    :type: part2_out: Output
    :output part3_out: path
    :type: part3_out: Output
    :output part4_out: path
    :type: part4_out: Output
    :output part5_out: path
    :type: part5_out: Output
    :output part6_out: path
    :type: part6_out: Output
    :output part7_out: path
    :type: part7_out: Output
    :output part8_out: path
    :type: part8_out: Output
    :output part9_out: path
    :type: part9_out: Output
    """
    global _cosmos_split_1_stream_to_10
    if _cosmos_split_1_stream_to_10 is None:
        _cosmos_split_1_stream_to_10 = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/cosmos_split_1_stream_to_10/0.0.1/e05289ac-6f6d-4c0f-92c0-00f9c3ef9c4e.spec.yaml")
    return _cosmos_split_1_stream_to_10(
            inputstream=inputstream,
            scopeparams=scopeparams,
            vc=vc,)


class _ScopeBasicsUnionAnyTypeBetweenSstreamsInput:
    in_1: Input = None
    """path(optional)"""
    in_2: Input = None
    """path(optional)"""
    in_3: Input = None
    """path(optional)"""
    in_4: Input = None
    """path(optional)"""
    in_5: Input = None
    """path(optional)"""
    in_6: Input = None
    """path(optional)"""
    in_7: Input = None
    """path(optional)"""
    in_8: Input = None
    """path(optional)"""
    in_9: Input = None
    """path(optional)"""
    in_10: Input = None
    """path(optional)"""
    in_11: Input = None
    """path(optional)"""
    in_12: Input = None
    """path(optional)"""
    in_13: Input = None
    """path(optional)"""
    in_14: Input = None
    """path(optional)"""
    in_15: Input = None
    """path(optional)"""
    in_16: Input = None
    """path(optional)"""
    in_17: Input = None
    """path(optional)"""
    in_18: Input = None
    """path(optional)"""
    in_19: Input = None
    """path(optional)"""
    in_20: Input = None
    """path(optional)"""
    referencedstreampath: str = None
    """String (optional)"""
    clusterkey: str = None
    """String (optional)"""
    numberofpartitions: str = None
    """String (optional)"""
    sortkey: str = None
    """String (optional)"""
    unionoption: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _ScopeBasicsUnionAnyTypeBetweenSstreamsOutput:
    ssoutput_unioneddata_out: Output = None
    """path"""


class _ScopeBasicsUnionAnyTypeBetweenSstreamsComponent(Component):
    inputs: _ScopeBasicsUnionAnyTypeBetweenSstreamsInput
    outputs: _ScopeBasicsUnionAnyTypeBetweenSstreamsOutput
    runsettings: _CommandComponentRunsetting


_scope_basics_union_any_type_between_sstreams = None


def scope_basics_union_any_type_between_sstreams(
    in_1: Path = None,
    in_2: Path = None,
    in_3: Path = None,
    in_4: Path = None,
    in_5: Path = None,
    in_6: Path = None,
    in_7: Path = None,
    in_8: Path = None,
    in_9: Path = None,
    in_10: Path = None,
    in_11: Path = None,
    in_12: Path = None,
    in_13: Path = None,
    in_14: Path = None,
    in_15: Path = None,
    in_16: Path = None,
    in_17: Path = None,
    in_18: Path = None,
    in_19: Path = None,
    in_20: Path = None,
    referencedstreampath: str = None,
    clusterkey: str = None,
    numberofpartitions: str = None,
    sortkey: str = None,
    unionoption: str = None,
    vc: str = None,
) -> _ScopeBasicsUnionAnyTypeBetweenSstreamsComponent:
    """scope_basics_union_any_type_between_sstreams
    
    :param in_1: path(optional)
    :type in_1: Path
    :param in_2: path(optional)
    :type in_2: Path
    :param in_3: path(optional)
    :type in_3: Path
    :param in_4: path(optional)
    :type in_4: Path
    :param in_5: path(optional)
    :type in_5: Path
    :param in_6: path(optional)
    :type in_6: Path
    :param in_7: path(optional)
    :type in_7: Path
    :param in_8: path(optional)
    :type in_8: Path
    :param in_9: path(optional)
    :type in_9: Path
    :param in_10: path(optional)
    :type in_10: Path
    :param in_11: path(optional)
    :type in_11: Path
    :param in_12: path(optional)
    :type in_12: Path
    :param in_13: path(optional)
    :type in_13: Path
    :param in_14: path(optional)
    :type in_14: Path
    :param in_15: path(optional)
    :type in_15: Path
    :param in_16: path(optional)
    :type in_16: Path
    :param in_17: path(optional)
    :type in_17: Path
    :param in_18: path(optional)
    :type in_18: Path
    :param in_19: path(optional)
    :type in_19: Path
    :param in_20: path(optional)
    :type in_20: Path
    :param referencedstreampath: String (optional)
    :type referencedstreampath: str
    :param clusterkey: String (optional)
    :type clusterkey: str
    :param numberofpartitions: String (optional)
    :type numberofpartitions: str
    :param sortkey: String (optional)
    :type sortkey: str
    :param unionoption: String (optional)
    :type unionoption: str
    :param vc: String (optional)
    :type vc: str
    :output ssoutput_unioneddata_out: path
    :type: ssoutput_unioneddata_out: Output
    """
    global _scope_basics_union_any_type_between_sstreams
    if _scope_basics_union_any_type_between_sstreams is None:
        _scope_basics_union_any_type_between_sstreams = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/scope_basics_union_any_type_between_sstreams/0.0.1/ebd9005d-f80d-47c4-93f8-3c6453f62624.spec.yaml")
    return _scope_basics_union_any_type_between_sstreams(
            in_1=in_1,
            in_2=in_2,
            in_3=in_3,
            in_4=in_4,
            in_5=in_5,
            in_6=in_6,
            in_7=in_7,
            in_8=in_8,
            in_9=in_9,
            in_10=in_10,
            in_11=in_11,
            in_12=in_12,
            in_13=in_13,
            in_14=in_14,
            in_15=in_15,
            in_16=in_16,
            in_17=in_17,
            in_18=in_18,
            in_19=in_19,
            in_20=in_20,
            referencedstreampath=referencedstreampath,
            clusterkey=clusterkey,
            numberofpartitions=numberofpartitions,
            sortkey=sortkey,
            unionoption=unionoption,
            vc=vc,)


class _CreateGenericTsvInput:
    text: str = None
    """String (optional)"""
    tabseparator: str = None
    """String (optional)"""
    lineseparator: str = None
    """String (optional)"""


class _CreateGenericTsvOutput:
    outputfile_out: Output = None
    """path"""
    logfile_out: Output = None
    """path"""


class _CreateGenericTsvComponent(Component):
    inputs: _CreateGenericTsvInput
    outputs: _CreateGenericTsvOutput
    runsettings: _CommandComponentRunsetting


_create_generic_tsv = None


def create_generic_tsv(
    text: str = None,
    tabseparator: str = None,
    lineseparator: str = None,
) -> _CreateGenericTsvComponent:
    """create_generic_tsv
    
    :param text: String (optional)
    :type text: str
    :param tabseparator: String (optional)
    :type tabseparator: str
    :param lineseparator: String (optional)
    :type lineseparator: str
    :output outputfile_out: path
    :type: outputfile_out: Output
    :output logfile_out: path
    :type: logfile_out: Output
    """
    global _create_generic_tsv
    if _create_generic_tsv is None:
        _create_generic_tsv = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/create_generic_tsv/0.0.1/ec32907d-5822-4468-9483-a34b9e6ae41b.spec.yaml")
    return _create_generic_tsv(
            text=text,
            tabseparator=tabseparator,
            lineseparator=lineseparator,)


class _NotConditionalDecisionLogicInput:
    control: Input = None
    """path(optional)"""


class _NotConditionalDecisionLogicOutput:
    control_out: Output = None
    """path"""


class _NotConditionalDecisionLogicComponent(Component):
    inputs: _NotConditionalDecisionLogicInput
    outputs: _NotConditionalDecisionLogicOutput
    runsettings: _CommandComponentRunsetting


_not_conditional_decision_logic = None


def not_conditional_decision_logic(
    control: Path = None,
) -> _NotConditionalDecisionLogicComponent:
    """not_conditional_decision_logic
    
    :param control: path(optional)
    :type control: Path
    :output control_out: path
    :type: control_out: Output
    """
    global _not_conditional_decision_logic
    if _not_conditional_decision_logic is None:
        _not_conditional_decision_logic = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/not_conditional_decision_logic/0.0.1/f02ecb1b-03ae-44f6-ad70-97cd970cdb8b.spec.yaml")
    return _not_conditional_decision_logic(
            control=control,)


class _OutingsTopicExtractionInput:
    input_stream: Input = None
    """path(optional)"""
    vc: str = None
    """String (optional)"""
    scopeparams: str = None
    """String (optional)"""


class _OutingsTopicExtractionOutput:
    output_stream_out: Output = None
    """path"""


class _OutingsTopicExtractionComponent(Component):
    inputs: _OutingsTopicExtractionInput
    outputs: _OutingsTopicExtractionOutput
    runsettings: _CommandComponentRunsetting


_outings_topic_extraction = None


def outings_topic_extraction(
    input_stream: Path = None,
    vc: str = None,
    scopeparams: str = None,
) -> _OutingsTopicExtractionComponent:
    """outings_topic_extraction
    
    :param input_stream: path(optional)
    :type input_stream: Path
    :param vc: String (optional)
    :type vc: str
    :param scopeparams: String (optional)
    :type scopeparams: str
    :output output_stream_out: path
    :type: output_stream_out: Output
    """
    global _outings_topic_extraction
    if _outings_topic_extraction is None:
        _outings_topic_extraction = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/outings_topic_extraction/0.0.1/f3958437-9847-4b12-9a27-da993681f15a.spec.yaml")
    return _outings_topic_extraction(
            input_stream=input_stream,
            vc=vc,
            scopeparams=scopeparams,)


class _SstreamToTsvAetherInput:
    aetherstructuredstream: Input = None
    """path(optional)"""
    addheader: str = None
    """String (optional)"""
    commasepcolumnstokeep: str = None
    """String (optional)"""


class _SstreamToTsvAetherOutput:
    outputtsv_out: Output = None
    """path"""


class _SstreamToTsvAetherComponent(Component):
    inputs: _SstreamToTsvAetherInput
    outputs: _SstreamToTsvAetherOutput
    runsettings: _CommandComponentRunsetting


_sstream_to_tsv_aether = None


def sstream_to_tsv_aether(
    aetherstructuredstream: Path = None,
    addheader: str = None,
    commasepcolumnstokeep: str = None,
) -> _SstreamToTsvAetherComponent:
    """sstream_to_tsv_aether
    
    :param aetherstructuredstream: path(optional)
    :type aetherstructuredstream: Path
    :param addheader: String (optional)
    :type addheader: str
    :param commasepcolumnstokeep: String (optional)
    :type commasepcolumnstokeep: str
    :output outputtsv_out: path
    :type: outputtsv_out: Output
    """
    global _sstream_to_tsv_aether
    if _sstream_to_tsv_aether is None:
        _sstream_to_tsv_aether = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/sstream_to_tsv_aether/0.0.1/f4bccc75-7f1b-4ce5-9900-6ae25df32613.spec.yaml")
    return _sstream_to_tsv_aether(
            aetherstructuredstream=aetherstructuredstream,
            addheader=addheader,
            commasepcolumnstokeep=commasepcolumnstokeep,)


class _AlltrailscenteredclusteringInput:
    inputfile1: Input = None
    """path(optional)"""
    inputfile2: Input = None
    """path(optional)"""


class _AlltrailscenteredclusteringOutput:
    outputfile_out: Output = None
    """path"""


class _AlltrailscenteredclusteringComponent(Component):
    inputs: _AlltrailscenteredclusteringInput
    outputs: _AlltrailscenteredclusteringOutput
    runsettings: _CommandComponentRunsetting


_alltrailscenteredclustering = None


def alltrailscenteredclustering(
    inputfile1: Path = None,
    inputfile2: Path = None,
) -> _AlltrailscenteredclusteringComponent:
    """alltrailscenteredclustering
    
    :param inputfile1: path(optional)
    :type inputfile1: Path
    :param inputfile2: path(optional)
    :type inputfile2: Path
    :output outputfile_out: path
    :type: outputfile_out: Output
    """
    global _alltrailscenteredclustering
    if _alltrailscenteredclustering is None:
        _alltrailscenteredclustering = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/alltrailscenteredclustering/0.0.1/fc1312bc-201c-4d81-b5ce-7dfccf8b2d25.spec.yaml")
    return _alltrailscenteredclustering(
            inputfile1=inputfile1,
            inputfile2=inputfile2,)


class _RadioSplitSstreamInput:
    inputpath: Input = None
    """path(optional)"""
    columns: str = None
    """String (optional)"""
    leftratio: str = None
    """String (optional)"""
    vc: str = None
    """String (optional)"""


class _RadioSplitSstreamOutput:
    leftpath_out: Output = None
    """path"""
    rightpath_out: Output = None
    """path"""


class _RadioSplitSstreamComponent(Component):
    inputs: _RadioSplitSstreamInput
    outputs: _RadioSplitSstreamOutput
    runsettings: _CommandComponentRunsetting


_radio_split_sstream = None


def radio_split_sstream(
    inputpath: Path = None,
    columns: str = None,
    leftratio: str = None,
    vc: str = None,
) -> _RadioSplitSstreamComponent:
    """radio_split_sstream
    
    :param inputpath: path(optional)
    :type inputpath: Path
    :param columns: String (optional)
    :type columns: str
    :param leftratio: String (optional)
    :type leftratio: str
    :param vc: String (optional)
    :type vc: str
    :output leftpath_out: path
    :type: leftpath_out: Output
    :output rightpath_out: path
    :type: rightpath_out: Output
    """
    global _radio_split_sstream
    if _radio_split_sstream is None:
        _radio_split_sstream = Component.from_yaml(yaml_file=SOURCE_DIRECTORY / "components/radio_split_sstream/0.0.1/fee138f5-a4d4-422c-9cd2-b8951dcecda5.spec.yaml")
    return _radio_split_sstream(
            inputpath=inputpath,
            columns=columns,
            leftratio=leftratio,
            vc=vc,)


# No datasets class is generated.
