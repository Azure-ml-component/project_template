from datetime import datetime
from azure.ml.component import dsl
from resources import cosmospathcreator_rundate_func, cosmos_mirror_with_inputs_and_overwrite_func, generalselectcosmos_func, cast_anyfile_to_generictsv_func, copy_cosmospath_to_generictsv_func, tsv_to_html_func, concat_generictsv_func, create_generic_tsv_func, cosmospathcreator_rundate_func, cosmos_mirror_with_inputs_and_overwrite_func, concat_generictsv_func, cast_anyfile_to_generictsv_func, copy_cosmospath_to_generictsv_func, tsv_to_html_func, generalselectcosmos_func, concat_generictsv_func, create_generic_tsv_func


print(datetime.now(), "Declaring pipeline: generate_html_report_37c3")
@dsl.pipeline(name='generate_html_report_37c3', default_compute_target='cpu-cluster')
def generate_html_report_37c3(
    in1_2,
    in1,
    conflation_date=''
):
    generalselectcosmos_func_f3a8_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.*;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='convert to tsv',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=in1_2
    )
    cosmospathcreator_rundate_func_1119_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Stats/ConflationMonitor.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    create_generic_tsv_func_194a_instance = create_generic_tsv_func(
        text='<strong> Domain Coverage </strong>\\n',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    create_generic_tsv_func_4892_instance = create_generic_tsv_func(
        text='<strong>Feature and Similarity Coverage </strong>\\n',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    cosmospathcreator_rundate_func_4faf_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Stats/ConflationDomains.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    generalselectcosmos_func_e6e6_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.*;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='convert to tsv',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=in1
    )
    copy_cosmospath_to_generictsv_func_02e2_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_f3a8_instance.outputs.outputtsv_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_deef_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_f3a8_instance.outputs.outputstream_out,
        destinationpath=cosmospathcreator_rundate_func_4faf_instance.outputs.createdpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_f115_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_e6e6_instance.outputs.outputstream_out,
        destinationpath=cosmospathcreator_rundate_func_1119_instance.outputs.createdpath_out
    )
    copy_cosmospath_to_generictsv_func_9c8a_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_e6e6_instance.outputs.outputtsv_out
    )
    tsv_to_html_func_c6d7_instance = tsv_to_html_func(
        generatehlinkforurl='true',
        tsv=copy_cosmospath_to_generictsv_func_02e2_instance.outputs.tsv_out
    )
    tsv_to_html_func_5e0a_instance = tsv_to_html_func(
        generatehlinkforurl='true',
        tsv=copy_cosmospath_to_generictsv_func_9c8a_instance.outputs.tsv_out
    )
    cast_anyfile_to_generictsv_func_76da_instance = cast_anyfile_to_generictsv_func(
        input=tsv_to_html_func_c6d7_instance.outputs.htmlreport_out
    )
    cast_anyfile_to_generictsv_func_cb2a_instance = cast_anyfile_to_generictsv_func(
        input=tsv_to_html_func_5e0a_instance.outputs.htmlreport_out
    )
    concat_generictsv_func_4888_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=create_generic_tsv_func_194a_instance.outputs.outputfile_out,
        input_2=cast_anyfile_to_generictsv_func_76da_instance.outputs.outputtsv_out
    )
    concat_generictsv_func_5cde_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=create_generic_tsv_func_4892_instance.outputs.outputfile_out,
        input_2=cast_anyfile_to_generictsv_func_cb2a_instance.outputs.outputtsv_out
    )
    concat_generictsv_func_b45d_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=concat_generictsv_func_4888_instance.outputs.output_out,
        input_2=concat_generictsv_func_5cde_instance.outputs.output_out
    )
    return {'output_out': concat_generictsv_func_5cde_instance.outputs.output_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating generate_html_report_37c3")
    pipeline = generate_html_report_37c3()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='generate_html_report_37c3')
    print(datetime.now(), "Finish")
