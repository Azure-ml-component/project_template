from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, cosmos_split_1_tsv_to_10_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, landmark_datacollection_utils_rmacextractor_outings_vc_func, landmark_datacollection_utils_rmacextractor_outings_vc_func


print(datetime.now(), "Declaring pipeline: image_vector_generation_sub_graph_50b0")
@dsl.pipeline(name='image_vector_generation_sub_graph_50b0', default_compute_target='cpu-cluster')
def image_vector_generation_sub_graph_50b0(
    master_image_vectors,
    downloaded_images
):
    generalselectcosmos_func_1291_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='FilteredImageUrls = SELECT ImageUrl FROM In1 EXCEPT SELECT ImageUrl FROM In2;',
        select2='SELECT ImageUrl, Base64 FROM In1 INNER JOIN FilteredImageUrls ON In1.ImageUrl == FilteredImageUrls.ImageUrl WHERE !String.IsNullOrEmpty(Base64) AND !String.IsNullOrEmpty(ImageUrl) && Base64.Length % 4 == 0;',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 20',
        in1=downloaded_images,
        in2=master_image_vectors
    )
    cosmos_split_1_tsv_to_10_func_instance = cosmos_split_1_tsv_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputfile=generalselectcosmos_func_1291_instance.outputs.outputtsv_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_63cd_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part0_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_ffce_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part1_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_b0b8_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part2_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_68fc_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part3_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_1879_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part4_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_a0a1_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part5_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_34df_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part6_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_56ef_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part7_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_2d69_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part8_out
    )
    landmark_datacollection_utils_rmacextractor_outings_vc_func_bc9b_instance = landmark_datacollection_utils_rmacextractor_outings_vc_func(
        vc='cosmos08/Outings',
        scopeparams='-tokens 75',
        inputimagebinaryfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part9_out
    )
    generalselectcosmos_func_9ddb_instance = generalselectcosmos_func(
        extractcols1='ImageUrl:string, Vec:string',
        extractcols2='ImageUrl:string, Vec:string',
        extractcols3='ImageUrl:string, Vec:string',
        extractcols4='ImageUrl:string, Vec:string',
        select1='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
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
        scopeparams='-tokens 20',
        in1=landmark_datacollection_utils_rmacextractor_outings_vc_func_63cd_instance.outputs.outputfeaturefiletsv_out,
        in2=landmark_datacollection_utils_rmacextractor_outings_vc_func_ffce_instance.outputs.outputfeaturefiletsv_out,
        in3=landmark_datacollection_utils_rmacextractor_outings_vc_func_b0b8_instance.outputs.outputfeaturefiletsv_out,
        in4=landmark_datacollection_utils_rmacextractor_outings_vc_func_68fc_instance.outputs.outputfeaturefiletsv_out
    )
    generalselectcosmos_func_ad55_instance = generalselectcosmos_func(
        extractcols1='ImageUrl:string, Vec:string',
        extractcols2='ImageUrl:string, Vec:string',
        extractcols3='ImageUrl:string, Vec:string',
        extractcols4='ImageUrl:string, Vec:string',
        select1='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
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
        scopeparams='-tokens 20',
        in1=landmark_datacollection_utils_rmacextractor_outings_vc_func_1879_instance.outputs.outputfeaturefiletsv_out,
        in2=landmark_datacollection_utils_rmacextractor_outings_vc_func_a0a1_instance.outputs.outputfeaturefiletsv_out,
        in3=landmark_datacollection_utils_rmacextractor_outings_vc_func_34df_instance.outputs.outputfeaturefiletsv_out,
        in4=landmark_datacollection_utils_rmacextractor_outings_vc_func_56ef_instance.outputs.outputfeaturefiletsv_out
    )
    generalselectcosmos_func_6228_instance = generalselectcosmos_func(
        extractcols1='ImageUrl:string, Vec:string',
        extractcols2='ImageUrl:string, Vec:string',
        extractcols3='ImageUrl:string, Vec:string',
        extractcols4='Id:string, Vec:string',
        select1='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
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
        scopeparams='-tokens 20',
        in1=generalselectcosmos_func_9ddb_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_ad55_instance.outputs.outputtsv_out,
        in3=landmark_datacollection_utils_rmacextractor_outings_vc_func_2d69_instance.outputs.outputfeaturefiletsv_out,
        in4=landmark_datacollection_utils_rmacextractor_outings_vc_func_bc9b_instance.outputs.outputfeaturefiletsv_out
    )
    return {'outputfeaturefiletsv_out': generalselectcosmos_func_6228_instance.outputs.outputtsv_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating image_vector_generation_sub_graph_50b0")
    pipeline = image_vector_generation_sub_graph_50b0()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='image_vector_generation_sub_graph_50b0')
    print(datetime.now(), "Finish")
