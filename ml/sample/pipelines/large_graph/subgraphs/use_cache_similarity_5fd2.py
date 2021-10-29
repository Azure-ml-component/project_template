from datetime import datetime
from azure.ml.component import dsl
from resources import cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func, cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: use_cache_similarity_5fd2")
@dsl.pipeline(name='use_cache_similarity_5fd2', default_compute_target='cpu-cluster')
def use_cache_similarity_5fd2(
    currpairsfiltered,
    currattributes,
    conflationdate='',
    attributecol='',
    similaritycols=''
):
    cosmospathcreator_rundate_func_41e0_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/MasterMergedAllSimilarity.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflationdate
    )
    generalselectcosmos_func_15a1_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId,CandidateEntityId ',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Cluster',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=currpairsfiltered
    )
    cosmospathcreator_rundate_func_37d5_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/MasterAttributes.ss',
        vc='vc://cosmos08/Outings',
        rundate="""%s""" % (conflationdate)
    )
    generalselectcosmos_func_3851_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SELECT EntityId, %s FROM In1 INNER JOIN In2 ON In1.EntityId == In2.EntityId AND In1.%s == In2.%s """ % (attributecol, attributecol, attributecol),
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
        scopeparams='-tokens 25',
        in1=cosmospathcreator_rundate_func_37d5_instance.outputs.createdpath_out,
        in2=currattributes
    )
    generalselectcosmos_func_2f69_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In2 = SELECT In2.*, S1.%s AS SourceEntity%s, S2.%s AS CandidateEntity%s FROM In2 INNER JOIN In1 AS S1 ON In2.SourceEntityId == S1.EntityId INNER JOIN In1 AS S2 ON In2.CandidateEntityId == S2.EntityId;""" % (attributecol, attributecol, attributecol, attributecol),
        select2="""SELECT %s FROM In2""" % (similaritycols),
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId,CandidateEntityId ',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=generalselectcosmos_func_3851_instance.outputs.outputstream_out,
        in2=cosmospathcreator_rundate_func_41e0_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_f18b_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In2.* FROM In2 LEFT JOIN In1 ON In1.SourceEntityId == In2.SourceEntityId AND In1.CandidateEntityId==In2.CandidateEntityId WHERE String.IsNullOrEmpty(In1.CandidateEntityId)',
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
        scopeparams='-tokens 25',
        in1=generalselectcosmos_func_2f69_instance.outputs.outputstream_out,
        in2=generalselectcosmos_func_15a1_instance.outputs.outputstream_out
    )
    return {'similarities_out': generalselectcosmos_func_2f69_instance.outputs.outputstream_out, 'newpairsfiltered_out': generalselectcosmos_func_f18b_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating use_cache_similarity_5fd2")
    pipeline = use_cache_similarity_5fd2()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='use_cache_similarity_5fd2')
    print(datetime.now(), "Finish")
