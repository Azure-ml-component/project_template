from datetime import datetime
from azure.ml.component import dsl
from copy_major_files_0299 import copy_major_files_0299
from resources import cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, scope_basics_union_intersect_except_sstream_func, cosmos_mirror_with_inputs_and_overwrite_func, conditional_passthrough_anyfile_func


print(datetime.now(), "Declaring pipeline: publish_data_to_prod_cbdb")
@dsl.pipeline(name='publish_data_to_prod_cbdb', default_compute_target='cpu-cluster')
def publish_data_to_prod_cbdb(
    linkedentities,
    historicalstats,
    runstats,
    qgpass,
    conflation_date=''
):
    cosmospathcreator_rundate_func_5f6b_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/Resources/ConflationStats.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_a28d_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterAttributes.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_7fc4_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterAllCandidatePairsFiltered.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_009c_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterMergedAllSimilarity.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_4a56_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterCandidateUrls.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    copy_major_files_3dfa_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=linkedentities,
        control=qgpass
    )
    cosmospathcreator_rundate_func_aece_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterAllCandidatePairs.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_df12_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterCandidatePairs.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_9af6_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterEnhanced.snapshot.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    scope_basics_union_intersect_except_sstream_func_instance = scope_basics_union_intersect_except_sstream_func(
        uniontype='UNION ALL',
        clusteredbycolumns='RunDate',
        sortedbycolumns='RunDate,StatName',
        vc='cosmos08/Outings',
        scopeparams='',
        first=historicalstats,
        second=runstats
    )
    conditional_passthrough_anyfile_func_instance = conditional_passthrough_anyfile_func(
        input=cosmospathcreator_rundate_func_5f6b_instance.outputs.createdpath_out,
        control=qgpass
    )
    copy_major_files_cc31_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=cosmospathcreator_rundate_func_a28d_instance.outputs.createdpath_out,
        control=qgpass
    )
    copy_major_files_1279_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=cosmospathcreator_rundate_func_7fc4_instance.outputs.createdpath_out,
        control=qgpass
    )
    copy_major_files_ceec_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=cosmospathcreator_rundate_func_009c_instance.outputs.createdpath_out,
        control=qgpass
    )
    copy_major_files_0ed3_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=cosmospathcreator_rundate_func_4a56_instance.outputs.createdpath_out,
        control=qgpass
    )
    copy_major_files_64df_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=cosmospathcreator_rundate_func_aece_instance.outputs.createdpath_out,
        control=qgpass
    )
    copy_major_files_2e6d_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=cosmospathcreator_rundate_func_df12_instance.outputs.createdpath_out,
        control=qgpass
    )
    copy_major_files_1f06_subgraph = copy_major_files_0299(
        conflation_date=conflation_date,
        input=cosmospathcreator_rundate_func_9af6_instance.outputs.createdpath_out,
        control=qgpass
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        sourcepath=scope_basics_union_intersect_except_sstream_func_instance.outputs.outputss_out,
        destinationpath=conditional_passthrough_anyfile_func_instance.outputs.output_out
    )
    return 


if __name__ == '__main__':
    print(datetime.now(), "Creating publish_data_to_prod_cbdb")
    pipeline = publish_data_to_prod_cbdb()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='publish_data_to_prod_cbdb')
    print(datetime.now(), "Finish")
