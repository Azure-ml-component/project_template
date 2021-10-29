from datetime import datetime
from azure.ml.component import dsl
from publishing_stats_8ad9 import publishing_stats_8ad9
from email_summary_ee53 import email_summary_ee53
from pipeline_stats_b6d3 import pipeline_stats_b6d3
from backup_file_bdd9 import backup_file_bdd9
from ta_sid_mapping_bvt_a67c import ta_sid_mapping_bvt_a67c
from set_up_email_06da import set_up_email_06da
from guid_ta_wiki_sid_2392 import guid_ta_wiki_sid_2392
from resources import top_reducer_ss_func, generalselectcosmos_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, scope_basics_union_intersect_except_sstream_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, aetheremailmodule_func, aetheremailmodule_func


print(datetime.now(), "Declaring pipeline: run_quality_gates_6dbe")
@dsl.pipeline(name='run_quality_gates_6dbe', default_compute_target='cpu-cluster')
def run_quality_gates_6dbe(
    merged_sim,
    ta_satori_links,
    master_attr,
    record_triples,
    conflation_date='',
    recipients=''
):
    pipeline_stats_subgraph = pipeline_stats_b6d3(
        conflation_date=conflation_date,
        master_attr=master_attr,
        merged_sim=merged_sim
    )
    cosmospathcreator_rundate_func_359c_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/Resources/QualityGateConfig.txt',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    guid_ta_wiki_sid_subgraph = guid_ta_wiki_sid_2392(
        conflation_date=conflation_date,
        recordtriples=record_triples,
        master_attribute=master_attr
    )
    publishing_stats_subgraph = publishing_stats_8ad9(
        conflation_date=conflation_date,
        record_triples=record_triples,
        ta_satori_links=ta_satori_links,
        master_attr=master_attr
    )
    cosmospathcreator_rundate_func_f8dd_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/Resources/ConflationStats.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    ta_sid_mapping_bvt_subgraph = ta_sid_mapping_bvt_a67c(
        conflation_date=conflation_date,
        ta_sid_mapping=ta_satori_links
    )
    backup_file_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/Stats/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='ConflationStats.ss',
        sourcepath=cosmospathcreator_rundate_func_f8dd_instance.outputs.createdpath_out
    )
    scope_basics_union_intersect_except_sstream_func_instance = scope_basics_union_intersect_except_sstream_func(
        uniontype='UNION ALL',
        clusteredbycolumns='RunDate',
        sortedbycolumns='RunDate,StatName',
        vc='cosmos08/Outings',
        scopeparams='',
        first=publishing_stats_subgraph.outputs.qg_data_out,
        second=guid_ta_wiki_sid_subgraph.outputs.qg_data_out,
        third=ta_sid_mapping_bvt_subgraph.outputs.qg_data_out
    )
    email_summary_subgraph = email_summary_ee53(
        recipients=recipients,
        conflation_date=conflation_date,
        input_1=publishing_stats_subgraph.outputs.htmlreport_out,
        input_2_3=guid_ta_wiki_sid_subgraph.outputs.htmlreport_out,
        input_2_2=ta_sid_mapping_bvt_subgraph.outputs.htmlreport_out,
        input_2=pipeline_stats_subgraph.outputs.htmlreport_out
    )
    generalselectcosmos_func_7106_instance = generalselectcosmos_func(
        extractcols1='RunDate:DateTime, Description:string, StatName:string, Type:string, Value:float',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='convert to ss',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=backup_file_subgraph.outputs.backuppath_out
    )
    top_reducer_ss_func_instance = top_reducer_ss_func(
        sortcol='RunDate',
        sortdir='DESC',
        reducecol='StatName',
        numtokeep='1',
        vc='vc://cosmos08/Outings',
        input=generalselectcosmos_func_7106_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_1a0d_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In2 = SELECT In1.StatName, In1.Type, In1.RunDate AS LastRun, In2.RunDate AS CurrentRun, In1.Value AS LastValue, In2.Value AS CurrentValue, 100.0*(In2.Value-In1.Value)/In1.Value AS Change FROM In1 INNER JOIN In2 ON In1.StatName == In2.StatName',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Get Data to Compare',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=top_reducer_ss_func_instance.outputs.output_out,
        in2=scope_basics_union_intersect_except_sstream_func_instance.outputs.outputss_out
    )
    generalselectcosmos_func_97ea_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='Type:string, AlertNegThreshold:float, AlertPosThreshold:float, FailNegThreshold:float, FailPosThreshold:float',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.*, AlertNegThreshold, AlertPosThreshold, FailNegThreshold, FailPosThreshold FROM In1 INNER JOIN In2 ON In1.Type == In2.Type',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Get thresholds',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_1a0d_instance.outputs.outputstream_out,
        in2=cosmospathcreator_rundate_func_359c_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_c88f_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='Type:string, AlertNegThreshold:float, AlertPosThreshold:float, FailNegThreshold:float, FailPosThreshold:float',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1 WHERE (Change < AlertNegThreshold OR Change > AlertPosThreshold) AND !(Change < FailNegThreshold OR Change > FailPosThreshold)',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Get alerts',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_97ea_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_ee07_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='Type:string, AlertNegThreshold:float, AlertPosThreshold:float, FailNegThreshold:float, FailPosThreshold:float',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1 WHERE Change < FailNegThreshold OR Change > FailPosThreshold',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Get failures',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_97ea_instance.outputs.outputstream_out
    )
    set_up_email_917d_subgraph = set_up_email_06da(
        input=generalselectcosmos_func_c88f_instance.outputs.outputstream_out,
        path=generalselectcosmos_func_c88f_instance.outputs.outputtsv_out
    )
    set_up_email_5803_subgraph = set_up_email_06da(
        input=generalselectcosmos_func_ee07_instance.outputs.outputstream_out,
        path=generalselectcosmos_func_ee07_instance.outputs.outputtsv_out
    )
    aetheremailmodule_func_4912_instance = aetheremailmodule_func(
        recipients=recipients,
        subject='[SEV 3] [ALERT] Entity Conflation Quality Gate',
        body=set_up_email_917d_subgraph.outputs.htmlreport_out
    )
    aetheremailmodule_func_7311_instance = aetheremailmodule_func(
        recipients=recipients,
        subject='[SEV 2] [FAILURE] Entity Conflation Quality Gate',
        body=set_up_email_5803_subgraph.outputs.htmlreport_out
    )
    return {'historicalstats_out': generalselectcosmos_func_7106_instance.outputs.outputstream_out, 'runstats_out': scope_basics_union_intersect_except_sstream_func_instance.outputs.outputss_out, 'passing_out': set_up_email_5803_subgraph.outputs.control_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating run_quality_gates_6dbe")
    pipeline = run_quality_gates_6dbe()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='run_quality_gates_6dbe')
    print(datetime.now(), "Finish")
