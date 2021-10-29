from datetime import datetime
from azure.ml.component import dsl
from backup_file_bdd9 import backup_file_bdd9
from resources import cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, outings_ta_sid_mapping_generator_func


print(datetime.now(), "Declaring pipeline: generate_triples_data_and_ta_sid_mapping_dfe7")
@dsl.pipeline(name='generate_triples_data_and_ta_sid_mapping_dfe7', default_compute_target='cpu-cluster')
def generate_triples_data_and_ta_sid_mapping_dfe7(
    triples_ss,
    conflation_date='',
    conflation_month=''
):
    cosmospathcreator_rundate_func_512a_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/GroundTruthFeeds/Mappings/TripAdvisorGTMap.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_1fba_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/GroundTruthFeeds/Mappings/WikipediaGTMap.ss',
        vc='vc://cosmos08/Outings',
        rundate="""%s0""" % (conflation_date)
    )
    cosmospathcreator_rundate_func_34e5_instance = cosmospathcreator_rundate_func(
        relativepath='/shares/ldp-storage/TripAdvisorAttractions/2020/11/all-ALL-SSTripAdvisorAttractions_2020_11_15_17.1.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_43be_instance = cosmospathcreator_rundate_func(
        relativepath='/local/AttractionsPipeline/Tables/AllTrails.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    outings_ta_sid_mapping_generator_func_instance = outings_ta_sid_mapping_generator_func(
        vc='cosmos08/Outings',
        all_trails_feed=cosmospathcreator_rundate_func_43be_instance.outputs.createdpath_out,
        ta_satori_map=cosmospathcreator_rundate_func_512a_instance.outputs.createdpath_out,
        wiki_satori_map=cosmospathcreator_rundate_func_1fba_instance.outputs.createdpath_out,
        triples_ss=triples_ss
    )
    backup_file_cb85_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='RecordSidTriples.ss',
        sourcepath=outings_ta_sid_mapping_generator_func_instance.outputs.record_ta_sid_triples_out
    )
    backup_file_706b_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='TripAdvisorSatoriMapping.General.ss',
        sourcepath=outings_ta_sid_mapping_generator_func_instance.outputs.ta_sid_mapping_out
    )
    return {'record_ta_sid_triples_out': outings_ta_sid_mapping_generator_func_instance.outputs.record_ta_sid_triples_out, 'ta_sid_mapping_out': outings_ta_sid_mapping_generator_func_instance.outputs.ta_sid_mapping_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating generate_triples_data_and_ta_sid_mapping_dfe7")
    pipeline = generate_triples_data_and_ta_sid_mapping_dfe7()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='generate_triples_data_and_ta_sid_mapping_dfe7')
    print(datetime.now(), "Finish")
