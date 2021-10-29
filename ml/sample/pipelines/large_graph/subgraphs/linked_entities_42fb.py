from datetime import datetime
from azure.ml.component import dsl
from backup_file_bdd9 import backup_file_bdd9
from resources import generalselectcosmos_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func, cosmospathcreator_rundate_func


print(datetime.now(), "Declaring pipeline: linked_entities_42fb")
@dsl.pipeline(name='linked_entities_42fb', default_compute_target='cpu-cluster')
def linked_entities_42fb(
    triples_ss,
    conflation_date='',
    conflation_month=''
):
    cosmospathcreator_rundate_func_d5e4_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/GroundTruthFeeds/Mappings/SatoriData.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_8b0f_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/GroundTruthFeeds/www.tripadvisor.com.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_3e5c_instance = cosmospathcreator_rundate_func(
        relativepath='/local/users/jepatel/StoryIdGUID.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    generalselectcosmos_func_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT Record AS StoryId, TAId, WikiUrl AS WikiLink, SatoriId AS EntityId FROM In1',
        select2='In1 = SELECT In1.*, In3.Url AS TALink FROM In1 LEFT JOIN In3 ON In1.TAId == In3.Id;',
        select3='SELECT In1.*, EntityName, StaticRank, EntityLatitude.ToString() AS EntityLatitude, EntityLongitude.ToString() AS EntityLongitude, Address FROM In1 LEFT JOIN In2 ON In1.EntityId == In2.EntityId;',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Merge SatoriData',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in2=cosmospathcreator_rundate_func_d5e4_instance.outputs.createdpath_out,
        in3=cosmospathcreator_rundate_func_8b0f_instance.outputs.createdpath_out,
        in1=triples_ss
    )
    backup_file_subgraph = backup_file_bdd9(
        backupdirectory="""/local/EntityConflation/Backups/%s/""" % (conflation_date),
        conflation_date=conflation_date,
        vc='vc://cosmos08/Outings',
        backupexp='90',
        filename='LinkedEntities.ss',
        sourcepath=generalselectcosmos_func_instance.outputs.outputstream_out
    )
    return {'linkedentities_ss_out': backup_file_subgraph.outputs.backuppath_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating linked_entities_42fb")
    pipeline = linked_entities_42fb()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='linked_entities_42fb')
    print(datetime.now(), "Finish")
