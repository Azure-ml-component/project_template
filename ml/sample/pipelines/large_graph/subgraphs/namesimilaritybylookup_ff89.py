from datetime import datetime
from azure.ml.component import dsl
from namesimilarityupdate_subgraph_b72b import namesimilarityupdate_subgraph_b72b
from resources import generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func, copy_cosmospath_to_cosmospathtsv_func, generalselectcosmos_func, generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func, generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func, scope_basics_union_any_type_between_sstreams_func, copy_cosmospath_to_cosmospathtsv_func, cosmos_split_1_stream_to_10_func, generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func, generalselectcosmos_func, generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func, generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func, generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func, generalselectcosmos_func, copy_cosmospath_to_cosmospathtsv_func


print(datetime.now(), "Declaring pipeline: namesimilaritybylookup_ff89")
@dsl.pipeline(name='namesimilaritybylookup_ff89', default_compute_target='cpu-cluster')
def namesimilaritybylookup_ff89(
    in1,
    file_suffix='',
    conflation_date='',
    sub_suffix='',
    end_suffix=''
):
    cosmos_split_1_stream_to_10_func_instance = cosmos_split_1_stream_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputstream=in1
    )
    generalselectcosmos_func_d161_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part4_out
    )
    generalselectcosmos_func_c8fe_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part3_out
    )
    generalselectcosmos_func_3b50_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part0_out
    )
    generalselectcosmos_func_7678_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part2_out
    )
    generalselectcosmos_func_95ff_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part1_out
    )
    generalselectcosmos_func_6507_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part5_out
    )
    generalselectcosmos_func_0cf6_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part6_out
    )
    generalselectcosmos_func_8121_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part7_out
    )
    generalselectcosmos_func_9839_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part9_out
    )
    generalselectcosmos_func_2cad_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        scopeparams='-tokens 25',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part8_out
    )
    copy_cosmospath_to_cosmospathtsv_func_c894_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_d161_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_fd15_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_c8fe_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_183b_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_3b50_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_6582_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_7678_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_ec00_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_95ff_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_edc8_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_6507_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_59c2_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_0cf6_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_98f5_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_8121_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_9bf0_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_9839_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_cosmospathtsv_func_3e2a_instance = copy_cosmospath_to_cosmospathtsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_2cad_instance.outputs.outputtsv_out
    )
    namesimilarityupdate_subgraph_421c_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='05',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_c894_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_d012_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='04',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_fd15_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_9720_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='01',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_183b_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_2b8e_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='03',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_6582_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_75f1_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='02',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_ec00_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_83ae_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='06',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_edc8_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_8b83_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='07',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_59c2_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_48bc_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='08',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_98f5_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_3383_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='10',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_9bf0_instance.outputs.tsv_out
    )
    namesimilarityupdate_subgraph_f6ac_subgraph = namesimilarityupdate_subgraph_b72b(
        conflation_date=conflation_date,
        file_suffix=file_suffix,
        sub_suffix=sub_suffix,
        end_suffix='09',
        inputfile2=copy_cosmospath_to_cosmospathtsv_func_3e2a_instance.outputs.tsv_out
    )
    scope_basics_union_any_type_between_sstreams_func_instance = scope_basics_union_any_type_between_sstreams_func(
        referencedstreampath='none',
        clusterkey='none',
        numberofpartitions='200',
        sortkey='none',
        unionoption='DISTINCT',
        vc='cosmos08/Outings',
        in_1=namesimilarityupdate_subgraph_9720_subgraph.outputs.outputstream_out,
        in_2=namesimilarityupdate_subgraph_75f1_subgraph.outputs.outputstream_out,
        in_3=namesimilarityupdate_subgraph_2b8e_subgraph.outputs.outputstream_out,
        in_4=namesimilarityupdate_subgraph_d012_subgraph.outputs.outputstream_out,
        in_5=namesimilarityupdate_subgraph_421c_subgraph.outputs.outputstream_out,
        in_6=namesimilarityupdate_subgraph_83ae_subgraph.outputs.outputstream_out,
        in_7=namesimilarityupdate_subgraph_8b83_subgraph.outputs.outputstream_out,
        in_8=namesimilarityupdate_subgraph_48bc_subgraph.outputs.outputstream_out,
        in_9=namesimilarityupdate_subgraph_f6ac_subgraph.outputs.outputstream_out,
        in_10=namesimilarityupdate_subgraph_3383_subgraph.outputs.outputstream_out
    )
    return {'outputstream_out': scope_basics_union_any_type_between_sstreams_func_instance.outputs.ssoutput_unioneddata_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating namesimilaritybylookup_ff89")
    pipeline = namesimilaritybylookup_ff89()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='namesimilaritybylookup_ff89')
    print(datetime.now(), "Finish")
