from datetime import datetime
from azure.ml.component import dsl
from backup_file_bdd9 import backup_file_bdd9
from update_by_dateupdated_4cf1 import update_by_dateupdated_4cf1
from topics_and_entity_type_extraction_subgraph_b0d9 import topics_and_entity_type_extraction_subgraph_b0d9
from named_entity_relationship_generation_subgraph_65f2 import named_entity_relationship_generation_subgraph_65f2
from resources import generalselectcosmos_func, createcosmospathfreely_func, createcosmospathfreely_func, cosmospathcreator_rundate_func, attractions_ground_truth_candidates_attributes_generator_func, attractions_ground_truth_candidates_attributes_generator_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: attribute_generation_sub_graph_9848")
@dsl.pipeline(name='attribute_generation_sub_graph_9848', default_compute_target='cpu-cluster')
def attribute_generation_sub_graph_9848(
    master_records,
    ground_truth_domain2_candidates,
    ground_truth_domain1_candidates,
    ground_truth_domain1='',
    ground_truth_domain2='',
    ground_truth_domain3='',
    conflation_date=''
):
    createcosmospathfreely_func_71e4_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath='/local/EntityConflation/MasterAttributes.ss'
    )
    generalselectcosmos_func_cc96_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SourceEntities1 = SELECT In2.GUID AS EntityId, In2.SourceEntityName AS EntityName, In1.Domain AS EntityDomain, In1.SourceUrl AS EntityUrl,  Description, LocationLatitude AS EntityLatitude, LocationLongitude AS EntityLongitude, LocationCity AS Locality, LocationCounty AS Area, LocationState AS Region, LocationCountry AS Country, LocationPostalCode AS PostalCode, LocationStreetAddress AS StreetAddress, Website, PhoneNumber, Topics, EntityType FROM In2 INNER JOIN In1 ON In1.StoryId == In2.GUID;',
        select2='SourceEntities2 = SELECT In3.GUID AS EntityId, In3.SourceEntityName AS EntityName, In1.Domain AS EntityDomain, In1.SourceUrl AS EntityUrl, Description, LocationLatitude AS EntityLatitude, LocationLongitude AS EntityLongitude, LocationCity AS Locality, LocationCounty AS Area, LocationState AS Region, LocationCountry AS Country, LocationPostalCode AS PostalCode, LocationStreetAddress AS StreetAddress, Website, PhoneNumber, Topics, EntityType  FROM In3 INNER JOIN In1 ON In1.StoryId == In3.GUID;',
        select3='SELECT * FROM SourceEntities1 UNION DISTINCT SELECT * FROM SourceEntities2;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY EntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=master_records,
        in2=ground_truth_domain1_candidates,
        in3=ground_truth_domain2_candidates
    )
    cosmospathcreator_rundate_func_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/GroundTruthFeeds/%s.ss""" % (ground_truth_domain2),
        vc='vc://cosmos08/Outings',
        rundate="""%s""" % (conflation_date)
    )
    createcosmospathfreely_func_4bcf_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/GroundTruthFeeds/%s.ss""" % (ground_truth_domain1)
    )
    generalselectcosmos_func_f472_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT *, "" AS Tags FROM In1',
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
        in1=cosmospathcreator_rundate_func_instance.outputs.createdpath_out
    )
    attractions_ground_truth_candidates_attributes_generator_func_130f_instance = attractions_ground_truth_candidates_attributes_generator_func(
        ground_truth_domain=ground_truth_domain1,
        vc='cosmos08/Outings',
        ground_truth_stream=createcosmospathfreely_func_4bcf_instance.outputs.createdpath_out,
        master_candidates_output_stream=ground_truth_domain1_candidates
    )
    attractions_ground_truth_candidates_attributes_generator_func_b48f_instance = attractions_ground_truth_candidates_attributes_generator_func(
        ground_truth_domain=ground_truth_domain2,
        vc='cosmos08/Outings',
        ground_truth_stream=generalselectcosmos_func_f472_instance.outputs.outputstream_out,
        master_candidates_output_stream=ground_truth_domain2_candidates
    )
    generalselectcosmos_func_e5b6_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY EntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=attractions_ground_truth_candidates_attributes_generator_func_130f_instance.outputs.ground_truth_candidates_attributes_stream_out,
        in2=attractions_ground_truth_candidates_attributes_generator_func_b48f_instance.outputs.ground_truth_candidates_attributes_stream_out
    )
    topics_and_entity_type_extraction_subgraph_subgraph = topics_and_entity_type_extraction_subgraph_b0d9(
        ground_truth_domains_merged_attributes=generalselectcosmos_func_e5b6_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_bc62_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT DISTINCT * FROM In1 UNION DISTINCT SELECT DISTINCT * FROM In2;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY EntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_cc96_instance.outputs.outputstream_out,
        in2=topics_and_entity_type_extraction_subgraph_subgraph.outputs.outputstream_out
    )
    named_entity_relationship_generation_subgraph_subgraph = named_entity_relationship_generation_subgraph_65f2(
        conflation_date="""%s""" % (conflation_date),
        master_attributes=generalselectcosmos_func_bc62_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_fea2_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='MergedJson = SELECT In1.*, In2.NERJson FROM In1 FULL JOIN In2 ON In1.EntityId == In2.EntityId;',
        select2='SELECT *, DateTime.UtcNow.ToString() AS DateUpdated FROM MergedJson UNION DISTINCT SELECT * FROM In3;',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY EntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 20',
        in1=generalselectcosmos_func_bc62_instance.outputs.outputstream_out,
        in2=named_entity_relationship_generation_subgraph_subgraph.outputs.master_ner_json_table_out,
        in3=createcosmospathfreely_func_71e4_instance.outputs.createdpath_out
    )
    update_by_dateupdated_subgraph = update_by_dateupdated_4cf1(
        datekey='EntityId',
        in1=generalselectcosmos_func_fea2_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_6232_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY EntityId;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 20',
        in1=update_by_dateupdated_subgraph.outputs.filteredss_out
    )
    backup_file_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='MasterAttributes.ss',
        sourcepath=generalselectcosmos_func_6232_instance.outputs.outputstream_out
    )
    return {'master_attributes_out': update_by_dateupdated_subgraph.outputs.filteredss_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating attribute_generation_sub_graph_9848")
    pipeline = attribute_generation_sub_graph_9848()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='attribute_generation_sub_graph_9848')
    print(datetime.now(), "Finish")
