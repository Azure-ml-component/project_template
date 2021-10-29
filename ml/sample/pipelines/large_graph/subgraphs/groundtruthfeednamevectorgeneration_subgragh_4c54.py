from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, copy_cosmospath_to_generictsv_func, reversegeocoder_func, buildentitynamedictionary_func, buildentitynamevectors_func


print(datetime.now(), "Declaring pipeline: groundtruthfeednamevectorgeneration_subgragh_4c54")
@dsl.pipeline(name='groundtruthfeednamevectorgeneration_subgragh_4c54', default_compute_target='cpu-cluster')
def groundtruthfeednamevectorgeneration_subgragh_4c54(
    groundtruthfeed
):
    generalselectcosmos_func_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT Id, EntityName, Latitude, Longitude FROM In1;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY Id;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=groundtruthfeed
    )
    copy_cosmospath_to_generictsv_func_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_instance.outputs.outputtsv_out
    )
    reversegeocoder_func_instance = reversegeocoder_func(
        inputfile=copy_cosmospath_to_generictsv_func_instance.outputs.tsv_out
    )
    buildentitynamedictionary_func_instance = buildentitynamedictionary_func(
        inputfile=reversegeocoder_func_instance.outputs.outputfile_out
    )
    buildentitynamevectors_func_instance = buildentitynamevectors_func(
        inputfile1=reversegeocoder_func_instance.outputs.outputfile_out,
        inputfile2=buildentitynamedictionary_func_instance.outputs.outputfile1_out
    )
    return {'locationtogroundtruthfeedid_out': buildentitynamedictionary_func_instance.outputs.outputfile2_out, 'groundtruthfeedtoitsnamevector_out': buildentitynamevectors_func_instance.outputs.outputfile_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating groundtruthfeednamevectorgeneration_subgragh_4c54")
    pipeline = groundtruthfeednamevectorgeneration_subgragh_4c54()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='groundtruthfeednamevectorgeneration_subgragh_4c54')
    print(datetime.now(), "Finish")
