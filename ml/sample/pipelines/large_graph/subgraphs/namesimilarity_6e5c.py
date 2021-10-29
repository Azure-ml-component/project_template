from datetime import datetime
from azure.ml.component import dsl
from namesimilaritybylookupupdate_5811 import namesimilaritybylookupupdate_5811
from resources import cosmos_split_1_stream_to_10_func, scope_basics_union_any_type_between_sstreams_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: namesimilarity_6e5c")
@dsl.pipeline(name='namesimilarity_6e5c', default_compute_target='cpu-cluster')
def namesimilarity_6e5c(
    inputstream,
    file_suffix='',
    conflation_date=''
):
    generalselectcosmos_func_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT DISTINCT In1.SourceEntityName,  In1.CandidateEntityName FROM In1; ',
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
        in1=inputstream
    )
    cosmos_split_1_stream_to_10_func_instance = cosmos_split_1_stream_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputstream=generalselectcosmos_func_instance.outputs.outputstream_out
    )
    namesimilaritybylookupupdate_bb5f_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='01',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part0_out
    )
    namesimilaritybylookupupdate_1289_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='03',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part2_out
    )
    namesimilaritybylookupupdate_ffcd_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='02',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part1_out
    )
    namesimilaritybylookupupdate_83de_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='09',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part8_out
    )
    namesimilaritybylookupupdate_e0ea_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='08',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part7_out
    )
    namesimilaritybylookupupdate_98f7_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='07',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part6_out
    )
    namesimilaritybylookupupdate_ae6d_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='06',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part5_out
    )
    namesimilaritybylookupupdate_ce13_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='05',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part4_out
    )
    namesimilaritybylookupupdate_3c27_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='04',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part3_out
    )
    namesimilaritybylookupupdate_15b4_subgraph = namesimilaritybylookupupdate_5811(
        file_suffix='10',
        conflation_date=conflation_date,
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part9_out
    )
    scope_basics_union_any_type_between_sstreams_func_instance = scope_basics_union_any_type_between_sstreams_func(
        referencedstreampath='none',
        clusterkey='none',
        numberofpartitions='200',
        sortkey='none',
        unionoption='DISTINCT',
        vc='cosmos08/Outings',
        in_1=namesimilaritybylookupupdate_bb5f_subgraph.outputs.outputstream_out,
        in_2=namesimilaritybylookupupdate_ffcd_subgraph.outputs.outputstream_out,
        in_3=namesimilaritybylookupupdate_1289_subgraph.outputs.outputstream_out,
        in_4=namesimilaritybylookupupdate_3c27_subgraph.outputs.outputstream_out,
        in_5=namesimilaritybylookupupdate_ce13_subgraph.outputs.outputstream_out,
        in_6=namesimilaritybylookupupdate_ae6d_subgraph.outputs.outputstream_out,
        in_7=namesimilaritybylookupupdate_98f7_subgraph.outputs.outputstream_out,
        in_8=namesimilaritybylookupupdate_e0ea_subgraph.outputs.outputstream_out,
        in_9=namesimilaritybylookupupdate_83de_subgraph.outputs.outputstream_out,
        in_10=namesimilaritybylookupupdate_15b4_subgraph.outputs.outputstream_out
    )
    return {'ssoutput_unioneddata_out': scope_basics_union_any_type_between_sstreams_func_instance.outputs.ssoutput_unioneddata_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating namesimilarity_6e5c")
    pipeline = namesimilarity_6e5c()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='namesimilarity_6e5c')
    print(datetime.now(), "Finish")
