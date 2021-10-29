from datetime import datetime
from azure.ml.component import dsl
from attractions_entity_feature_vector_generation_subgraph_21bc import attractions_entity_feature_vector_generation_subgraph_21bc
from resources import scope_basics_union_any_type_between_sstreams_func


print(datetime.now(), "Declaring pipeline: batch_10_feature_vector_generation_7984")
@dsl.pipeline(name='batch_10_feature_vector_generation_7984', default_compute_target='cpu-cluster')
def batch_10_feature_vector_generation_7984(
    master_candidate_pairs_filtered_4,
    master_candidate_pairs_filtered_5,
    master_candidate_pairs_filtered_8,
    master_location_similarity,
    master_candidate_pairs_filtered_6,
    master_candidate_pairs_filtered_7,
    imagevectors,
    name_similarity_stream,
    master_candidate_pairs_filtered_9,
    master_candidate_pairs_filtered,
    master_candidate_pairs_filtered_2,
    master_candidate_pairs_filtered_10,
    master_attributes,
    master_candidate_pairs_filtered_3,
    number_of_images_to_compare='',
    conflationdate=''
):
    attractions_entity_feature_vector_generation_subgraph_70ea_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='13',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_3,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_c863_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='19',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_9,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_3215_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='15',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_5,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_5a47_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='16',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_6,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_3341_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='11',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_ae78_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='18',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_8,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_4234_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='20',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_10,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_e363_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='14',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_4,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_1ad7_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='12',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_2,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    attractions_entity_feature_vector_generation_subgraph_4c94_subgraph = attractions_entity_feature_vector_generation_subgraph_21bc(
        number_of_images_to_compare=number_of_images_to_compare,
        file_suffix='17',
        conflationdate=conflationdate,
        master_attributes=master_attributes,
        master_candidate_pairs_filtered=master_candidate_pairs_filtered_7,
        master_location_similarity=master_location_similarity,
        imagevectors=imagevectors,
        name_similarity_stream=name_similarity_stream
    )
    scope_basics_union_any_type_between_sstreams_func_instance = scope_basics_union_any_type_between_sstreams_func(
        referencedstreampath='none',
        clusterkey='SourceEntityId, CandidateEntityId',
        numberofpartitions='',
        sortkey='none',
        unionoption='DISTINCT',
        vc='cosmos08/Outings',
        in_1=attractions_entity_feature_vector_generation_subgraph_5a47_subgraph.outputs.master_feature_vectors_out,
        in_2=attractions_entity_feature_vector_generation_subgraph_3341_subgraph.outputs.master_feature_vectors_out,
        in_3=attractions_entity_feature_vector_generation_subgraph_1ad7_subgraph.outputs.master_feature_vectors_out,
        in_4=attractions_entity_feature_vector_generation_subgraph_70ea_subgraph.outputs.master_feature_vectors_out,
        in_5=attractions_entity_feature_vector_generation_subgraph_e363_subgraph.outputs.master_feature_vectors_out,
        in_6=attractions_entity_feature_vector_generation_subgraph_3215_subgraph.outputs.master_feature_vectors_out,
        in_7=attractions_entity_feature_vector_generation_subgraph_4c94_subgraph.outputs.master_feature_vectors_out,
        in_8=attractions_entity_feature_vector_generation_subgraph_ae78_subgraph.outputs.master_feature_vectors_out,
        in_9=attractions_entity_feature_vector_generation_subgraph_c863_subgraph.outputs.master_feature_vectors_out,
        in_10=attractions_entity_feature_vector_generation_subgraph_4234_subgraph.outputs.master_feature_vectors_out
    )
    return {'mergedsimilarity_out': scope_basics_union_any_type_between_sstreams_func_instance.outputs.ssoutput_unioneddata_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating batch_10_feature_vector_generation_7984")
    pipeline = batch_10_feature_vector_generation_7984()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='batch_10_feature_vector_generation_7984')
    print(datetime.now(), "Finish")
