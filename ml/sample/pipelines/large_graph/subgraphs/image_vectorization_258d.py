from datetime import datetime
from azure.ml.component import dsl
from image_vector_generation_sub_graph_50b0 import image_vector_generation_sub_graph_50b0
from resources import cosmos_mirror_with_inputs_and_overwrite_func, generalselectcosmos_func, createcosmospathfreely_func, top_reducer_ss_func, generalselectcosmos_func, generalselectcosmos_func, createcosmospathfreely_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: image_vectorization_258d")
@dsl.pipeline(name='image_vectorization_258d', default_compute_target='cpu-cluster')
def image_vectorization_258d(
    recordimages,
    attributes,
    groundtruthimages,
    number_of_images_to_compare=''
):
    createcosmospathfreely_func_0120_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath='/local/EntityConflation/MasterImageVectors.ss'
    )
    generalselectcosmos_func_dc48_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SourceEntities = SELECT EntityId, ImageUrl, Base64, BWScore, AttractiveNessScore FROM In1 INNER JOIN In2 ON In1.EntityId == In2.Id',
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
        scopeparams='-tokens 75',
        in1=attributes,
        in2=recordimages
    )
    createcosmospathfreely_func_6355_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath='/local/EntityConflation/MasterImageVectors.ss'
    )
    generalselectcosmos_func_1c7b_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In2 = SELECT *, DateTime.UtcNow.ToString() AS DateUpdated FROM In2 ',
        select2='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2;',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        in2=generalselectcosmos_func_dc48_instance.outputs.outputstream_out,
        in1=groundtruthimages
    )
    top_reducer_ss_func_instance = top_reducer_ss_func(
        sortcol='AttractiveNessScore',
        sortdir='DESC',
        reducecol='EntityId',
        numtokeep=number_of_images_to_compare,
        vc='vc://cosmos08/Outings',
        input=generalselectcosmos_func_1c7b_instance.outputs.outputstream_out
    )
    image_vector_generation_sub_graph_subgraph = image_vector_generation_sub_graph_50b0(
        downloaded_images=top_reducer_ss_func_instance.outputs.output_out,
        master_image_vectors=createcosmospathfreely_func_0120_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_25cd_instance = generalselectcosmos_func(
        extractcols1='ImageUrl:string, Vec:string',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY ImageUrl;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=image_vector_generation_sub_graph_subgraph.outputs.outputfeaturefiletsv_out,
        in2=createcosmospathfreely_func_0120_instance.outputs.createdpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_25cd_instance.outputs.outputstream_out,
        destinationpath=createcosmospathfreely_func_6355_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_28f7_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.EntityId, In1.ImageUrl, In2.Vec FROM In1 INNER JOIN In2 ON In1.ImageUrl == In2.ImageUrl;',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY ImageUrl;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=top_reducer_ss_func_instance.outputs.output_out,
        in2=generalselectcosmos_func_25cd_instance.outputs.outputstream_out
    )
    return {'masterimagevectors_out': cosmos_mirror_with_inputs_and_overwrite_func_instance.outputs.destinationpath_out, 'imageidvectors_out': generalselectcosmos_func_28f7_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating image_vectorization_258d")
    pipeline = image_vectorization_258d()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='image_vectorization_258d')
    print(datetime.now(), "Finish")
