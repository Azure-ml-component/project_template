from datetime import datetime
from azure.ml.component import dsl
from resources import cosmospathcreator_rundate_func, generalselectcosmos_func, outings_get_xpath_value_func, generalselectcosmos_func, generalselectcosmos_func, cosmospathcreator_rundate_func, generalselectcosmos_func, cosmospathcreator_rundate_func


print(datetime.now(), "Declaring pipeline: record_image_data_generation_d333")
@dsl.pipeline(name='record_image_data_generation_d333', default_compute_target='cpu-cluster')
def record_image_data_generation_d333(
    conflation_date='@@Conflation_Date@@'
):
    cosmospathcreator_rundate_func_5132_instance = cosmospathcreator_rundate_func(
        relativepath='/local/AttractionsPipeline/Tables/MasterPhotosScores.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_004d_instance = cosmospathcreator_rundate_func(
        relativepath='/local/AttractionsPipeline/Tables/MasterPhotosDownloaded.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_0693_instance = cosmospathcreator_rundate_func(
        relativepath='/local/AttractionsPipeline/MasterRecords.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    generalselectcosmos_func_b074_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SourceEntities = SELECT In1.ImageUrl, Base64, BWScore, AttractiveNessScore FROM In1 INNER JOIN In2 ON In1.ImageUrl == In2.ImageUrl ',
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
        scopeparams='-tokens 100',
        in1=cosmospathcreator_rundate_func_004d_instance.outputs.createdpath_out,
        in2=cosmospathcreator_rundate_func_5132_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_69ee_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT StoryId, Photos',
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
        in1=cosmospathcreator_rundate_func_0693_instance.outputs.createdpath_out
    )
    outings_get_xpath_value_func_instance = outings_get_xpath_value_func(
        output_col='PhotoList',
        xml_column='Photos',
        xpath='/ArrayOfImage/Image/ImageUrl',
        vc='cosmos08/Outings',
        scopeparams='',
        input_stream=generalselectcosmos_func_69ee_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_bb08_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT StoryId AS Id, PhotoList AS ImageUrl',
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
        in1=outings_get_xpath_value_func_instance.outputs.output_stream_out
    )
    generalselectcosmos_func_5bdc_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SourceEntities = SELECT In1.Id, In2.* FROM In1 INNER JOIN In2 ON In1.ImageUrl == In2.ImageUrl',
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
        scopeparams='-tokens 100',
        in1=generalselectcosmos_func_bb08_instance.outputs.outputstream_out,
        in2=generalselectcosmos_func_b074_instance.outputs.outputstream_out
    )
    return {'recordimagedata_out': generalselectcosmos_func_5bdc_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating record_image_data_generation_d333")
    pipeline = record_image_data_generation_d333()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='record_image_data_generation_d333')
    print(datetime.now(), "Finish")
