from datetime import datetime
from azure.ml.component import dsl
from resources import cosmospathcreator_rundate_func, outings_ta_sid_mapping_bvt_func, generalselectcosmos_func, cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func, cosmospathcreator_rundate_func, cosmos_mirror_with_inputs_and_overwrite_func, cosmos_mirror_with_inputs_and_overwrite_func, cosmospathcreator_rundate_func, generalselectcosmos_func, copy_cosmospath_to_generictsv_func, create_generic_tsv_func, concat_generictsv_func, tsv_to_html_func, create_generic_tsv_func, concat_generictsv_func, cast_anyfile_to_generictsv_func


print(datetime.now(), "Declaring pipeline: ta_sid_mapping_bvt_a67c")
@dsl.pipeline(name='ta_sid_mapping_bvt_a67c', default_compute_target='cpu-cluster')
def ta_sid_mapping_bvt_a67c(
    ta_sid_mapping,
    conflation_date=''
):
    cosmospathcreator_rundate_func_60c3_instance = cosmospathcreator_rundate_func(
        relativepath='/local/OutingsAttractionsPipeline/TestData/EntityAttributeBVT/Baseline.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_af1c_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Stats/BVTStats.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    cosmospathcreator_rundate_func_1dc0_instance = cosmospathcreator_rundate_func(
        relativepath='/local/EntityConflation/GroundTruthFeeds/www.tripadvisor.com.ss',
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    create_generic_tsv_func_69ef_instance = create_generic_tsv_func(
        text='<strong>TA-SID BVT</strong>\\n',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    cosmospathcreator_rundate_func_738f_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/Backups/%s/Stats/BVTResults.ss""" % (conflation_date),
        vc='vc://cosmos08/Outings',
        rundate=conflation_date
    )
    create_generic_tsv_func_1705_instance = create_generic_tsv_func(
        text='Date\\tTrue Positives\\tFalse Positives\\tFalseNegatives\\tPrecision\\tRecall',
        tabseparator='\\t',
        lineseparator='\\n'
    )
    generalselectcosmos_func_fb34_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT EntityId, EntityName, TALink FROM In1 WHERE !String.IsNullOrEmpty(TALink)',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Get TA Sid Data',
        vc='cosmos08/Outings',
        scopeparams='',
        in1=cosmospathcreator_rundate_func_60c3_instance.outputs.createdpath_out
    )
    outings_ta_sid_mapping_bvt_func_instance = outings_ta_sid_mapping_bvt_func(
        date=conflation_date,
        vc='cosmos08/Outings',
        scopeparams='',
        ta_ground_truth=cosmospathcreator_rundate_func_1dc0_instance.outputs.createdpath_out,
        bvt_file=generalselectcosmos_func_fb34_instance.outputs.outputtsv_out,
        ta_sid_mapping=ta_sid_mapping
    )
    cosmos_mirror_with_inputs_and_overwrite_func_6ec2_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_ta_sid_mapping_bvt_func_instance.outputs.bvt_results_out,
        destinationpath=cosmospathcreator_rundate_func_738f_instance.outputs.createdpath_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_a360_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='false',
        shouldoverrideifexists='true',
        sourcepath=outings_ta_sid_mapping_bvt_func_instance.outputs.bvt_stat_out,
        destinationpath=cosmospathcreator_rundate_func_af1c_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_3b68_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""SELECT "%s".Replace("_","/") AS RunDate, "%s" AS Description, "TA->SID Precision" AS StatName, "BVT" AS Type, (float)Precision AS Value FROM In1 UNION DISTINCT SELECT "%s".Replace("_","/") AS RunDate, "%s" AS Description, "TA->SID Recall" AS StatName, "BVT" AS Type, (float)Recall AS Value FROM In1""" % (conflation_date, conflation_date, conflation_date, conflation_date),
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='Set up Format',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=cosmos_mirror_with_inputs_and_overwrite_func_a360_instance.outputs.destinationpath_out
    )
    generalselectcosmos_func_c08e_instance = generalselectcosmos_func(
        extractcols1='*',
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
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 25',
        in1=cosmos_mirror_with_inputs_and_overwrite_func_a360_instance.outputs.destinationpath_out
    )
    generalselectcosmos_func_30d9_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_3b68_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_generictsv_func_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_c08e_instance.outputs.outputtsv_out
    )
    concat_generictsv_func_0626_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=create_generic_tsv_func_1705_instance.outputs.outputfile_out,
        input_2=copy_cosmospath_to_generictsv_func_instance.outputs.tsv_out
    )
    tsv_to_html_func_instance = tsv_to_html_func(
        generatehlinkforurl='true',
        tsv=concat_generictsv_func_0626_instance.outputs.output_out
    )
    cast_anyfile_to_generictsv_func_instance = cast_anyfile_to_generictsv_func(
        input=tsv_to_html_func_instance.outputs.htmlreport_out
    )
    concat_generictsv_func_f1bc_instance = concat_generictsv_func(
        input2hasheader='0',
        input_1=create_generic_tsv_func_69ef_instance.outputs.outputfile_out,
        input_2=cast_anyfile_to_generictsv_func_instance.outputs.outputtsv_out
    )
    return {'qg_data_out': generalselectcosmos_func_30d9_instance.outputs.outputstream_out, 'htmlreport_out': concat_generictsv_func_f1bc_instance.outputs.output_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating ta_sid_mapping_bvt_a67c")
    pipeline = ta_sid_mapping_bvt_a67c()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='ta_sid_mapping_bvt_a67c')
    print(datetime.now(), "Finish")
