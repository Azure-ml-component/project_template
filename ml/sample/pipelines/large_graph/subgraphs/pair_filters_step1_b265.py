from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, outing_distance_metric_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: pair_filters_step1_b265")
@dsl.pipeline(name='pair_filters_step1_b265', default_compute_target='cpu-cluster')
def pair_filters_step1_b265(
    namepairsim,
    attributes,
    pairs,
    location_similarity_threshold='',
    name_similarity_threshold='',
    conflation_date=''
):
    generalselectcosmos_func_9837_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SourceEntities = SELECT DISTINCT In2.SourceEntityId, In1.EntityLatitude AS SourceEntityLatitude, In1.EntityLongitude AS SourceEntityLongitude, In1.EntityName AS SourceEntityName FROM In2 INNER JOIN In1 ON In2.SourceEntityId == In1.EntityId;',
        select2='CandidateEntities = SELECT DISTINCT In2.CandidateEntityId, In1.EntityLatitude AS CandidateEntityLatitude, In1.EntityLongitude AS CandidateEntityLongitude,In1.EntityName AS CandidateEntityName FROM In2 INNER JOIN In1 ON In2.CandidateEntityId == In1.EntityId;',
        select3='SELECT DISTINCT In2.SourceEntityId, SourceEntityName, SourceEntityLatitude, SourceEntityLongitude, In2.CandidateEntityId, CandidateEntityName,CandidateEntityLatitude, CandidateEntityLongitude FROM In2 INNER JOIN SourceEntities ON In2.SourceEntityId == SourceEntities.SourceEntityId INNER JOIN CandidateEntities ON In2.CandidateEntityId == CandidateEntities.CandidateEntityId;',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=attributes,
        in2=pairs
    )
    outing_distance_metric_func_instance = outing_distance_metric_func(
        lat1='SourceEntityLatitude',
        lon1='SourceEntityLongitude',
        lat2='CandidateEntityLatitude',
        lon2='CandidateEntityLongitude',
        vc='cosmos08/Outings',
        scopeparams='',
        input_ss=generalselectcosmos_func_9837_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_c14e_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1 = SELECT SourceEntityId, SourceEntityName, SourceEntityLatitude, SourceEntityLongitude, CandidateEntityId, CandidateEntityName,CandidateEntityLatitude, CandidateEntityLongitude, Distance FROM In1 WHERE Distance < %s;""" % (location_similarity_threshold),
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
        in1=outing_distance_metric_func_instance.outputs.output_ss_out
    )
    generalselectcosmos_func_e51e_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1 = SELECT * FROM In1 WHERE NameSimilarity >= %s;""" % (name_similarity_threshold),
        select2='In11 = SELECT In2.*, In1.NameSimilarity FROM In1 INNER JOIN In2 ON In2.SourceEntityName== In1.SourceEntityName AND In2.CandidateEntityName== In1.CandidateEntityName;',
        select3='In12 = SELECT In2.*, In1.NameSimilarity FROM In1 INNER JOIN In2 ON In2.CandidateEntityName== In1.SourceEntityName AND In2.SourceEntityName== In1.CandidateEntityName;',
        select4='In1 = SELECT * FROM In11 UNION DISTINCT SELECT * FROM In12;',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in2=generalselectcosmos_func_c14e_instance.outputs.outputstream_out,
        in1=namepairsim
    )
    generalselectcosmos_func_bb18_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In2.* FROM In2 INNER JOIN In1 ON In2.SourceEntityId == In1.SourceEntityId AND In2.CandidateEntityId == In1.CandidateEntityId;',
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
        in1=generalselectcosmos_func_e51e_instance.outputs.outputstream_out,
        in2=pairs
    )
    generalselectcosmos_func_332a_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT In1.* FROM In2 INNER JOIN In1 ON In2.SourceEntityId == In1.SourceEntityId AND In2.CandidateEntityId == In1.CandidateEntityId;',
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
        in1=generalselectcosmos_func_e51e_instance.outputs.outputstream_out,
        in2=pairs
    )
    generalselectcosmos_func_b5f4_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT SourceEntityId, SourceEntityName, CandidateEntityId, CandidateEntityName, Distance FROM In1;',
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
        in1=generalselectcosmos_func_332a_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_ace2_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT SourceEntityId, SourceEntityName, CandidateEntityId, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=generalselectcosmos_func_332a_instance.outputs.outputstream_out
    )
    return {'location_out': generalselectcosmos_func_b5f4_instance.outputs.outputstream_out, 'outputstream_out': generalselectcosmos_func_bb18_instance.outputs.outputstream_out, 'outputtsv_out': generalselectcosmos_func_bb18_instance.outputs.outputtsv_out, 'masternamesimilarity_out': generalselectcosmos_func_ace2_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating pair_filters_step1_b265")
    pipeline = pair_filters_step1_b265()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='pair_filters_step1_b265')
    print(datetime.now(), "Finish")
