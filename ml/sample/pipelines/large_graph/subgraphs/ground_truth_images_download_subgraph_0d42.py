from datetime import datetime
from azure.ml.component import dsl
from update_by_dateupdated_4cf1 import update_by_dateupdated_4cf1
from resources import attractions_entity_conflation_image_url_extractor_scope_module_func, generalselectcosmos_func, cosmos_split_1_tsv_to_10_func, createcosmospathfreely_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, image_dl_and_convert_to_base64_func, image_dl_and_convert_to_base64_func, image_dl_and_convert_to_base64_func, image_dl_and_convert_to_base64_func, image_dl_and_convert_to_base64_func, image_dl_and_convert_to_base64_func, image_dl_and_convert_to_base64_func, image_dl_and_convert_to_base64_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, copy_cosmospath_to_generictsv_func, image_dl_and_convert_to_base64_func, createcosmospathfreely_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, upload_to_vc_with_inputs_generictsv_func, copy_cosmospath_to_generictsv_func, upload_to_vc_with_inputs_generictsv_func, image_dl_and_convert_to_base64_func, createcosmospathfreely_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, createcosmospathfreely_func, createcosmospathfreely_func, get_image_attractiveness_score_using_base64_encoded_image_func, generalselectcosmos_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, generalselectcosmos_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, generalselectcosmos_func, get_image_attractiveness_score_using_base64_encoded_image_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: ground_truth_images_download_subgraph_0d42")
@dsl.pipeline(name='ground_truth_images_download_subgraph_0d42', default_compute_target='cpu-cluster')
def ground_truth_images_download_subgraph_0d42(
    master_candidate_pairs_filtered,
    master_attributes,
    conflation_date='',
    ground_truth_domain1='',
    ground_truth_domain2='',
    download_image_count='',
    ground_truth_domain3=''
):
    createcosmospathfreely_func_87b4_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_07.tsv""" % (conflation_date)
    )
    generalselectcosmos_func_629e_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SourceEntities = SELECT SourceEntityId AS EntityId FROM In1 WHERE SourceEntityDomain == "%s" OR SourceEntityDomain == "%s";""" % (ground_truth_domain1, ground_truth_domain2),
        select2="""CandidateEntities = SELECT CandidateEntityId AS EntityId FROM In1 WHERE CandidateEntityDomain == "%s" OR CandidateEntityDomain == "%s";""" % (ground_truth_domain1, ground_truth_domain2),
        select3='SELECT * FROM SourceEntities UNION DISTINCT SELECT * FROM CandidateEntities;',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=master_candidate_pairs_filtered
    )
    createcosmospathfreely_func_bae8_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/MergedAttractiveNessScore.ss""" % (conflation_date)
    )
    createcosmospathfreely_func_0788_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_08.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_78ac_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath='/local/EntityConflation/ImageProcessing/MasterGroundTruthImages.ss'
    )
    createcosmospathfreely_func_30a7_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_01.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_1655_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/GroundTruthFeeds/%s.ss""" % (ground_truth_domain1)
    )
    createcosmospathfreely_func_f0db_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/GroundTruthFeeds/%s.ss""" % (ground_truth_domain2)
    )
    createcosmospathfreely_func_bc1c_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_09.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_9775_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_00.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_d38c_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_03.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_1b95_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_06.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_719d_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_05.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_b6db_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_02.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_1f33_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageDownload_04.tsv""" % (conflation_date)
    )
    generalselectcosmos_func_96ca_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='GroundTruthImages1 = SELECT In1.EntityId, Photo AS PhotoUrls FROM In1 INNER JOIN In2 ON In1.EntityId == In2.Id;',
        select2='GroundTruthImages2 = SELECT In1.EntityId, Photo AS PhotoUrls FROM In1 INNER JOIN In3 ON In1.EntityId == In3.Id;',
        select3='SELECT * FROM GroundTruthImages1 UNION DISTINCT SELECT * FROM GroundTruthImages2;',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in2=createcosmospathfreely_func_1655_instance.outputs.createdpath_out,
        in3=createcosmospathfreely_func_f0db_instance.outputs.createdpath_out,
        in1=master_attributes
    )
    generalselectcosmos_func_fc6e_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.* FROM In1 INNER JOIN In2 ON In1.EntityId == In2.EntityId;',
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
        in1=generalselectcosmos_func_96ca_instance.outputs.outputstream_out,
        in2=generalselectcosmos_func_629e_instance.outputs.outputstream_out
    )
    attractions_entity_conflation_image_url_extractor_scope_module_func_instance = attractions_entity_conflation_image_url_extractor_scope_module_func(
        max_image_count=download_image_count,
        vc='cosmos08/Outings',
        master_features_stream=generalselectcosmos_func_fc6e_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_cfbf_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT EntityId, ImageUrl FROM In1 EXCEPT DISTINCT SELECT EntityId, ImageUrl FROM In2;',
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
        scopeparams='-tokens 5',
        in1=attractions_entity_conflation_image_url_extractor_scope_module_func_instance.outputs.image_urls_out,
        in2=createcosmospathfreely_func_78ac_instance.outputs.createdpath_out
    )
    cosmos_split_1_tsv_to_10_func_instance = cosmos_split_1_tsv_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputfile=generalselectcosmos_func_cfbf_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_generictsv_func_c2ab_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part0_out
    )
    copy_cosmospath_to_generictsv_func_4f44_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part1_out
    )
    copy_cosmospath_to_generictsv_func_55e2_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part2_out
    )
    copy_cosmospath_to_generictsv_func_9b1c_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part5_out
    )
    copy_cosmospath_to_generictsv_func_979c_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part4_out
    )
    copy_cosmospath_to_generictsv_func_e7a8_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part3_out
    )
    copy_cosmospath_to_generictsv_func_ca23_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part6_out
    )
    copy_cosmospath_to_generictsv_func_e87e_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part7_out
    )
    copy_cosmospath_to_generictsv_func_2f66_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part8_out
    )
    copy_cosmospath_to_generictsv_func_53fc_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part9_out
    )
    image_dl_and_convert_to_base64_func_1b23_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_c2ab_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_0b3a_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_4f44_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_3a70_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_55e2_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_7434_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_9b1c_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_2dbb_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_979c_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_fbc8_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_e7a8_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_ee0f_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_ca23_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_07d8_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_e87e_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_ad80_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_2f66_instance.outputs.tsv_out
    )
    image_dl_and_convert_to_base64_func_8f0a_instance = image_dl_and_convert_to_base64_func(
        max_size='500',
        input=copy_cosmospath_to_generictsv_func_53fc_instance.outputs.tsv_out
    )
    upload_to_vc_with_inputs_generictsv_func_374d_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_1b23_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_9775_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_ca76_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_1b23_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_8c49_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_0b3a_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_30a7_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_a6fe_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_0b3a_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_0116_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_3a70_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_b6db_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_89ff_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_3a70_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_3a2c_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_7434_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_719d_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_a977_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_7434_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_e068_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_2dbb_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_1f33_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_a983_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_2dbb_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_6280_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_fbc8_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_d38c_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_cbfa_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_fbc8_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_edbe_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_ee0f_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_1b95_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_df60_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_ee0f_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_4bbe_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_07d8_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_87b4_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_9e20_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_07d8_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_8cd6_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_ad80_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_0788_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_be60_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_ad80_instance.outputs.output_out
    )
    upload_to_vc_with_inputs_generictsv_func_54d1_instance = upload_to_vc_with_inputs_generictsv_func(
        shouldrespectlineboundaries='false',
        overwrite='true',
        expiration='',
        datamanagementenabled='true',
        tsv=image_dl_and_convert_to_base64_func_8f0a_instance.outputs.output_out,
        destinationpath=createcosmospathfreely_func_bc1c_instance.outputs.createdpath_out
    )
    get_image_attractiveness_score_using_base64_encoded_image_func_b411_instance = get_image_attractiveness_score_using_base64_encoded_image_func(
        param1='10',
        input1=image_dl_and_convert_to_base64_func_8f0a_instance.outputs.output_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_c645_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_00.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_ca76_instance.outputs.output1_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_cb2a_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_01.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_a6fe_instance.outputs.output1_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_6af7_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_02.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_89ff_instance.outputs.output1_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_18fc_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_05.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_a977_instance.outputs.output1_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_65b7_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_04.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_a983_instance.outputs.output1_out
    )
    generalselectcosmos_func_5bb4_instance = generalselectcosmos_func(
        extractcols1='Id:string, ImageUrl:String, Base64:String',
        extractcols2='Id:string, ImageUrl:String, Base64:String',
        extractcols3='Id:string, ImageUrl:String, Base64:String',
        extractcols4='Id:string, ImageUrl:String, Base64:String',
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
        scopeparams='-tokens 4',
        in1=upload_to_vc_with_inputs_generictsv_func_374d_instance.outputs.destinationpath_out,
        in2=upload_to_vc_with_inputs_generictsv_func_8c49_instance.outputs.destinationpath_out,
        in3=upload_to_vc_with_inputs_generictsv_func_0116_instance.outputs.destinationpath_out,
        in4=upload_to_vc_with_inputs_generictsv_func_6280_instance.outputs.destinationpath_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_4b56_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_03.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_cbfa_instance.outputs.output1_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_4b02_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_06.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_df60_instance.outputs.output1_out
    )
    generalselectcosmos_func_de90_instance = generalselectcosmos_func(
        extractcols1='Id:string, ImageUrl:String, Base64:String',
        extractcols2='Id:string, ImageUrl:String, Base64:String',
        extractcols3='Id:string, ImageUrl:String, Base64:String',
        extractcols4='Id:string, ImageUrl:String, Base64:String',
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
        scopeparams='-tokens 4',
        in1=upload_to_vc_with_inputs_generictsv_func_e068_instance.outputs.destinationpath_out,
        in2=upload_to_vc_with_inputs_generictsv_func_3a2c_instance.outputs.destinationpath_out,
        in3=upload_to_vc_with_inputs_generictsv_func_edbe_instance.outputs.destinationpath_out,
        in4=upload_to_vc_with_inputs_generictsv_func_4bbe_instance.outputs.destinationpath_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_081f_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_07.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_9e20_instance.outputs.output1_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_891b_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_08.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_be60_instance.outputs.output1_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_1b33_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/ImageProcessing/%s/ImageAttractiveNess_09.tsv""" % (conflation_date),
        overwrite='true',
        datamanagementenabled='false',
        expiration='',
        tsv=get_image_attractiveness_score_using_base64_encoded_image_func_b411_instance.outputs.output1_out
    )
    generalselectcosmos_func_42c8_instance = generalselectcosmos_func(
        extractcols1='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols2='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols3='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols4='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        select1='SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In1 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In2 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In3 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In4;',
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
        in1=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_c645_instance.outputs.destinationpath_out,
        in2=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_cb2a_instance.outputs.destinationpath_out,
        in3=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_6af7_instance.outputs.destinationpath_out,
        in4=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_4b56_instance.outputs.destinationpath_out
    )
    generalselectcosmos_func_bb3d_instance = generalselectcosmos_func(
        extractcols1='Id:string, ImageUrl:String, Base64:String',
        extractcols2='Id:string, ImageUrl:String, Base64:String',
        extractcols3='Id:string, ImageUrl:String, Base64:String',
        extractcols4='Id:string, ImageUrl:String, Base64:String',
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
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_5bb4_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_de90_instance.outputs.outputtsv_out,
        in3=upload_to_vc_with_inputs_generictsv_func_8cd6_instance.outputs.destinationpath_out,
        in4=upload_to_vc_with_inputs_generictsv_func_54d1_instance.outputs.destinationpath_out
    )
    generalselectcosmos_func_5c6e_instance = generalselectcosmos_func(
        extractcols1='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols2='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols3='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols4='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        select1='SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In1 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In2 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In3 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In4;',
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
        in1=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_65b7_instance.outputs.destinationpath_out,
        in2=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_18fc_instance.outputs.destinationpath_out,
        in3=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_4b02_instance.outputs.destinationpath_out,
        in4=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_081f_instance.outputs.destinationpath_out
    )
    generalselectcosmos_func_28fc_instance = generalselectcosmos_func(
        extractcols1='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols2='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols3='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        extractcols4='Id:string, ImageUrl:string, BWScore:double?, AttractiveNessScore :double?, Status:String',
        select1='SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In1 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In2 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In3 UNION DISTINCT SELECT Id, ImageUrl, BWScore, AttractiveNessScore FROM In4;',
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
        in1=generalselectcosmos_func_42c8_instance.outputs.outputstream_out,
        in2=generalselectcosmos_func_5c6e_instance.outputs.outputstream_out,
        in3=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_891b_instance.outputs.destinationpath_out,
        in4=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_1b33_instance.outputs.destinationpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_28fc_instance.outputs.outputstream_out,
        destinationpath=createcosmospathfreely_func_bae8_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_68ba_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='MergedImages = SELECT In1.Id AS EntityId, In1.ImageUrl, Base64, BWScore, AttractiveNessScore FROM In1 INNER JOIN In2 ON In1.Id == In2.Id AND In1.ImageUrl == In2.ImageUrl;',
        select2='SELECT *,DateTime.UtcNow.ToString() AS DateUpdated FROM MergedImages UNION DISTINCT SELECT * FROM In3;',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY EntityId, ImageUrl',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 5',
        in1=generalselectcosmos_func_bb3d_instance.outputs.outputstream_out,
        in2=cosmos_mirror_with_inputs_and_overwrite_func_instance.outputs.destinationpath_out,
        in3=createcosmospathfreely_func_78ac_instance.outputs.createdpath_out
    )
    update_by_dateupdated_subgraph = update_by_dateupdated_4cf1(
        datekey='EntityId',
        in1=generalselectcosmos_func_68ba_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_45ef_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT * FROM In1',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY EntityId, ImageUrl',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 5',
        in1=update_by_dateupdated_subgraph.outputs.filteredss_out
    )
    return {'master_ground_truth_images_out': generalselectcosmos_func_45ef_instance.outputs.outputstream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating ground_truth_images_download_subgraph_0d42")
    pipeline = ground_truth_images_download_subgraph_0d42()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='ground_truth_images_download_subgraph_0d42')
    print(datetime.now(), "Finish")
