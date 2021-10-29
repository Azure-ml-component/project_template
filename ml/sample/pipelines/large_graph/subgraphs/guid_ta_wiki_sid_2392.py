from datetime import datetime
from azure.ml.component import dsl
from resources import cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, guid_ta_wiki_sid_prmeasure_func, cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func, create_generic_tsv_func, concat_generictsv_func, generalselectcosmos_func, copy_cosmospath_to_generictsv_func, tsv_to_html_func, cast_anyfile_to_generictsv_func


print(datetime.now(), "Declaring pipeline: guid_ta_wiki_sid_2392")
@dsl.pipeline(name='guid_ta_wiki_sid_2392', default_compute_target='cpu-cluster')
def guid_ta_wiki_sid_2392(
    recordtriples,
    master_attribute,
    conflation_date=''
):
    cosmospathcreator_rundate_func_fe4d_instance = cosmospathcreator_rundate_func(
        relativepath='/local/users/miren/DatasetForGUIDMeaurement.tsv',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_be33_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/TAPairs.tsv""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    create_generic_tsv_func_instance = create_generic_tsv_func(
        text='<strong>Record BVT</strong>\\n',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    cosmospathcreator_rundate_func_5f94_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/WikiPairs.tsv""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    guid_ta_wiki_sid_prmeasure_func_instance = guid_ta_wiki_sid_prmeasure_func(
        vc='cosmos08/Outings',
        dataset_pr_measure=cosmospathcreator_rundate_func_fe4d_instance.outputs.createdpath_out,
        master_ta_storyid=cosmospathcreator_rundate_func_be33_instance.outputs.createdpath_out,
        master_wiki_storyid=cosmospathcreator_rundate_func_5f94_instance.outputs.createdpath_out,
        master_attribute=master_attribute,
        master_sid_storyid=recordtriples
    )
    generalselectcosmos_func_2b04_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SELECT "%s".Replace("_","/") AS RunDate, "%s" AS Description, Statistic AS StatName, "BVT" AS Type, (float)Value AS Value FROM In1""" % (conflation_date, conflation_date),
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
        in1=guid_ta_wiki_sid_prmeasure_func_instance.outputs.stat_guid_ta_wiki_sid_out
    )
    generalselectcosmos_func_fde2_instance = generalselectcosmos_func(
        extractcols1='*',
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
        comment='Set up tsv',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=guid_ta_wiki_sid_prmeasure_func_instance.outputs.stat_guid_ta_wiki_sid_out
    )
    generalselectcosmos_func_e6b0_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_2b04_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_generictsv_func_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_fde2_instance.outputs.outputtsv_out
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
    return {'qg_data_out': generalselectcosmos_func_e6b0_instance.outputs.outputstream_out, 'stat_guid_ta_wiki_sid_out': guid_ta_wiki_sid_prmeasure_func_instance.outputs.stat_guid_ta_wiki_sid_out, 'htmlreport_out': concat_generictsv_func_instance.outputs.output_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating guid_ta_wiki_sid_2392")
    pipeline = guid_ta_wiki_sid_2392()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='guid_ta_wiki_sid_2392')
    print(datetime.now(), "Finish")
