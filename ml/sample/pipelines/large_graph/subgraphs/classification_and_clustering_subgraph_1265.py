from datetime import datetime
from azure.ml.component import dsl
from gtc_clustering_96c0 import gtc_clustering_96c0
from resources import entity_graph_generation_func, generalselectcosmos_func, copy_cosmospath_to_generictsv_func, generalselectcosmos_func, copy_cosmospath_to_generictsv_func, copy_cosmos_stream_to_intermediate_resource_func, cosmospathcreator_rundate_func, copy_cosmos_stream_to_intermediate_resource_func, cosmospathcreator_rundate_func, rbf_svm_prediction_ongraph_func, cosmospathcreator_rundate_func, cast_anyfile_to_generictsv_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, generalselectcosmos_func, cosmospathcreator_rundate_func, cosmos_mirror_with_inputs_and_overwrite_func, cosmospathcreator_rundate_func, generalselectcosmos_func, cast_anyfile_to_generictsv_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: classification_and_clustering_subgraph_1265")
@dsl.pipeline(name='classification_and_clustering_subgraph_1265', default_compute_target='cpu-cluster')
def classification_and_clustering_subgraph_1265(
    master_feature_vectors,
    master_all_candidate_pairs_filtered,
    conflation_date=''
):
    cosmospathcreator_rundate_func_0e88_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Predictions.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_1515_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/ClassificationAndClustering/MergedTrainingData_model.sav',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_53da_instance = cosmospathcreator_rundate_func(
        relativepath='/local/users/jepatel/Debug/EntityConflation/GroundTruth/WikiPopulationBlacklist.ss',
        vc='vc://cosmos08/Outings',
        rundate='06_16_2020'
    )
    cosmospathcreator_rundate_func_31d1_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Predictions.tsv""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_1ba8_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/ClassificationAndClustering/SameDomainModel.sav',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_c06b_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Predictions.gpkl""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_d115_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/DomainCodeTable.tsv',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    copy_cosmos_stream_to_intermediate_resource_func_687f_instance = copy_cosmos_stream_to_intermediate_resource_func(
        shouldrespectlineboundaries='false',
        cosmospath=cosmospathcreator_rundate_func_1515_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_cf95_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='ToRemove = SELECT In1.* FROM In1 INNER JOIN In2 ON In1.SourceEntityId == In2.Id UNION DISTINCT SELECT In1.* FROM In1 INNER JOIN In2 ON In1.CandidateEntityId == In2.Id',
        select2='SELECT * FROM In1 EXCEPT DISTINCT SELECT * FROM ToRemove',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Remove Wiki Pairs By Population',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in2=cosmospathcreator_rundate_func_53da_instance.outputs.createdpath_out,
        in1=master_feature_vectors
    )
    generalselectcosmos_func_7383_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='ToRemove = SELECT In1.* FROM In1 INNER JOIN In2 ON In1.SourceEntityId == In2.Id UNION DISTINCT SELECT In1.* FROM In1 INNER JOIN In2 ON In1.CandidateEntityId == In2.Id',
        select2='SELECT * FROM In1 EXCEPT DISTINCT SELECT * FROM ToRemove',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Remove Wiki Pairs By Population',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in2=cosmospathcreator_rundate_func_53da_instance.outputs.createdpath_out,
        in1=master_all_candidate_pairs_filtered
    )
    copy_cosmos_stream_to_intermediate_resource_func_2c7f_instance = copy_cosmos_stream_to_intermediate_resource_func(
        shouldrespectlineboundaries='false',
        cosmospath=cosmospathcreator_rundate_func_1ba8_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_87d9_instance = generalselectcosmos_func(
        extractcols1='Domain : string, DomainCode : string',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmospathcreator_rundate_func_d115_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_acc5_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_7383_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_dada_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='rs0 = SELECT * FROM In1;',
        select2='rs1 = SELECT * FROM In2;',
        select3='rs2 = SELECT rs0.SourceEntityId, rs0.CandidateEntityId, rs1.DomainCode, rs0.Distance/10.0 AS Distance, rs0.NameSimilarity, rs0.LocationIntersectionFrequencyRatio, rs0.ImageSimilarity, rs0.EntityTypeSimilarity FROM rs0 INNER JOIN rs1 ON rs0.SourceEntityDomain == rs1.Domain AND rs0.CandidateEntityDomain == rs1.Domain;',
        select4='rs = SELECT * FROM rs2 UNION DISTINCT SELECT SourceEntityId, CandidateEntityId, "0" AS DomainCode, Distance/10.0 AS Distance, NameSimilarity, LocationIntersectionFrequencyRatio, ImageSimilarity, EntityTypeSimilarity FROM rs0 WHERE SourceEntityDomain != CandidateEntityDomain;',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_cf95_instance.outputs.outputstream_out,
        in2=generalselectcosmos_func_87d9_instance.outputs.outputstream_out
    )
    copy_cosmospath_to_generictsv_func_41ee_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_acc5_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_generictsv_func_528a_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_dada_instance.outputs.outputtsv_out
    )
    entity_graph_generation_func_instance = entity_graph_generation_func(
        inputfile=copy_cosmospath_to_generictsv_func_41ee_instance.outputs.tsv_out
    )
    rbf_svm_prediction_ongraph_func_instance = rbf_svm_prediction_ongraph_func(
        inputfile1=copy_cosmospath_to_generictsv_func_528a_instance.outputs.tsv_out,
        inputfile2=copy_cosmos_stream_to_intermediate_resource_func_687f_instance.outputs.anyfile_out,
        inputfile3=copy_cosmos_stream_to_intermediate_resource_func_2c7f_instance.outputs.anyfile_out,
        inputfile4=entity_graph_generation_func_instance.outputs.outputfile_out
    )
    cast_anyfile_to_generictsv_func_176e_instance = cast_anyfile_to_generictsv_func(
        input=rbf_svm_prediction_ongraph_func_instance.outputs.outputfile1_out
    )
    cast_anyfile_to_generictsv_func_05cd_instance = cast_anyfile_to_generictsv_func(
        input=rbf_svm_prediction_ongraph_func_instance.outputs.outputfile2_out
    )
    gtc_clustering_subgraph = gtc_clustering_96c0(
        conflation_date=conflation_date,
        inputfile=rbf_svm_prediction_ongraph_func_instance.outputs.outputfile2_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_eb42_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=cast_anyfile_to_generictsv_func_176e_instance.outputs.outputtsv_out,
        destinationpath=cosmospathcreator_rundate_func_31d1_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_44f0_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=cast_anyfile_to_generictsv_func_05cd_instance.outputs.outputtsv_out,
        destinationpath=cosmospathcreator_rundate_func_c06b_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_9d57_instance = generalselectcosmos_func(
        extractcols1='SourceEntityId:string, CandidateEntityId:string, Probability:double, Label:int',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId,CandidateEntityId',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_eb42_instance.outputs.cosmospath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_9d57_instance.outputs.outputstream_out,
        destinationpath=cosmospathcreator_rundate_func_0e88_instance.outputs.createdpath_out
    )
    return {'triples_out': gtc_clustering_subgraph.outputs.outputtsv_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating classification_and_clustering_subgraph_1265")
    pipeline = classification_and_clustering_subgraph_1265()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='classification_and_clustering_subgraph_1265')
    print(datetime.now(), "Finish")
