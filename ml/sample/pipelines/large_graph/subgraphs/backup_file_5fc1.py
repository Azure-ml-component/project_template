from datetime import datetime
from azure.ml.component import dsl
from resources import cosmos_mirror_with_inputs_and_overwrite_func, cosmospathcreator_rundate_func


print(datetime.now(), "Declaring pipeline: backup_file_5fc1")
@dsl.pipeline(name='backup_file_5fc1', default_compute_target='cpu-cluster')
def backup_file_5fc1(
    sourcepath,
    backupdirectory='/local/EntityConflation/Backups/@@Conflation_Date@@/',
    conflation_date='',
    vc='vc://cosmos08/Outings',
    backupexp='45',
    filename=''
):
    cosmospathcreator_rundate_func_instance = cosmospathcreator_rundate_func(
        relativepath="""%s%s""" % (backupdirectory, filename),
        vc=vc,
        rundate='12_28_2020'
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration="""%s""" % (backupexp),
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        destinationpath=cosmospathcreator_rundate_func_instance.outputs.createdpath_out,
        sourcepath=sourcepath
    )
    return {'backuppath_out': cosmos_mirror_with_inputs_and_overwrite_func_instance.outputs.destinationpath_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating backup_file_5fc1")
    pipeline = backup_file_5fc1()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='backup_file_5fc1')
    print(datetime.now(), "Finish")
