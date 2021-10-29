from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, cosmos_split_1_stream_to_10_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: split_10_with_clustering_c32e")
@dsl.pipeline(name='split_10_with_clustering_c32e', default_compute_target='cpu-cluster')
def split_10_with_clustering_c32e(
    inputstream,
    clustercol='',
    sortcol=''
):
    cosmos_split_1_stream_to_10_func_instance = cosmos_split_1_stream_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputstream=inputstream
    )
    generalselectcosmos_func_5674_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part0_out
    )
    generalselectcosmos_func_cff0_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part1_out
    )
    generalselectcosmos_func_3d87_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part2_out
    )
    generalselectcosmos_func_f5a9_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part3_out
    )
    generalselectcosmos_func_14b3_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part4_out
    )
    generalselectcosmos_func_d988_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part5_out
    )
    generalselectcosmos_func_702f_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part6_out
    )
    generalselectcosmos_func_7c7b_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part7_out
    )
    generalselectcosmos_func_65bf_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part8_out
    )
    generalselectcosmos_func_fd36_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause="""CLUSTERED BY %s SORTED BY %s""" % (clustercol, sortcol),
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_split_1_stream_to_10_func_instance.outputs.part9_out
    )
    return {'part0_out': generalselectcosmos_func_5674_instance.outputs.outputstream_out, 'part1_out': generalselectcosmos_func_cff0_instance.outputs.outputstream_out, 'part2_out': generalselectcosmos_func_3d87_instance.outputs.outputstream_out, 'part3_out': generalselectcosmos_func_f5a9_instance.outputs.outputstream_out, 'part4_out': generalselectcosmos_func_14b3_instance.outputs.outputstream_out, 'part5_out': generalselectcosmos_func_d988_instance.outputs.outputstream_out, 'part6_out': generalselectcosmos_func_702f_instance.outputs.outputstream_out, 'part7_out': generalselectcosmos_func_7c7b_instance.outputs.outputstream_out, 'part8_out': generalselectcosmos_func_65bf_instance.outputs.outputstream_out, 'part9_out': generalselectcosmos_func_fd36_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating split_10_with_clustering_c32e")
    pipeline = split_10_with_clustering_c32e()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='split_10_with_clustering_c32e')
    print(datetime.now(), "Finish")
