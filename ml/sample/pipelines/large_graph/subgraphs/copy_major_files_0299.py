from datetime import datetime
from azure.ml.component import dsl
from resources import conditional_passthrough_anyfile_func, replacecosmospath_func, cosmos_mirror_with_inputs_and_overwrite_func


print(datetime.now(), "Declaring pipeline: copy_major_files_0299")
@dsl.pipeline(name='copy_major_files_0299', default_compute_target='cpu-cluster')
def copy_major_files_0299(
    control,
    input,
    conflation_date=''
):
    conditional_passthrough_anyfile_func_instance = conditional_passthrough_anyfile_func(
        input=input,
        control=control
    )
    replacecosmospath_func_instance = replacecosmospath_func(
        srcstring="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        deststring='/local/EntityConflation/',
        input=conditional_passthrough_anyfile_func_instance.outputs.output_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        destinationpath=replacecosmospath_func_instance.outputs.count_out,
        sourcepath=input
    )
    return 


if __name__ == '__main__':
    print(datetime.now(), "Creating copy_major_files_0299")
    pipeline = copy_major_files_0299()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='copy_major_files_0299')
    print(datetime.now(), "Finish")
