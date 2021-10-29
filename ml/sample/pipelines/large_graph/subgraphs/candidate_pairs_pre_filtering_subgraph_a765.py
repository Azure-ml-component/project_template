from datetime import datetime
from azure.ml.component import dsl
from pair_filters_step1_b265 import pair_filters_step1_b265
from pair_filters_w_top_10_updateonnamesim_0ce0 import pair_filters_w_top_10_updateonnamesim_0ce0
from backup_file_5fc1 import backup_file_5fc1
from update_by_dateupdated_4cf1 import update_by_dateupdated_4cf1
from backup_file_9ad6 import backup_file_9ad6
from cross_join_d285 import cross_join_d285
from backup_file_bdd9 import backup_file_bdd9
from resources import cosmos_mirror_with_inputs_and_overwrite_func, generalselectcosmos_func, createcosmospathfreely_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, outings_source_url_id_generator_func, outings_source_url_id_generator_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: candidate_pairs_pre_filtering_subgraph_a765")
@dsl.pipeline(name='candidate_pairs_pre_filtering_subgraph_a765', default_compute_target='cpu-cluster')
def candidate_pairs_pre_filtering_subgraph_a765(
    namepairsim,
    master_canddiate_urls,
    master_attributes,
    location_similarity_threshold='',
    name_similarity_threshold='',
    conflation_date=''
):
    outings_source_url_id_generator_func_6313_instance = outings_source_url_id_generator_func(
        url_col='CandidateEntityUrl',
        url_id_col='CandidateEntityUrlId',
        vc='cosmos08/Outings',
        scopeparams='',
        input=master_canddiate_urls
    )
    outings_source_url_id_generator_func_289a_instance = outings_source_url_id_generator_func(
        url_col='EntityUrl',
        url_id_col='CandidateEntityUrlId',
        vc='cosmos08/Outings',
        scopeparams='',
        input=master_attributes
    )
    createcosmospathfreely_func_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath='/local/EntityConflation/MasterLocationSimilarity.ss'
    )
    generalselectcosmos_func_0be9_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In2.GUID AS SourceEntityId, In2.SourceEntityDomain, In2.SourceEntityUrl, In1.EntityId AS CandidateEntityId, In1.EntityDomain AS CandidateEntityDomain, In1.EntityUrl AS CandidateEntityUrl FROM In2 INNER JOIN In1 ON In2.CandidateEntityUrlId== In1.CandidateEntityUrlId;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=outings_source_url_id_generator_func_289a_instance.outputs.output_ss_out,
        in2=outings_source_url_id_generator_func_6313_instance.outputs.output_ss_out
    )
    backup_file_2563_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterCandidatePairs.ss',
        sourcepath=generalselectcosmos_func_0be9_instance.outputs.outputstream_out
    )
    backup_file_4cc6_subgraph = backup_file_bdd9(
        backupdirectory='/local/EntityConflation/',
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='0',
        filename='MasterCandidatePairs.ss',
        sourcepath=backup_file_2563_subgraph.outputs.backuppath_out
    )
    pair_filters_step1_subgraph = pair_filters_step1_b265(
        location_similarity_threshold=location_similarity_threshold,
        name_similarity_threshold=name_similarity_threshold,
        conflation_date=conflation_date,
        pairs=backup_file_2563_subgraph.outputs.backuppath_out,
        attributes=master_attributes,
        namepairsim=namepairsim
    )
    generalselectcosmos_func_187e_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT *, DateTime.UtcNow.ToString() AS DateUpdated FROM In1',
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
        in1=pair_filters_step1_subgraph.outputs.outputstream_out
    )
    cross_join_subgraph = cross_join_d285(
        conflation_date=conflation_date,
        input=pair_filters_step1_subgraph.outputs.outputtsv_out
    )
    update_by_dateupdated_d716_subgraph = update_by_dateupdated_4cf1(
        datekey='SourceEntityId,CandidateEntityId',
        in1=generalselectcosmos_func_187e_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_b295_instance = generalselectcosmos_func(
        extractcols1='SourceEntityId: string, CandidateEntityId: string',
        extractcols2='SourceEntityId: string, SourceEntityDomain: string, SourceEntityUrl: string, CandidateEntityId: string, CandidateEntityDomain: string, CandidateEntityUrl: string',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT In1.SourceEntityId, In2.EntityDomain AS SourceEntityDomain, In2.EntityUrl AS SourceEntityUrl, CandidateEntityId FROM In2 INNER JOIN In1 ON In2.EntityId == In1.SourceEntityId;',
        select2='In1 = SELECT In1.SourceEntityId, SourceEntityDomain, SourceEntityUrl, CandidateEntityId, In2.EntityDomain AS CandidateEntityDomain, In2.EntityUrl AS CandidateEntityUrl FROM In2 INNER JOIN In1 ON In2.EntityId == In1.CandidateEntityId;',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId, CandidateEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=cross_join_subgraph.outputs.output_out,
        in2=master_attributes
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        sourcepath=update_by_dateupdated_d716_subgraph.outputs.filteredss_out,
        destinationpath=createcosmospathfreely_func_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_1f57_instance = generalselectcosmos_func(
        extractcols1='SourceEntityId: string, CandidateEntityId: string',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT *, DateTime.UtcNow.ToString() AS DateUpdated',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId, CandidateEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=generalselectcosmos_func_b295_instance.outputs.outputstream_out
    )
    backup_file_subgraph = backup_file_9ad6(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterLocationSimilarity.ss',
        sourcepath=cosmos_mirror_with_inputs_and_overwrite_func_instance.outputs.destinationpath_out
    )
    update_by_dateupdated_e932_subgraph = update_by_dateupdated_4cf1(
        datekey='SourceEntityId,CandidateEntityId',
        in1=generalselectcosmos_func_1f57_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_88ac_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId, CandidateEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=update_by_dateupdated_e932_subgraph.outputs.filteredss_out
    )
    pair_filters_w_top_10_updateonnamesim_subgraph = pair_filters_w_top_10_updateonnamesim_0ce0(
        location_similarity_threshold='10.0',
        name_similarity_threshold='4',
        conflation_date=conflation_date,
        pairs=update_by_dateupdated_e932_subgraph.outputs.filteredss_out,
        attributes=master_attributes
    )
    backup_file_8436_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterAllCandidatePairs.ss',
        sourcepath=generalselectcosmos_func_88ac_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_8f5b_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId, CandidateEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=pair_filters_w_top_10_updateonnamesim_subgraph.outputs.location_out
    )
    generalselectcosmos_func_424c_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId, CandidateEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=pair_filters_w_top_10_updateonnamesim_subgraph.outputs.masternamesimilarity_out
    )
    update_by_dateupdated_82ee_subgraph = update_by_dateupdated_4cf1(
        datekey='SourceEntityId,CandidateEntityId',
        in1=pair_filters_w_top_10_updateonnamesim_subgraph.outputs.top10pairfilter_out
    )
    backup_file_subgraph = backup_file_5fc1(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterLocationSimilarity.ss',
        sourcepath=generalselectcosmos_func_8f5b_instance.outputs.outputstream_out
    )
    backup_file_0456_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterNameSimilarity.ss',
        sourcepath=generalselectcosmos_func_424c_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_e601_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId, CandidateEntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=update_by_dateupdated_82ee_subgraph.outputs.filteredss_out
    )
    backup_file_5cf9_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterAllCandidatePairsFiltered.ss',
        sourcepath=generalselectcosmos_func_e601_instance.outputs.outputstream_out
    )
    return {'master_candidate_pairs_filtered_out': update_by_dateupdated_82ee_subgraph.outputs.filteredss_out, 'master_location_similarity_out': backup_file_subgraph.outputs.backuppath_out, 'master_name_similarity_out': backup_file_0456_subgraph.outputs.backuppath_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating candidate_pairs_pre_filtering_subgraph_a765")
    pipeline = candidate_pairs_pre_filtering_subgraph_a765()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='candidate_pairs_pre_filtering_subgraph_a765')
    print(datetime.now(), "Finish")
