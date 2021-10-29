from datetime import datetime
from azure.ml.component import dsl
from resources import conditional_passthrough_anyfile_func, not_conditional_decision_logic_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, is_file_empty_to_controloutput_func, sstream_to_tsv_aether_func, tsv_to_html_func


print(datetime.now(), "Declaring pipeline: set_up_email_06da")
@dsl.pipeline(name='set_up_email_06da', default_compute_target='cpu-cluster')
def set_up_email_06da(
    input,
    path
):
    copy_cosmospath_to_generictsv_func_2c7d_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=path
    )
    is_file_empty_to_controloutput_func_instance = is_file_empty_to_controloutput_func(
        input=copy_cosmospath_to_generictsv_func_2c7d_instance.outputs.tsv_out
    )
    not_conditional_decision_logic_func_instance = not_conditional_decision_logic_func(
        control=is_file_empty_to_controloutput_func_instance.outputs.control_out
    )
    conditional_passthrough_anyfile_func_instance = conditional_passthrough_anyfile_func(
        control=not_conditional_decision_logic_func_instance.outputs.control_out,
        input=input
    )
    copy_cosmospath_to_generictsv_func_ea3b_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=conditional_passthrough_anyfile_func_instance.outputs.output_out
    )
    sstream_to_tsv_aether_func_instance = sstream_to_tsv_aether_func(
        addheader='true',
        commasepcolumnstokeep='*',
        aetherstructuredstream=copy_cosmospath_to_generictsv_func_ea3b_instance.outputs.tsv_out
    )
    tsv_to_html_func_instance = tsv_to_html_func(
        generatehlinkforurl='true',
        tsv=sstream_to_tsv_aether_func_instance.outputs.outputtsv_out
    )
    return {'control_out': is_file_empty_to_controloutput_func_instance.outputs.control_out, 'htmlreport_out': tsv_to_html_func_instance.outputs.htmlreport_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating set_up_email_06da")
    pipeline = set_up_email_06da()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='set_up_email_06da')
    print(datetime.now(), "Finish")
