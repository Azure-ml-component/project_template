from datetime import datetime
from azure.ml.component import dsl
from resources import namepairsimilaritylookuptableupdates_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, generalselectcosmos_func, cosmospathcreator_rundate_func


print(datetime.now(), "Declaring pipeline: namesimilarityupdate_subgraph_b72b")
@dsl.pipeline(name='namesimilarityupdate_subgraph_b72b', default_compute_target='cpu-cluster')
def namesimilarityupdate_subgraph_b72b(
    inputfile2,
    conflation_date='',
    file_suffix='',
    sub_suffix='',
    end_suffix=''
):
    cosmospathcreator_rundate_func_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/FeatureVectorGeneration/Splits/NameSimilarity.%s.%s.%s.tsv""" % (conflation_date, file_suffix, sub_suffix, end_suffix),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    namepairsimilaritylookuptableupdates_func_instance = namepairsimilaritylookuptableupdates_func(
        inputfile1=inputfile2
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=namepairsimilaritylookuptableupdates_func_instance.outputs.outputfile1_out,
        destinationpath=cosmospathcreator_rundate_func_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_instance = generalselectcosmos_func(
        extractcols1='SourceEntityName: string, CandidateEntityName: string, NameSimilarity: double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1; ',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_instance.outputs.cosmospath_out
    )
    return {'outputstream_out': generalselectcosmos_func_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating namesimilarityupdate_subgraph_b72b")
    pipeline = namesimilarityupdate_subgraph_b72b()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='namesimilarityupdate_subgraph_b72b')
    print(datetime.now(), "Finish")
