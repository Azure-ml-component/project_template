from datetime import datetime
from azure.ml.component import dsl
from batch_10_feature_vector_generation_7984 import batch_10_feature_vector_generation_7984
from split_10_with_clustering_c32e import split_10_with_clustering_c32e
from batch_10_feature_vector_generation_085e import batch_10_feature_vector_generation_085e
from batch_10_feature_vector_generation_75ee import batch_10_feature_vector_generation_75ee
from backup_file_bdd9 import backup_file_bdd9
from resources import radio_split_sstream_func, scope_basics_union_any_type_between_sstreams_func, radio_split_sstream_func, radio_split_sstream_func


print(datetime.now(), "Declaring pipeline: attractions_entity_feature_vector_generation_subgraph_3441")
@dsl.pipeline(name='attractions_entity_feature_vector_generation_subgraph_3441', default_compute_target='cpu-cluster')
def attractions_entity_feature_vector_generation_subgraph_3441(
    master_location_similarity,
    name_similarity_stream,
    imagevectors,
    master_candidate_pairs_filtered,
    master_attributes,
    number_of_images_to_compare='',
    conflation_date=''
):
    radio_split_sstream_func_2acd_instance = radio_split_sstream_func(
        columns='SourceEntityId,SourceEntityDomain,SourceEntityUrl,CandidateEntityId,CandidateEntityDomain,CandidateEntityUrl,DateUpdated',
        leftratio='0.5',
        vc='cosmos08/Outings',
        inputpath=master_candidate_pairs_filtered
    )
    radio_split_sstream_func_e164_instance = radio_split_sstream_func(
        columns='SourceEntityId,SourceEntityDomain,SourceEntityUrl,CandidateEntityId,CandidateEntityDomain,CandidateEntityUrl,DateUpdated',
        leftratio='0.5',
        vc='cosmos08/Outings',
        inputpath=radio_split_sstream_func_2acd_instance.outputs.leftpath_out
    )
    radio_split_sstream_func_7d4c_instance = radio_split_sstream_func(
        columns='SourceEntityId,SourceEntityDomain,SourceEntityUrl,CandidateEntityId,CandidateEntityDomain,CandidateEntityUrl,DateUpdated',
        leftratio='0.5',
        vc='cosmos08/Outings',
        inputpath=radio_split_sstream_func_2acd_instance.outputs.rightpath_out
    )
    split_10_with_clustering_14d9_subgraph = split_10_with_clustering_c32e(
        clustercol='SourceEntityId,CandidateEntityId',
        sortcol='SourceEntityId,CandidateEntityId',
        inputstream=radio_split_sstream_func_2acd_instance.outputs.rightpath_out
    )
    split_10_with_clustering_1ee1_subgraph = split_10_with_clustering_c32e(
        clustercol='SourceEntityId,CandidateEntityId',
        sortcol='SourceEntityId,CandidateEntityId',
        inputstream=radio_split_sstream_func_e164_instance.outputs.leftpath_out
    )
    split_10_with_clustering_8bb9_subgraph = split_10_with_clustering_c32e(
        clustercol='SourceEntityId,CandidateEntityId',
        sortcol='SourceEntityId,CandidateEntityId',
        inputstream=radio_split_sstream_func_e164_instance.outputs.rightpath_out
    )
    batch_10_feature_vector_generation_subgraph = batch_10_feature_vector_generation_75ee(
        number_of_images_to_compare=number_of_images_to_compare,
        conflationdate=conflation_date,
        master_candidate_pairs_filtered=split_10_with_clustering_14d9_subgraph.outputs.part0_out,
        master_candidate_pairs_filtered_2=split_10_with_clustering_14d9_subgraph.outputs.part1_out,
        master_candidate_pairs_filtered_3=split_10_with_clustering_14d9_subgraph.outputs.part2_out,
        master_candidate_pairs_filtered_4=split_10_with_clustering_14d9_subgraph.outputs.part3_out,
        master_candidate_pairs_filtered_5=split_10_with_clustering_14d9_subgraph.outputs.part4_out,
        master_candidate_pairs_filtered_6=split_10_with_clustering_14d9_subgraph.outputs.part5_out,
        master_candidate_pairs_filtered_7=split_10_with_clustering_14d9_subgraph.outputs.part6_out,
        master_candidate_pairs_filtered_8=split_10_with_clustering_14d9_subgraph.outputs.part7_out,
        master_candidate_pairs_filtered_9=split_10_with_clustering_14d9_subgraph.outputs.part8_out,
        master_candidate_pairs_filtered_10=split_10_with_clustering_14d9_subgraph.outputs.part9_out,
        master_attributes=master_attributes,
        imagevectors=imagevectors,
        master_location_similarity=master_location_similarity,
        name_similarity_stream=name_similarity_stream
    )
    batch_10_feature_vector_generation_subgraph = batch_10_feature_vector_generation_085e(
        number_of_images_to_compare=number_of_images_to_compare,
        conflationdate=conflation_date,
        master_candidate_pairs_filtered=split_10_with_clustering_1ee1_subgraph.outputs.part0_out,
        master_candidate_pairs_filtered_2=split_10_with_clustering_1ee1_subgraph.outputs.part1_out,
        master_candidate_pairs_filtered_3=split_10_with_clustering_1ee1_subgraph.outputs.part2_out,
        master_candidate_pairs_filtered_4=split_10_with_clustering_1ee1_subgraph.outputs.part3_out,
        master_candidate_pairs_filtered_5=split_10_with_clustering_1ee1_subgraph.outputs.part4_out,
        master_candidate_pairs_filtered_6=split_10_with_clustering_1ee1_subgraph.outputs.part5_out,
        master_candidate_pairs_filtered_7=split_10_with_clustering_1ee1_subgraph.outputs.part6_out,
        master_candidate_pairs_filtered_8=split_10_with_clustering_1ee1_subgraph.outputs.part7_out,
        master_candidate_pairs_filtered_9=split_10_with_clustering_1ee1_subgraph.outputs.part8_out,
        master_candidate_pairs_filtered_10=split_10_with_clustering_1ee1_subgraph.outputs.part9_out,
        master_attributes=master_attributes,
        imagevectors=imagevectors,
        master_location_similarity=master_location_similarity,
        name_similarity_stream=name_similarity_stream
    )
    batch_10_feature_vector_generation_subgraph = batch_10_feature_vector_generation_7984(
        number_of_images_to_compare=number_of_images_to_compare,
        conflationdate=conflation_date,
        master_candidate_pairs_filtered=split_10_with_clustering_8bb9_subgraph.outputs.part0_out,
        master_candidate_pairs_filtered_2=split_10_with_clustering_8bb9_subgraph.outputs.part1_out,
        master_candidate_pairs_filtered_3=split_10_with_clustering_8bb9_subgraph.outputs.part2_out,
        master_candidate_pairs_filtered_4=split_10_with_clustering_8bb9_subgraph.outputs.part3_out,
        master_candidate_pairs_filtered_5=split_10_with_clustering_8bb9_subgraph.outputs.part4_out,
        master_candidate_pairs_filtered_6=split_10_with_clustering_8bb9_subgraph.outputs.part5_out,
        master_candidate_pairs_filtered_7=split_10_with_clustering_8bb9_subgraph.outputs.part6_out,
        master_candidate_pairs_filtered_8=split_10_with_clustering_8bb9_subgraph.outputs.part7_out,
        master_candidate_pairs_filtered_9=split_10_with_clustering_8bb9_subgraph.outputs.part8_out,
        master_candidate_pairs_filtered_10=split_10_with_clustering_8bb9_subgraph.outputs.part9_out,
        master_attributes=master_attributes,
        imagevectors=imagevectors,
        master_location_similarity=master_location_similarity,
        name_similarity_stream=name_similarity_stream
    )
    scope_basics_union_any_type_between_sstreams_func_instance = scope_basics_union_any_type_between_sstreams_func(
        referencedstreampath='none',
        clusterkey='SourceEntityId, CandidateEntityId',
        numberofpartitions='',
        sortkey='none',
        unionoption='DISTINCT',
        vc='cosmos08/Outings',
        in_1=batch_10_feature_vector_generation_subgraph.outputs.mergedsimilarity_out,
        in_2=batch_10_feature_vector_generation_subgraph.outputs.mergedsimilarity_out,
        in_3=batch_10_feature_vector_generation_subgraph.outputs.mergedsimilarity_out
    )
    backup_file_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterMergedAllSimilarity.ss',
        sourcepath=scope_basics_union_any_type_between_sstreams_func_instance.outputs.ssoutput_unioneddata_out
    )
    return {'master_feature_vectors_out': scope_basics_union_any_type_between_sstreams_func_instance.outputs.ssoutput_unioneddata_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating attractions_entity_feature_vector_generation_subgraph_3441")
    pipeline = attractions_entity_feature_vector_generation_subgraph_3441()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='attractions_entity_feature_vector_generation_subgraph_3441')
    print(datetime.now(), "Finish")
