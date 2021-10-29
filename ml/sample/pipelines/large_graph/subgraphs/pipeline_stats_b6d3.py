from datetime import datetime
from azure.ml.component import dsl
from format_qg_data_e7fe import format_qg_data_e7fe
from generate_html_report_37c3 import generate_html_report_37c3
from resources import entity_conflation_data_status_monitor_func, cosmospathcreator_rundate_func


print(datetime.now(), "Declaring pipeline: pipeline_stats_b6d3")
@dsl.pipeline(name='pipeline_stats_b6d3', default_compute_target='cpu-cluster')
def pipeline_stats_b6d3(
    merged_sim,
    master_attr,
    conflation_date=''
):
    cosmospathcreator_rundate_func_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/MasterAllCandidatePairsFiltered.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    entity_conflation_data_status_monitor_func_instance = entity_conflation_data_status_monitor_func(
        vc='cosmos08/Outings',
        scopeparams='',
        master_pairs=cosmospathcreator_rundate_func_instance.outputs.createdpath_out,
        master_attr=master_attr,
        merged_sim=merged_sim
    )
    generate_html_report_subgraph = generate_html_report_37c3(
        conflation_date=conflation_date,
        in1=entity_conflation_data_status_monitor_func_instance.outputs.stats_ecis_out,
        in1_2=entity_conflation_data_status_monitor_func_instance.outputs.stats_ecis_dm_out
    )
    format_qg_data_subgraph = format_qg_data_e7fe(
        conflation_date=conflation_date,
        in1=entity_conflation_data_status_monitor_func_instance.outputs.stats_ecis_dm_out,
        in1_2=entity_conflation_data_status_monitor_func_instance.outputs.stats_ecis_out
    )
    return {'qg_data_out': format_qg_data_subgraph.outputs.output_out, 'htmlreport_out': generate_html_report_subgraph.outputs.output_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating pipeline_stats_b6d3")
    pipeline = pipeline_stats_b6d3()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='pipeline_stats_b6d3')
    print(datetime.now(), "Finish")
