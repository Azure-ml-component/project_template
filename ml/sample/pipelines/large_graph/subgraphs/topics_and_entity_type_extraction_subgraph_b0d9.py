from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, outings_topic_extraction_func, outings_dominant_type_classifier_func, copy_cosmospath_to_generictsv_func, generalselectcosmos_func, copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func, generalselectcosmos_func, generalselectcosmos_func, outings_remove_columns_from_structured_stream_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: topics_and_entity_type_extraction_subgraph_b0d9")
@dsl.pipeline(name='topics_and_entity_type_extraction_subgraph_b0d9', default_compute_target='cpu-cluster')
def topics_and_entity_type_extraction_subgraph_b0d9(
    ground_truth_domains_merged_attributes
):
    generalselectcosmos_func_4513_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT EntityId, EntityName AS Title, EntityDomain, EntityUrl, Description, EntityLatitude, EntityLongitude, Locality, Area, Region, Country, PostalCode, StreetAddress, Website, PhoneNumber, Tags + " " + RawCategory AS Tags FROM In1 WHERE (!String.IsNullOrEmpty(Description) OR !String.IsNullOrEmpty(Tags) OR !String.IsNullOrEmpty(RawCategory));',
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
        in1=ground_truth_domains_merged_attributes
    )
    outings_topic_extraction_func_instance = outings_topic_extraction_func(
        vc='cosmos08/Outings',
        scopeparams='',
        input_stream=generalselectcosmos_func_4513_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_5c4a_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT EntityId, Title, "" AS OriginalEntityName, EntityUrl, "" AS PageTitle, Description, Tags FROM In1;',
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
        in1=generalselectcosmos_func_4513_instance.outputs.outputstream_out
    )
    generalselectcosmos_func_0351_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT In2.*, Topics FROM In2 INNER JOIN In1 ON In1.EntityId == In2.EntityId;',
        select2='In2 = SELECT In2.*, string.Empty AS Topics FROM In2 WHERE Description == null;',
        select3='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2;',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=outings_topic_extraction_func_instance.outputs.output_stream_out,
        in2=ground_truth_domains_merged_attributes
    )
    copy_cosmospath_to_generictsv_func_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=generalselectcosmos_func_5c4a_instance.outputs.outputtsv_out
    )
    outings_dominant_type_classifier_func_instance = outings_dominant_type_classifier_func(
        inputdata=copy_cosmospath_to_generictsv_func_instance.outputs.tsv_out
    )
    copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_instance = copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func(
        vc='vc://cosmos08/Outings',
        relativepath='/local/AttractionsPipeline/IntermediateData/2019-09-22_2019-09-22/EntityTypeResults.tsv',
        overwrite='true',
        datamanagementenabled='true',
        expiration='0',
        tsv=outings_dominant_type_classifier_func_instance.outputs.dominantentitytypes_out
    )
    generalselectcosmos_func_9f2f_instance = generalselectcosmos_func(
        extractcols1='EntityId:string, EntityType:string, EntityTypeConfidence:double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1 = SELECT In2.*, EntityType FROM In2 INNER JOIN In1 ON In1.EntityId == In2.EntityId;',
        select2='In2 = SELECT In2.*, string.Empty AS EntityType FROM In2 WHERE (String.IsNullOrEmpty(Description) AND String.IsNullOrEmpty(Tags) AND String.IsNullOrEmpty(RawCategory));',
        select3='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2;',
        select4=';',
        select5=';',
        ssclause=';',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 20',
        in1=copy_intermediate_data_tsv_to_specific_vc_with_overwrite_func_instance.outputs.destinationpath_out,
        in2=ground_truth_domains_merged_attributes
    )
    generalselectcosmos_func_f6d9_instance = generalselectcosmos_func(
        extractcols1=':',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT In1.*, In2.EntityType FROM In1 FULL JOIN In2 ON In1.EntityId == In2.EntityId;',
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
        in1=generalselectcosmos_func_0351_instance.outputs.outputstream_out,
        in2=generalselectcosmos_func_9f2f_instance.outputs.outputstream_out
    )
    outings_remove_columns_from_structured_stream_func_instance = outings_remove_columns_from_structured_stream_func(
        columns_to_remove='Tags|RawCategory',
        vc='cosmos08/Outings',
        scopeparams='',
        input_stream=generalselectcosmos_func_f6d9_instance.outputs.outputstream_out
    )
    return {'outputstream_out': outings_remove_columns_from_structured_stream_func_instance.outputs.output_stream_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating topics_and_entity_type_extraction_subgraph_b0d9")
    pipeline = topics_and_entity_type_extraction_subgraph_b0d9()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='topics_and_entity_type_extraction_subgraph_b0d9')
    print(datetime.now(), "Finish")
