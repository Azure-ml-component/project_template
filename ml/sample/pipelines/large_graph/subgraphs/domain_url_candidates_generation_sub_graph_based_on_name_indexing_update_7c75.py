from datetime import datetime
from azure.ml.component import dsl
from update_by_dateupdated_4cf1 import update_by_dateupdated_4cf1
from candidatepairgenerationfromgroundtruthfeed2_4bed import candidatepairgenerationfromgroundtruthfeed2_4bed
from backup_file_bdd9 import backup_file_bdd9
from resources import cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75")
@dsl.pipeline(name='domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75', default_compute_target='cpu-cluster')
def domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75(
    enhanced,
    webrecords,
    ground_truth_domain1='',
    ground_truth_domain2='',
    conflation_date=''
):
    cosmospathcreator_rundate_func_8ef9_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/GroundTruthFeeds/%s.ss""" % (ground_truth_domain2),
        vc='vc://cosmos08/Outings',
        rundate="""%s""" % (conflation_date)
    )
    cosmospathcreator_rundate_func_341d_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/GroundTruthFeeds/%s.ss""" % (ground_truth_domain1),
        vc='vc://cosmos08/Outings',
        rundate="""%s""" % (conflation_date)
    )
    generalselectcosmos_func_3ccf_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1 WHERE !String.IsNullOrEmpty(EntityName) AND !String.IsNullOrEmpty(Latitude) AND !String.IsNullOrEmpty(Longitude)',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Filter by EntityName, Lat and Lng',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmospathcreator_rundate_func_8ef9_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_6504_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT *  FROM In1 WHERE !String.IsNullOrEmpty(EntityName) AND !String.IsNullOrEmpty(Latitude) AND !String.IsNullOrEmpty(Longitude)',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Filter by EntityName, Lat and Lng',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmospathcreator_rundate_func_341d_instance.outputs.createdpath_out
    )
    candidatepairgenerationfromgroundtruthfeed2_22b6_subgraph = candidatepairgenerationfromgroundtruthfeed2_4bed(
        ground_truth_domain=ground_truth_domain2,
        conflation_date=conflation_date,
        groundtruthfeed=generalselectcosmos_func_3ccf_instance.outputs.outputstream_out,
        webrecords=webrecords
    )
    candidatepairgenerationfromgroundtruthfeed2_b3fc_subgraph = candidatepairgenerationfromgroundtruthfeed2_4bed(
        ground_truth_domain=ground_truth_domain1,
        conflation_date=conflation_date,
        groundtruthfeed=generalselectcosmos_func_6504_instance.outputs.outputstream_out,
        webrecords=webrecords
    )
    generalselectcosmos_func_1dc6_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='GroundTruthEntities1 = SELECT In2.GUID, In2.SourceEntityName, In1.Domain AS SourceEntityDomain, In1.SourceUrl AS SourceEntityUrl, In2.CandidateEntityDomain, In2.CandidateEntityUrl, In2.DateUpdated FROM In2 INNER JOIN In1 ON In1.StoryId == In2.GUID;',
        select2='GroundTruthEntities2 = SELECT In3.GUID, In3.SourceEntityName, In1.Domain AS SourceEntityDomain, In1.SourceUrl AS SourceEntityUrl, In3.CandidateEntityDomain, In3.CandidateEntityUrl, In3.DateUpdated FROM In3 INNER JOIN In1 ON In1.StoryId == In3.GUID;',
        select3='SELECT * FROM GroundTruthEntities1 UNION DISTINCT SELECT * FROM GroundTruthEntities2;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID, SourceEntityUrl;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in2=candidatepairgenerationfromgroundtruthfeed2_b3fc_subgraph.outputs.destinationpath_out,
        in3=candidatepairgenerationfromgroundtruthfeed2_22b6_subgraph.outputs.destinationpath_out,
        in1=enhanced
    )
    generalselectcosmos_func_b4bd_instance = generalselectcosmos_func(
        extractcols1='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols3=';',
        extractcols4=';',
        select1='In1 = SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2;',
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
        in1=candidatepairgenerationfromgroundtruthfeed2_b3fc_subgraph.outputs.namepairsim_out,
        in2=candidatepairgenerationfromgroundtruthfeed2_22b6_subgraph.outputs.namepairsim_out
    )
    update_by_dateupdated_subgraph = update_by_dateupdated_4cf1(
        datekey='GUID,CandidateEntityUrl',
        in1=generalselectcosmos_func_1dc6_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_c54b_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID, SourceEntityUrl;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=update_by_dateupdated_subgraph.outputs.filteredss_out
    )
    backup_file_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterCandidateUrls.ss',
        sourcepath=generalselectcosmos_func_c54b_instance.outputs.outputstream_out
    )
    return {'candidatepairsingroundtruthdomain1_out': candidatepairgenerationfromgroundtruthfeed2_b3fc_subgraph.outputs.destinationpath_out, 'candidatepairsingroundtruthdomain2_out': candidatepairgenerationfromgroundtruthfeed2_22b6_subgraph.outputs.destinationpath_out, 'filteredss_out': update_by_dateupdated_subgraph.outputs.filteredss_out, 'namepairsimilarity_out': generalselectcosmos_func_b4bd_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75")
    pipeline = domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='domain_url_candidates_generation_sub_graph_based_on_name_indexing_update_7c75')
    print(datetime.now(), "Finish")
