from datetime import datetime
from azure.ml.component import dsl
from update_by_dateupdated_4cf1 import update_by_dateupdated_4cf1
from namesimilarity_6e5c import namesimilarity_6e5c
from resources import generalselectcosmos_func, outing_distance_metric_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, cosmos_mirror_with_inputs_and_overwrite_func, cosmospathcreator_rundate_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: pair_filters_w_top_10_updateonnamesim_0ce0")
@dsl.pipeline(name='pair_filters_w_top_10_updateonnamesim_0ce0', default_compute_target='cpu-cluster')
def pair_filters_w_top_10_updateonnamesim_0ce0(
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
    cosmospathcreator_rundate_func_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/MasterNameSimilarity.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
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
    generalselectcosmos_func_3c83_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT *, DateTime.UtcNow.ToString() AS DateUpdated FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId, CandidateEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=outing_distance_metric_func_instance.outputs.output_ss_out
    )
    generalselectcosmos_func_d5e3_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1 = SELECT * FROM In1 WHERE Distance < %s;""" % (location_similarity_threshold),
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
    update_by_dateupdated_subgraph = update_by_dateupdated_4cf1(
        datekey='SourceEntityId,CandidateEntityId',
        in1=generalselectcosmos_func_3c83_instance.outputs.outputstream_out
    )
    namesimilarity_subgraph = namesimilarity_6e5c(
        file_suffix='',
        conflation_date=conflation_date,
        inputstream=generalselectcosmos_func_d5e3_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_e51e_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In11 = SELECT In1.*, In3.NameSimilarity FROM In1 INNER JOIN In3 ON In3.SourceEntityName== In1.SourceEntityName AND In3.CandidateEntityName== In1.CandidateEntityName;',
        select2='In12 = SELECT In1.*, In3.NameSimilarity FROM In1 INNER JOIN In3 ON In3.CandidateEntityName== In1.SourceEntityName AND In3.SourceEntityName== In1.CandidateEntityName;',
        select3='In1 = SELECT * FROM In11 UNION DISTINCT SELECT * FROM In12;',
        select4="""In1 = SELECT * FROM In1 WHERE Distance < %s AND NameSimilarity >= %s;""" % (location_similarity_threshold, name_similarity_threshold),
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=generalselectcosmos_func_d5e3_instance.outputs.outputstream_out,
        in3=namesimilarity_subgraph.outputs.ssoutput_unioneddata_out,
        in2=pairs
    )
    generalselectcosmos_func_bb18_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT In2.*,NameSimilarity - Distance AS NameDist FROM In2 INNER JOIN In1 ON In2.SourceEntityId == In1.SourceEntityId AND In2.CandidateEntityId == In1.CandidateEntityId;',
        select2='sIn = SELECT *, ROW_NUMBER() OVER(PARTITION BY SourceEntityId, CandidateEntityDomain ORDER BY NameDist DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='cIn = SELECT *, ROW_NUMBER() OVER(PARTITION BY CandidateEntityId, SourceEntityDomain ORDER BY NameDist DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select4='In1 = SELECT * FROM sIn UNION DISTINCT SELECT * FROM cIn',
        select5='SELECT In2.* FROM In2 INNER JOIN In1 ON In2.SourceEntityId == In1.SourceEntityId AND In2.CandidateEntityId == In1.CandidateEntityId;',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=generalselectcosmos_func_e51e_instance.outputs.outputstream_out,
        in2=pairs
    )
    generalselectcosmos_func_332a_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT In1.* FROM In2 INNER JOIN In1 ON In2.SourceEntityId == In1.SourceEntityId AND In2.CandidateEntityId == In1.CandidateEntityId;',
        select2='SELECT SourceEntityId, SourceEntityName, CandidateEntityId, CandidateEntityName, NameSimilarity FROM In1;',
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
        in3=namesimilarity_subgraph.outputs.ssoutput_unioneddata_out,
        in2=pairs
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_332a_instance.outputs.outputstream_out,
        destinationpath=cosmospathcreator_rundate_func_instance.outputs.createdpath_out
    )
    return {'location_out': update_by_dateupdated_subgraph.outputs.filteredss_out, 'top10pairfilter_out': generalselectcosmos_func_bb18_instance.outputs.outputstream_out, 'outputtsv_out': generalselectcosmos_func_bb18_instance.outputs.outputtsv_out, 'masternamesimilarity_out': generalselectcosmos_func_332a_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating pair_filters_w_top_10_updateonnamesim_0ce0")
    pipeline = pair_filters_w_top_10_updateonnamesim_0ce0()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='pair_filters_w_top_10_updateonnamesim_0ce0')
    print(datetime.now(), "Finish")
