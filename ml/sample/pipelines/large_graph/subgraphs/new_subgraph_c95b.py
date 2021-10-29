from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: new_subgraph_c95b")
@dsl.pipeline(name='new_subgraph_c95b', default_compute_target='cpu-cluster')
def new_subgraph_c95b(
    in1,
    in2
):
    generalselectcosmos_func_36ed_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='ImageUrl:string, Vec:string',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT DISTINCT * FROM In1',
        select2='SELECT In1.*, In2.Vec AS Vec1 FROM In1 LEFT JOIN In2 ON In1.SourceEntityPhotoUrl == In2.ImageUrl AND In1.SourceEntityId == In2.EntityId',
        select3='SELECT DISTINCT *',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId,CandidateEntityId INTO 100',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 35',
        in1=in1,
        in2=in2
    )
    generalselectcosmos_func_7dba_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='ImageUrl:string, Vec:string',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.*, In2.Vec AS Vec2 FROM In1 LEFT JOIN In2 ON In1.CandidateEntityPhotoUrl == In2.ImageUrl AND In1.CandidateEntityId == In2.EntityId',
        select2='SELECT DISTINCT *',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY SourceEntityId,CandidateEntityId INTO 100',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 35',
        in1=generalselectcosmos_func_36ed_instance.outputs.outputstream_out,
        in2=in2
    )
    return {'outputstream_out': generalselectcosmos_func_7dba_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating new_subgraph_c95b")
    pipeline = new_subgraph_c95b()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='new_subgraph_c95b')
    print(datetime.now(), "Finish")
