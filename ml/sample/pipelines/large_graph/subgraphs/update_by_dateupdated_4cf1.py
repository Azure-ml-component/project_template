from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, outings_remove_columns_from_structured_stream_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: update_by_dateupdated_4cf1")
@dsl.pipeline(name='update_by_dateupdated_4cf1', default_compute_target='cpu-cluster')
def update_by_dateupdated_4cf1(
    in1,
    datekey=''
):
    generalselectcosmos_func_c6f2_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SELECT *, ROW_NUMBER() OVER (PARTITION BY %s ORDER BY DateTime.Parse(DateUpdated) DESC) AS Rn FROM In1""" % (datekey),
        select2='SELECT * WHERE Rn == 1;',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Time update',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=in1
    )
    outings_remove_columns_from_structured_stream_func_instance = outings_remove_columns_from_structured_stream_func(
        columns_to_remove='Rn',
        vc='cosmos08/Outings',
        scopeparams='',
        input_stream=generalselectcosmos_func_c6f2_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_d13e_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT "Before" AS Stat, COUNT(*) AS Count FROM In2 UNION DISTINCT SELECT "After" AS Stat, COUNT(*) AS Count FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Time update',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_c6f2_instance.outputs.outputstream_out,
        in2=in1
    )
    return {'filteredss_out': outings_remove_columns_from_structured_stream_func_instance.outputs.output_stream_out, 'counts_out': generalselectcosmos_func_d13e_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating update_by_dateupdated_4cf1")
    pipeline = update_by_dateupdated_4cf1()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='update_by_dateupdated_4cf1')
    print(datetime.now(), "Finish")
