from azure.ml.component import dsl


@dsl.pipeline(name='large_pipeline_graph', default_compute_target='cpu-cluster')
def large_pipeline_graph():
    from subgraphs.outings_entity_conflation_efb2 import outings_entity_conflation_efb2
    outings_entity_conflation_subgraph = outings_entity_conflation_efb2(
        conflation_date='07_20_2020',
        ground_truth_domain1='en.wikipedia.org',
        ground_truth_domain2='www.tripadvisor.com',
        ground_truth_domain3='www.alltrails.com',
        ground_truth_image_download_count='10',
        location_similarity_threshold='10.0',
        number_of_images_to_compare='3',
        name_similarity_threshold='4',
        qualitygateoverride='false'
    )
    return outings_entity_conflation_subgraph.outputs
