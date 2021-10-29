from datetime import datetime
from azure.ml.component import dsl
from linked_entities_42fb import linked_entities_42fb
from attribute_generation_sub_graph_9848 import attribute_generation_sub_graph_9848
from run_quality_gates_6dbe import run_quality_gates_6dbe
from classification_and_clustering_subgraph_1265 import classification_and_clustering_subgraph_1265
from domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75 import domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75
from candidate_pairs_pre_filtering_subgraph_a765 import candidate_pairs_pre_filtering_subgraph_a765
from attractions_entity_feature_vector_generation_subgraph_3441 import attractions_entity_feature_vector_generation_subgraph_3441
from generate_triples_data_and_ta_sid_mapping_dfe7 import generate_triples_data_and_ta_sid_mapping_dfe7
from record_image_data_generation_d333 import record_image_data_generation_d333
from image_vectorization_258d import image_vectorization_258d
from ground_truth_images_download_subgraph_0d42 import ground_truth_images_download_subgraph_0d42
from publish_data_to_prod_cbdb import publish_data_to_prod_cbdb
from backup_file_bdd9 import backup_file_bdd9
from resources import cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func, parameter_to_control_output_func, or_conditional_decision_logic_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: outings_entity_conflation_efb2")
@dsl.pipeline(name='outings_entity_conflation_efb2', default_compute_target='cpu-cluster')
def outings_entity_conflation_efb2(
    conflation_date='11_25_2020',
    ground_truth_domain1='en.wikipedia.org',
    ground_truth_domain2='www.tripadvisor.com',
    ground_truth_domain3='www.alltrails.com',
    ground_truth_image_download_count='10',
    location_similarity_threshold='10.0',
    number_of_images_to_compare='3',
    name_similarity_threshold='4',
    qualitygateoverride='false'
):
    record_image_data_generation_subgraph = record_image_data_generation_d333(
        conflation_date=conflation_date
    )
    cosmospathcreator_rundate_func_546f_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/DomainList.tsv',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_4870_instance = cosmospathcreator_rundate_func(
        relativepath='/local/AttractionsPipeline/MasterEnhanced.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    parameter_to_control_output_func_instance = parameter_to_control_output_func(
        control_output=qualitygateoverride
    )
    cosmospathcreator_rundate_func_8c0e_instance = cosmospathcreator_rundate_func(
        relativepath='/local/AttractionsPipeline/MasterRecords.ss',
        vc='vc://cosmos08/Outings',
        rundate="""%s""" % (conflation_date)
    )
    generalselectcosmos_func_4508_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1  WHERE !String.IsNullOrEmpty(OriginalEntityName) AND !String.IsNullOrEmpty(LocationLatitude) AND LocationLatitude!="NaN" AND !String.IsNullOrEmpty(LocationLongitude) AND LocationLongitude!="NaN";',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment=';',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmospathcreator_rundate_func_4870_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_cf3d_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In2.* FROM In2 INNER JOIN In1 ON In2.StoryId == In1.StoryId WHERE (DateTime.Today - DateTime.Parse(In1.DateUpdated)).Days <= 60; ',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Select Past 60 Days of Records',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmospathcreator_rundate_func_8c0e_instance.outputs.createdpath_out,
        in2=cosmospathcreator_rundate_func_4870_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_bd9c_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='domain: string, useFilter:bool',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.StoryId AS GUID, In1.OriginalEntityName AS OriginalEntityName,  In1.LocationLatitude AS LocationLatitude, In1.LocationLongitude AS LocationLongitude FROM In1  WHERE !String.IsNullOrEmpty(OriginalEntityName) AND !String.IsNullOrEmpty(LocationLatitude) AND LocationLatitude!="NaN" AND !String.IsNullOrEmpty(LocationLongitude) AND LocationLongitude!="NaN"',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Filter by Domain, Filter and OriginalEntityName',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_cf3d_instance.outputs.outputstream_out,
        in2=cosmospathcreator_rundate_func_546f_instance.outputs.createdpath_out
    )
    backup_file_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterEnhanced.snapshot.ss',
        sourcepath=generalselectcosmos_func_bd9c_instance.outputs.outputstream_out
    )
    domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_subgraph = domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75(
        ground_truth_domain1=ground_truth_domain1,
        ground_truth_domain2=ground_truth_domain2,
        conflation_date=conflation_date,
        webrecords=generalselectcosmos_func_bd9c_instance.outputs.outputtsv_out,
        enhanced=generalselectcosmos_func_4508_instance.outputs.outputstream_out
    )
    attribute_generation_sub_graph_subgraph = attribute_generation_sub_graph_9848(
        ground_truth_domain1=ground_truth_domain1,
        ground_truth_domain2=ground_truth_domain2,
        ground_truth_domain3=ground_truth_domain3,
        conflation_date=conflation_date,
        master_records=generalselectcosmos_func_cf3d_instance.outputs.outputstream_out,
        ground_truth_domain1_candidates=domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_subgraph.outputs.candidatepairsingroundtruthdomain1_out,
        ground_truth_domain2_candidates=domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_subgraph.outputs.candidatepairsingroundtruthdomain2_out
    )
    candidate_pairs_pre_filtering_subgraph_subgraph = candidate_pairs_pre_filtering_subgraph_a765(
        location_similarity_threshold=location_similarity_threshold,
        name_similarity_threshold=name_similarity_threshold,
        conflation_date=conflation_date,
        master_attributes=attribute_generation_sub_graph_subgraph.outputs.master_attributes_out,
        master_canddiate_urls=domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_subgraph.outputs.filteredss_out,
        namepairsim=domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_subgraph.outputs.namepairsimilarity_out
    )
    ground_truth_images_download_subgraph_subgraph = ground_truth_images_download_subgraph_0d42(
        conflation_date=conflation_date,
        ground_truth_domain1=ground_truth_domain1,
        ground_truth_domain2=ground_truth_domain2,
        download_image_count=ground_truth_image_download_count,
        ground_truth_domain3=ground_truth_domain3,
        master_attributes=attribute_generation_sub_graph_subgraph.outputs.master_attributes_out,
        master_candidate_pairs_filtered=candidate_pairs_pre_filtering_subgraph_subgraph.outputs.master_candidate_pairs_filtered_out
    )
    image_vectorization_subgraph = image_vectorization_258d(
        number_of_images_to_compare="""%s""" % (number_of_images_to_compare),
        attributes=attribute_generation_sub_graph_subgraph.outputs.master_attributes_out,
        groundtruthimages=ground_truth_images_download_subgraph_subgraph.outputs.master_ground_truth_images_out,
        recordimages=record_image_data_generation_subgraph.outputs.recordimagedata_out
    )
    attractions_entity_feature_vector_generation_subgraph_subgraph = attractions_entity_feature_vector_generation_subgraph_3441(
        number_of_images_to_compare=number_of_images_to_compare,
        conflation_date=conflation_date,
        master_attributes=attribute_generation_sub_graph_subgraph.outputs.master_attributes_out,
        imagevectors=image_vectorization_subgraph.outputs.imageidvectors_out,
        master_candidate_pairs_filtered=candidate_pairs_pre_filtering_subgraph_subgraph.outputs.master_candidate_pairs_filtered_out,
        master_location_similarity=candidate_pairs_pre_filtering_subgraph_subgraph.outputs.master_location_similarity_out,
        name_similarity_stream=candidate_pairs_pre_filtering_subgraph_subgraph.outputs.master_name_similarity_out
    )
    generalselectcosmos_func_b256_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT SourceEntityId,SourceEntityDomain,SourceEntityUrl,SourceEntityName,CandidateEntityId,CandidateEntityDomain,CandidateEntityUrl,CandidateEntityName,Distance,NameSimilarity,JaccardIndexValue == NULL ? -1:JaccardIndexValue AS JaccardIndexValue,SourceIntersectionValue == NULL ? -1:SourceIntersectionValue AS SourceIntersectionValue,CandidateIntersectionValue == NULL ? -1:CandidateIntersectionValue AS CandidateIntersectionValue,LocationIntersectionFrequencyRatio == NULL ? -1:LocationIntersectionFrequencyRatio AS LocationIntersectionFrequencyRatio,WebsiteSimilarity,PhoneNumberSimilarity,ImageSimilarity,EntityTypeSimilarity,TopicsJaccardIndexValue,SourceTopicsIntersectionValue,CandidateTopicsIntersectionValue FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Hot fix for NER bug',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=attractions_entity_feature_vector_generation_subgraph_subgraph.outputs.master_feature_vectors_out
    )
    classification_and_clustering_subgraph_subgraph = classification_and_clustering_subgraph_1265(
        conflation_date=conflation_date,
        master_feature_vectors=generalselectcosmos_func_b256_instance.outputs.outputstream_out,
        master_all_candidate_pairs_filtered=candidate_pairs_pre_filtering_subgraph_subgraph.outputs.master_candidate_pairs_filtered_out
    )
    generate_triples_data_and_ta_sid_mapping_subgraph = generate_triples_data_and_ta_sid_mapping_dfe7(
        conflation_date=conflation_date,
        conflation_month='04',
        triples_ss=classification_and_clustering_subgraph_subgraph.outputs.triples_out
    )
    linked_entities_subgraph = linked_entities_42fb(
        conflation_date=conflation_date,
        conflation_month='04',
        triples_ss=generate_triples_data_and_ta_sid_mapping_subgraph.outputs.record_ta_sid_triples_out
    )
    run_quality_gates_subgraph = run_quality_gates_6dbe(
        conflation_date=conflation_date,
        recipients='BingMapsMobileDevs@microsoft.com',
        record_triples=generate_triples_data_and_ta_sid_mapping_subgraph.outputs.record_ta_sid_triples_out,
        ta_satori_links=generate_triples_data_and_ta_sid_mapping_subgraph.outputs.ta_sid_mapping_out,
        master_attr=attribute_generation_sub_graph_subgraph.outputs.master_attributes_out,
        merged_sim=generalselectcosmos_func_b256_instance.outputs.outputstream_out
    )
    or_conditional_decision_logic_func_instance = or_conditional_decision_logic_func(
        controla=run_quality_gates_subgraph.outputs.passing_out,
        controlb=parameter_to_control_output_func_instance.outputs.control_out
    )
    publish_data_to_prod_subgraph = publish_data_to_prod_cbdb(
        conflation_date=conflation_date,
        historicalstats=run_quality_gates_subgraph.outputs.historicalstats_out,
        runstats=run_quality_gates_subgraph.outputs.runstats_out,
        linkedentities=linked_entities_subgraph.outputs.linkedentities_ss_out,
        qgpass=or_conditional_decision_logic_func_instance.outputs.control_out
    )
    return 


if __name__ == '__main__':
    print(datetime.now(), "Creating outings_entity_conflation_efb2")
    pipeline = outings_entity_conflation_efb2()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='outings_entity_conflation_efb2')
    print(datetime.now(), "Finish")
