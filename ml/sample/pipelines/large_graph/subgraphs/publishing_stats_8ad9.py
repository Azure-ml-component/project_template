from datetime import datetime
from azure.ml.component import dsl
from resources import outings_entity_conflation_publishing_statistics_func, generalselectcosmos_func, generalselectcosmos_func, cosmospathcreator_rundate_func, cosmos_mirror_with_inputs_and_overwrite_func, copy_cosmospath_to_generictsv_func, tsv_to_html_func, cast_anyfile_to_generictsv_func, create_generic_tsv_func, concat_generictsv_func


print(datetime.now(), "Declaring pipeline: publishing_stats_8ad9")
@dsl.pipeline(name='publishing_stats_8ad9', default_compute_target='cpu-cluster')
def publishing_stats_8ad9(
    ta_satori_links,
    master_attr,
    record_triples,
    conflation_date=''
):
    create_generic_tsv_func_instance = create_generic_tsv_func(
        text='<strong>Publishing Statistics </strong>\\n',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    cosmospathcreator_rundate_func_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Stats/PublishingStats.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    outings_entity_conflation_publishing_statistics_func_instance = outings_entity_conflation_publishing_statistics_func(
        vc='cosmos08/Outings',
        scopeparams='',
        record_triples=record_triples,
        ta_satori_links=ta_satori_links,
        master_attr=master_attr
    )
    generalselectcosmos_func_e858_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SELECT "%s".Replace("_","/") AS RunDate, "%s" AS Description, Description AS StatName, "Metric" AS Type, (float)Value AS Value FROM In1""" % (conflation_date, conflation_date),
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
        in1=outings_entity_conflation_publishing_statistics_func_instance.outputs.stats_ss_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_entity_conflation_publishing_statistics_func_instance.outputs.stats_ss_out,
        destinationpath=cosmospathcreator_rundate_func_instance.outputs.createdpath_out
    )
    copy_cosmospath_to_generictsv_func_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=outings_entity_conflation_publishing_statistics_func_instance.outputs.stats_tsv_out
    )
    generalselectcosmos_func_b1a7_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_e858_instance.outputs.outputtsv_out
    )
    tsv_to_html_func_instance = tsv_to_html_func(
        generatehlinkforurl='true',
        tsv=copy_cosmospath_to_generictsv_func_instance.outputs.tsv_out
    )
    cast_anyfile_to_generictsv_func_instance = cast_anyfile_to_generictsv_func(
        input=tsv_to_html_func_instance.outputs.htmlreport_out
    )
    concat_generictsv_func_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=create_generic_tsv_func_instance.outputs.outputfile_out,
        input_2=cast_anyfile_to_generictsv_func_instance.outputs.outputtsv_out
    )
    return {'qg_data_out': generalselectcosmos_func_b1a7_instance.outputs.outputstream_out, 'htmlreport_out': concat_generictsv_func_instance.outputs.output_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating publishing_stats_8ad9")
    pipeline = publishing_stats_8ad9()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='publishing_stats_8ad9')
    print(datetime.now(), "Finish")
