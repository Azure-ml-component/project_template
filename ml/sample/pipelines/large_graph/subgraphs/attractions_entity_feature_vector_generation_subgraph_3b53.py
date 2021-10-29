from datetime import datetime
from azure.ml.component import dsl
from use_cache_similarity_5fd2 import use_cache_similarity_5fd2
from attractions_entity_conflation_image_similarity_sub_graph_9935 import attractions_entity_conflation_image_similarity_sub_graph_9935
from resources import cosmos_mirror_with_inputs_and_overwrite_func, createcosmospathfreely_func, attractions_conflation_website_similarity_calculation_scope_module_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func, attractions_conflation_phone_number_similarity_calculation_scope_module_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func, attractions_entity_similarity_data_merge_scope_module_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func, attractions_conflation_entity_type_similarity_calculation_scope_module_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func, attractions_conflation_topics_similarity_calculation_scope_module_func, attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module_func, outings_cast_one_table_remove_from_other_union_both_func, outings_cast_one_table_remove_from_other_union_both_func, outings_cast_one_table_remove_from_other_union_both_func, outings_cast_one_table_remove_from_other_union_both_func, outings_cast_one_table_remove_from_other_union_both_func


print(datetime.now(), "Declaring pipeline: attractions_entity_feature_vector_generation_subgraph_3b53")
@dsl.pipeline(name='attractions_entity_feature_vector_generation_subgraph_3b53', default_compute_target='cpu-cluster')
def attractions_entity_feature_vector_generation_subgraph_3b53(
    master_location_similarity,
    name_similarity_stream,
    imagevectors,
    master_candidate_pairs_filtered,
    master_attributes,
    number_of_images_to_compare='',
    file_suffix='',
    conflationdate=''
):
    attractions_entity_conflation_image_similarity_sub_graph_subgraph = attractions_entity_conflation_image_similarity_sub_graph_9935(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix=file_suffix,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered,
        imagevectors=imagevectors
    )
    use_cache_similarity_3214_subgraph = use_cache_similarity_5fd2(
        conflationdate=conflationdate,
        attributecol='Website',
        similaritycols='SourceEntityId, SourceEntityName, CandidateEntityId, CandidateEntityName, WebsiteSimilarity',
        currattributes=master_attributes,
        currpairsfiltered=master_candidate_pairs_filtered
    )
    createcosmospathfreely_func_4dbe_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/MasterMergedAllSimilarity.%s.ss""" % (conflationdate, file_suffix)
    )
    use_cache_similarity_27ef_subgraph = use_cache_similarity_5fd2(
        conflationdate=conflationdate,
        attributecol='EntityType',
        similaritycols='SourceEntityId, SourceEntityName, CandidateEntityId, CandidateEntityName, EntityTypeSimilarity',
        currattributes=master_attributes,
        currpairsfiltered=master_candidate_pairs_filtered
    )
    createcosmospathfreely_func_3731_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/MasterNERSimilarity.%s.ss""" % (conflationdate, file_suffix)
    )
    createcosmospathfreely_func_4173_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/MasterWebsiteSimilarity.%s.ss""" % (conflationdate, file_suffix)
    )
    createcosmospathfreely_func_f722_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/MasterImageSimilarity.%s.ss""" % (conflationdate, file_suffix)
    )
    use_cache_similarity_4dd5_subgraph = use_cache_similarity_5fd2(
        conflationdate=conflationdate,
        attributecol='PhoneNumber',
        similaritycols='SourceEntityId, SourceEntityName, CandidateEntityId, CandidateEntityName, PhoneNumberSimilarity',
        currattributes=master_attributes,
        currpairsfiltered=master_candidate_pairs_filtered
    )
    use_cache_similarity_76b2_subgraph = use_cache_similarity_5fd2(
        conflationdate=conflationdate,
        attributecol='Topics',
        similaritycols='SourceEntityId, SourceEntityName, SourceEntityTopics, CandidateEntityId, CandidateEntityName, CandidateEntityTopics, TopicsJaccardIndexValue,SourceTopicsIntersectionValue,CandidateTopicsIntersectionValue',
        currattributes=master_attributes,
        currpairsfiltered=master_candidate_pairs_filtered
    )
    createcosmospathfreely_func_8500_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/MasterEntityTypeSimilarity.%s.ss""" % (conflationdate, file_suffix)
    )
    use_cache_similarity_23cf_subgraph = use_cache_similarity_5fd2(
        conflationdate=conflationdate,
        attributecol='NERJson',
        similaritycols='SourceEntityId, SourceEntityName, SourceEntityNERJson, CandidateEntityId, CandidateEntityName,CandidateEntityNERJson, JaccardIndexValue,SourceIntersectionValue,CandidateIntersectionValue,LocationIntersectionFrequencyRatio',
        currattributes=master_attributes,
        currpairsfiltered=master_candidate_pairs_filtered
    )
    createcosmospathfreely_func_8537_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/MasterPhoneNumberSimilarity.%s.ss""" % (conflationdate, file_suffix)
    )
    createcosmospathfreely_func_303a_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/MasterTopicsSimilarity.%s.ss""" % (conflationdate, file_suffix)
    )
    attractions_conflation_website_similarity_calculation_scope_module_func_instance = attractions_conflation_website_similarity_calculation_scope_module_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        master_candidate_pairs_filtered_stream=use_cache_similarity_3214_subgraph.outputs.newpairsfiltered_out,
        master_attributes=master_attributes
    )
    attractions_conflation_entity_type_similarity_calculation_scope_module_func_instance = attractions_conflation_entity_type_similarity_calculation_scope_module_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        master_candidate_pairs_filtered_stream=use_cache_similarity_27ef_subgraph.outputs.newpairsfiltered_out,
        master_attributes=master_attributes
    )
    cosmos_mirror_with_inputs_and_overwrite_func_515f_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=attractions_entity_conflation_image_similarity_sub_graph_subgraph.outputs.image_similarity_output_stream_out,
        destinationpath=createcosmospathfreely_func_f722_instance.outputs.createdpath_out
    )
    attractions_conflation_phone_number_similarity_calculation_scope_module_func_instance = attractions_conflation_phone_number_similarity_calculation_scope_module_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        master_candidate_pairs_filtered_stream=use_cache_similarity_4dd5_subgraph.outputs.newpairsfiltered_out,
        master_attributes=master_attributes
    )
    attractions_conflation_topics_similarity_calculation_scope_module_func_instance = attractions_conflation_topics_similarity_calculation_scope_module_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        master_candidate_pairs_filtered_stream=use_cache_similarity_76b2_subgraph.outputs.newpairsfiltered_out,
        master_attributes=master_attributes
    )
    attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module_func_instance = attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module_func(
        deep_model='/local/AttractionsPipeline/Resources/LocalConflation/DeepModel.zip',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        master_candidate_pairs_filtered_stream=use_cache_similarity_23cf_subgraph.outputs.newpairsfiltered_out,
        master_attributes=master_attributes
    )
    outings_cast_one_table_remove_from_other_union_both_func_a3a2_instance = outings_cast_one_table_remove_from_other_union_both_func(
        cast_list='WebsiteSimilarity:Double',
        remove_list='SourceEntityWebsite|CandidateEntityWebsite',
        vc='cosmos08/Outings',
        scopeparams='',
        remove_input=attractions_conflation_website_similarity_calculation_scope_module_func_instance.outputs.website_similarity_stream_out,
        cast_input=use_cache_similarity_3214_subgraph.outputs.similarities_out
    )
    outings_cast_one_table_remove_from_other_union_both_func_02c3_instance = outings_cast_one_table_remove_from_other_union_both_func(
        cast_list='EntityTypeSimilarity:Integer',
        remove_list='CandidateEntityType|SourceEntityType',
        vc='cosmos08/Outings',
        scopeparams='',
        remove_input=attractions_conflation_entity_type_similarity_calculation_scope_module_func_instance.outputs.entity_type_similarity_stream_out,
        cast_input=use_cache_similarity_27ef_subgraph.outputs.similarities_out
    )
    outings_cast_one_table_remove_from_other_union_both_func_4fcc_instance = outings_cast_one_table_remove_from_other_union_both_func(
        cast_list='PhoneNumberSimilarity:Double',
        remove_list='SourceEntityPhoneNumber|CandidateEntityPhoneNumber',
        vc='cosmos08/Outings',
        scopeparams='',
        remove_input=attractions_conflation_phone_number_similarity_calculation_scope_module_func_instance.outputs.phonenumber_similarity_stream_out,
        cast_input=use_cache_similarity_4dd5_subgraph.outputs.similarities_out
    )
    outings_cast_one_table_remove_from_other_union_both_func_d15e_instance = outings_cast_one_table_remove_from_other_union_both_func(
        cast_list='TopicsJaccardIndexValue:Double|SourceTopicsIntersectionValue:Double|CandidateTopicsIntersectionValue:Double',
        remove_list='',
        vc='cosmos08/Outings',
        scopeparams='',
        remove_input=attractions_conflation_topics_similarity_calculation_scope_module_func_instance.outputs.topics_similarity_stream_out,
        cast_input=use_cache_similarity_76b2_subgraph.outputs.similarities_out
    )
    outings_cast_one_table_remove_from_other_union_both_func_5d52_instance = outings_cast_one_table_remove_from_other_union_both_func(
        cast_list='JaccardIndexValue:Double|SourceIntersectionValue:Double|CandidateIntersectionValue:Double|LocationIntersectionFrequencyRatio:Double',
        remove_list='SourceEntityDescription|CandidateEntityDescription',
        vc='cosmos08/Outings',
        scopeparams='',
        remove_input=attractions_conflation_named_entity_recognition_similarity_calcuation_scope_module_func_instance.outputs.ner_json_similarity_stream_out,
        cast_input=use_cache_similarity_23cf_subgraph.outputs.similarities_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_04de_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_cast_one_table_remove_from_other_union_both_func_a3a2_instance.outputs.output_ss_out,
        destinationpath=createcosmospathfreely_func_4173_instance.outputs.createdpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_af50_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_cast_one_table_remove_from_other_union_both_func_02c3_instance.outputs.output_ss_out,
        destinationpath=createcosmospathfreely_func_8500_instance.outputs.createdpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_f02e_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_cast_one_table_remove_from_other_union_both_func_4fcc_instance.outputs.output_ss_out,
        destinationpath=createcosmospathfreely_func_8537_instance.outputs.createdpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_c40d_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_cast_one_table_remove_from_other_union_both_func_d15e_instance.outputs.output_ss_out,
        destinationpath=createcosmospathfreely_func_303a_instance.outputs.createdpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_5273_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_cast_one_table_remove_from_other_union_both_func_5d52_instance.outputs.output_ss_out,
        destinationpath=createcosmospathfreely_func_3731_instance.outputs.createdpath_out
    )
    attractions_entity_similarity_data_merge_scope_module_func_instance = attractions_entity_similarity_data_merge_scope_module_func(
        vc='cosmos08/Outings',
        scopeparams='',
        entity_type_similarity_stream=cosmos_mirror_with_inputs_and_overwrite_func_af50_instance.outputs.destinationpath_out,
        topics_similarity_stream=cosmos_mirror_with_inputs_and_overwrite_func_c40d_instance.outputs.destinationpath_out,
        image_similarity_stream=cosmos_mirror_with_inputs_and_overwrite_func_515f_instance.outputs.destinationpath_out,
        ner_json_similarity_stream=cosmos_mirror_with_inputs_and_overwrite_func_5273_instance.outputs.destinationpath_out,
        website_similarity_stream=cosmos_mirror_with_inputs_and_overwrite_func_04de_instance.outputs.destinationpath_out,
        phonenumber_similarity_stream=cosmos_mirror_with_inputs_and_overwrite_func_f02e_instance.outputs.destinationpath_out,
        master_candidate_pairs_filtered_stream=master_candidate_pairs_filtered,
        location_similarity_stream=master_location_similarity,
        name_similarity_stream=name_similarity_stream
    )
    cosmos_mirror_with_inputs_and_overwrite_func_18c5_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=attractions_entity_similarity_data_merge_scope_module_func_instance.outputs.merged_similarity_stream_out,
        destinationpath=createcosmospathfreely_func_4dbe_instance.outputs.createdpath_out
    )
    return {'master_feature_vectors_out': cosmos_mirror_with_inputs_and_overwrite_func_18c5_instance.outputs.destinationpath_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating attractions_entity_feature_vector_generation_subgraph_3b53")
    pipeline = attractions_entity_feature_vector_generation_subgraph_3b53()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='attractions_entity_feature_vector_generation_subgraph_3b53')
    print(datetime.now(), "Finish")
