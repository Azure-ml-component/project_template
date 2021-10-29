from datetime import datetime
from azure.ml.component import dsl
from namesimilaritybylookup_ff89 import namesimilaritybylookup_ff89
from resources import scope_basics_union_any_type_between_sstreams_func, cosmos_split_1_stream_to_10_func


print(datetime.now(), "Declaring pipeline: namesimilaritybylookupupdate_5811")
@dsl.pipeline(name='namesimilaritybylookupupdate_5811', default_compute_target='cpu-cluster')
def namesimilaritybylookupupdate_5811(
    in1,
    file_suffix='',
    conflation_date=''
):
    cosmos_split_1_stream_to_10_func_instance = cosmos_split_1_stream_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputstream=in1
    )
    namesimilaritybylookup_99db_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='02',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part1_out
    )
    namesimilaritybylookup_d6fd_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='03',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part2_out
    )
    namesimilaritybylookup_e60d_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='04',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part3_out
    )
    namesimilaritybylookup_7f89_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='05',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part4_out
    )
    namesimilaritybylookup_ebbc_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='06',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part5_out
    )
    namesimilaritybylookup_528e_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='07',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part6_out
    )
    namesimilaritybylookup_dca2_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='08',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part7_out
    )
    namesimilaritybylookup_912a_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='10',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part9_out
    )
    namesimilaritybylookup_f87d_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='09',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part8_out
    )
    namesimilaritybylookup_12f6_subgraph = namesimilaritybylookup_ff89(
        file_suffix=file_suffix,
        conflation_date=conflation_date,
        sub_suffix='01',
        end_suffix='',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part0_out
    )
    scope_basics_union_any_type_between_sstreams_func_instance = scope_basics_union_any_type_between_sstreams_func(
        referencedstreampath='none',
        clusterkey='none',
        numberofpartitions='200',
        sortkey='none',
        unionoption='DISTINCT',
        vc='cosmos08/Outings',
        in_1=namesimilaritybylookup_12f6_subgraph.outputs.outputstream_out,
        in_2=namesimilaritybylookup_99db_subgraph.outputs.outputstream_out,
        in_3=namesimilaritybylookup_d6fd_subgraph.outputs.outputstream_out,
        in_4=namesimilaritybylookup_e60d_subgraph.outputs.outputstream_out,
        in_5=namesimilaritybylookup_7f89_subgraph.outputs.outputstream_out,
        in_6=namesimilaritybylookup_ebbc_subgraph.outputs.outputstream_out,
        in_7=namesimilaritybylookup_528e_subgraph.outputs.outputstream_out,
        in_8=namesimilaritybylookup_dca2_subgraph.outputs.outputstream_out,
        in_9=namesimilaritybylookup_f87d_subgraph.outputs.outputstream_out,
        in_10=namesimilaritybylookup_912a_subgraph.outputs.outputstream_out
    )
    return {'outputstream_out': scope_basics_union_any_type_between_sstreams_func_instance.outputs.ssoutput_unioneddata_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating namesimilaritybylookupupdate_5811")
    pipeline = namesimilaritybylookupupdate_5811()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='namesimilaritybylookupupdate_5811')
    print(datetime.now(), "Finish")
