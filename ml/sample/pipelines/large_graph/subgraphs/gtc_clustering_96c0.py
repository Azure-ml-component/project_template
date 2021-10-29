from datetime import datetime
from azure.ml.component import dsl
from resources import taprioritizedclustering_func, flattenclusters_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, flattenwikiclusters_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, generalselectcosmos_func, flattenwikiclusters_func, wikicenteredclustering_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, cosmospathcreator_rundate_func, generatetripple_record_ta_wiki_alltrails_func, alltrailscenteredclustering_func


print(datetime.now(), "Declaring pipeline: gtc_clustering_96c0")
@dsl.pipeline(name='gtc_clustering_96c0', default_compute_target='cpu-cluster')
def gtc_clustering_96c0(
    inputfile,
    conflation_date=''
):
    cosmospathcreator_rundate_func_9ce5_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/AlltrailsPairs.tsv""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate='9/14/2020'
    )
    taprioritizedclustering_func_instance = taprioritizedclustering_func(
        inputfile=inputfile
    )
    cosmospathcreator_rundate_func_5cba_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/WikiPairs.tsv""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate='9/14/2020'
    )
    cosmospathcreator_rundate_func_9944_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/TAPairs.tsv""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate='9/14/2020'
    )
    flattenclusters_func_instance = flattenclusters_func(
        inputfile2=taprioritizedclustering_func_instance.outputs.outputfile_out,
        inputfile1=inputfile
    )
    wikicenteredclustering_func_instance = wikicenteredclustering_func(
        inputfile2=taprioritizedclustering_func_instance.outputs.outputfile_out,
        inputfile1=inputfile
    )
    alltrailscenteredclustering_func_instance = alltrailscenteredclustering_func(
        inputfile2=taprioritizedclustering_func_instance.outputs.outputfile_out,
        inputfile1=inputfile
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_c8c7_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=flattenclusters_func_instance.outputs.outputfile_out,
        destinationpath=cosmospathcreator_rundate_func_9944_instance.outputs.createdpath_out
    )
    flattenwikiclusters_func_7be0_instance = flattenwikiclusters_func(
        inputfile1=wikicenteredclustering_func_instance.outputs.outputfile_out
    )
    flattenwikiclusters_func_1278_instance = flattenwikiclusters_func(
        inputfile1=alltrailscenteredclustering_func_instance.outputs.outputfile_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_c0de_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=flattenwikiclusters_func_7be0_instance.outputs.outputfile_out,
        destinationpath=cosmospathcreator_rundate_func_5cba_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_dbf0_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=flattenwikiclusters_func_1278_instance.outputs.outputfile_out,
        destinationpath=cosmospathcreator_rundate_func_9ce5_instance.outputs.createdpath_out
    )
    generatetripple_record_ta_wiki_alltrails_func_instance = generatetripple_record_ta_wiki_alltrails_func(
        vc='cosmos08/Outings',
        record_alltrails=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_dbf0_instance.outputs.cosmospath_out,
        record_ta=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_c8c7_instance.outputs.cosmospath_out,
        record_wiki=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_c0de_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1;',
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
        in1=generatetripple_record_ta_wiki_alltrails_func_instance.outputs.record_ta_wiki_alltrails_out
    )
    return {'outputtsv_out': generalselectcosmos_func_instance.outputs.outputtsv_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating gtc_clustering_96c0")
    pipeline = gtc_clustering_96c0()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='gtc_clustering_96c0')
    print(datetime.now(), "Finish")
