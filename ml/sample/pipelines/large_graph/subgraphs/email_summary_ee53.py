from datetime import datetime
from azure.ml.component import dsl
from resources import concat_generictsv_func, create_generic_tsv_func, concat_generictsv_func, concat_generictsv_func, concat_generictsv_func, concat_generictsv_func, aetheremailmodule_func, create_generic_tsv_func


print(datetime.now(), "Declaring pipeline: email_summary_ee53")
@dsl.pipeline(name='email_summary_ee53', default_compute_target='cpu-cluster')
def email_summary_ee53(
    input_2_3,
    input_1,
    input_2_2,
    input_2,
    recipients='',
    conflation_date=''
):
    create_generic_tsv_func_f6ad_instance = create_generic_tsv_func(
        text='<h2> Pipeline Stats </h2>\\n',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    create_generic_tsv_func_b734_instance = create_generic_tsv_func(
        text='<h2> Publishing Stats </h2>\\n',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    concat_generictsv_func_44e8_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=input_1,
        input_2=input_2_3
    )
    concat_generictsv_func_d710_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=create_generic_tsv_func_f6ad_instance.outputs.outputfile_out,
        input_2=input_2
    )
    concat_generictsv_func_1f95_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=concat_generictsv_func_44e8_instance.outputs.output_out,
        input_2=input_2_2
    )
    concat_generictsv_func_9188_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=create_generic_tsv_func_b734_instance.outputs.outputfile_out,
        input_2=concat_generictsv_func_1f95_instance.outputs.output_out
    )
    concat_generictsv_func_c865_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=concat_generictsv_func_9188_instance.outputs.output_out,
        input_2=concat_generictsv_func_d710_instance.outputs.output_out
    )
    aetheremailmodule_func_instance = aetheremailmodule_func(
        recipients=recipients,
        subject="""Entity Conflation Summary %s""" % (conflation_date),
        body=concat_generictsv_func_c865_instance.outputs.output_out
    )
    return 


if __name__ == '__main__':
    print(datetime.now(), "Creating email_summary_ee53")
    pipeline = email_summary_ee53()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='email_summary_ee53')
    print(datetime.now(), "Finish")
