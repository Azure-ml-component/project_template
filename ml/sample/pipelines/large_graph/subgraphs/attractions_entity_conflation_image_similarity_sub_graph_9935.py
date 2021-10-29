from datetime import datetime
from azure.ml.component import dsl
from new_subgraph_c95b import new_subgraph_c95b
from resources import generalselectcosmos_func, outings_cosine_similarity_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: attractions_entity_conflation_image_similarity_sub_graph_9935")
@dsl.pipeline(name='attractions_entity_conflation_image_similarity_sub_graph_9935', default_compute_target='cpu-cluster')
def attractions_entity_conflation_image_similarity_sub_graph_9935(
    master_candidate_pairs_filtered,
    imagevectors,
    number_of_images_to_compare='3',
    file_suffix=''
):
    generalselectcosmos_func_e651_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SourceEntities = SELECT SourceEntityId, ImageUrl AS SourceEntityPhotoUrl FROM In2 INNER JOIN In1 ON In2.SourceEntityId == In1.EntityId',
        select2='CandidateEntities = SELECT CandidateEntityId, ImageUrl AS CandidateEntityPhotoUrl FROM In2 INNER JOIN In1 ON In2.CandidateEntityId == In1.EntityId',
        select3='SELECT DISTINCT SourceEntityId, SourceEntityPhotoUrl, CandidateEntityId, CandidateEntityPhotoUrl FROM In2 INNER JOIN SourceEntities ON In2.SourceEntityId == SourceEntities.SourceEntityId INNER JOIN CandidateEntities ON In2.CandidateEntityId == CandidateEntities.CandidateEntityId',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId,CandidateEntityId INTO 100',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 15',
        in2=master_candidate_pairs_filtered,
        in1=imagevectors
    )
    new_subgraph_subgraph = new_subgraph_c95b(
        in1=generalselectcosmos_func_e651_instance.outputs.outputstream_out,
        in2=imagevectors
    )
    outings_cosine_similarity_func_instance = outings_cosine_similarity_func(
        vec1='Vec1',
        vec2='Vec2',
        delim=';',
        vc='cosmos08/Outings',
        scopeparams='',
        stream_in=new_subgraph_subgraph.outputs.outputstream_out
    )
    generalselectcosmos_func_24e3_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT SourceEntityId, SourceEntityPhotoUrl , CandidateEntityId, CandidateEntityPhotoUrl, Similarity AS ImageSimilarity FROM In1',
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
        scopeparams='-tokens 5',
        in1=outings_cosine_similarity_func_instance.outputs.output_ss_out
    )
    return {'image_similarity_output_stream_out': generalselectcosmos_func_24e3_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating attractions_entity_conflation_image_similarity_sub_graph_9935")
    pipeline = attractions_entity_conflation_image_similarity_sub_graph_9935()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='attractions_entity_conflation_image_similarity_sub_graph_9935')
    print(datetime.now(), "Finish")
