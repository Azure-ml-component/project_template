from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, sstreamunion2_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: format_qg_data_e7fe")
@dsl.pipeline(name='format_qg_data_e7fe', default_compute_target='cpu-cluster')
def format_qg_data_e7fe(
    in1_2,
    in1,
    conflation_date=''
):
    generalselectcosmos_func_6b90_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SELECT "%s".Replace("_","/") AS RunDate, "%s" AS Description, Statistic AS StatName, "Metric" AS Type, (float)Value AS Value FROM In1""" % (conflation_date, conflation_date),
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Set up Format',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=in1_2
    )
    generalselectcosmos_func_2b03_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SELECT "%s".Replace("_","/") AS RunDate, "%s" AS Description, EntityDomain AS StatName, "Metric" AS Type, (float)count AS Value FROM In1""" % (conflation_date, conflation_date),
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Set up Format',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=in1
    )
    generalselectcosmos_func_7681_instance = generalselectcosmos_func(
        extractcols1='RunDate:DateTime, Description:string, StatName:string, Type:string, Value:float',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT RunDate, Description, StatName == "Total Records" ? "Total Attribute Records":StatName AS StatName, Type, Value FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='convert to ss',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_6b90_instance.outputs.outputtsv_out
    )
    generalselectcosmos_func_35d2_instance = generalselectcosmos_func(
        extractcols1='RunDate:DateTime, Description:string, StatName:string, Type:string, Value:float',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='convert to ss',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_2b03_instance.outputs.outputtsv_out
    )
    sstreamunion2_func_instance = sstreamunion2_func(
        clusterbycolumn='RunDate',
        vc='vc://cosmos08/Outings',
        in1=generalselectcosmos_func_35d2_instance.outputs.outputstream_out,
        in2=generalselectcosmos_func_7681_instance.outputs.outputstream_out
    )
    return {'output_out': generalselectcosmos_func_7681_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating format_qg_data_e7fe")
    pipeline = format_qg_data_e7fe()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='format_qg_data_e7fe')
    print(datetime.now(), "Finish")
