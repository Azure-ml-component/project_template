from datetime import datetime
from azure.ml.component import dsl
from resources import generalselectcosmos_func, cosmos_split_1_tsv_to_5_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, outings_description_ner_func, outings_description_ner_func, outings_description_ner_func, outings_description_ner_func, copy_cosmospath_to_generictsv_func, outings_description_ner_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, copy_aether_cosmos_with_fixed_destination_func, copy_aether_cosmos_with_fixed_destination_func, copy_aether_cosmos_with_fixed_destination_func, copy_aether_cosmos_with_fixed_destination_func, copy_aether_cosmos_with_fixed_destination_func, generalselectcosmos_func, generalselectcosmos_func, createcosmospathfreely_func, cosmos_mirror_with_inputs_and_overwrite_func


print(datetime.now(), "Declaring pipeline: named_entity_relationship_generation_subgraph_65f2")
@dsl.pipeline(name='named_entity_relationship_generation_subgraph_65f2', default_compute_target='cpu-cluster')
def named_entity_relationship_generation_subgraph_65f2(
    master_attributes,
    conflation_date=''
):
    generalselectcosmos_func_6b1f_instance = generalselectcosmos_func(
        extractcols1='*',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='SELECT EntityId, Description FROM In1 WHERE Description != NULL;',
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
        in1=master_attributes
    )
    createcosmospathfreely_func_13da_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/AttributeGeneration/%s/MasterNEROutput_1.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_acee_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/AttributeGeneration/%s/MasterNEROutput_0.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_c240_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/AttributeGeneration/%s/MasterNEROutput_3.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_9785_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath='/local/EntityConflation/AttributeGeneration/MasterNERJson.ss'
    )
    createcosmospathfreely_func_a602_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/AttributeGeneration/%s/MasterNEROutput_4.tsv""" % (conflation_date)
    )
    createcosmospathfreely_func_1337_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/AttributeGeneration/%s/MasterNEROutput_2.tsv""" % (conflation_date)
    )
    cosmos_split_1_tsv_to_5_func_instance = cosmos_split_1_tsv_to_5_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputfile=generalselectcosmos_func_6b1f_instance.outputs.outputtsv_out
    )
    copy_cosmospath_to_generictsv_func_eba6_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_5_func_instance.outputs.part1_out
    )
    copy_cosmospath_to_generictsv_func_8e7f_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_5_func_instance.outputs.part0_out
    )
    copy_cosmospath_to_generictsv_func_2e82_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_5_func_instance.outputs.part3_out
    )
    copy_cosmospath_to_generictsv_func_f054_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_5_func_instance.outputs.part2_out
    )
    copy_cosmospath_to_generictsv_func_587b_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_5_func_instance.outputs.part4_out
    )
    outings_description_ner_func_7435_instance = outings_description_ner_func(
        inputfile=copy_cosmospath_to_generictsv_func_eba6_instance.outputs.tsv_out
    )
    outings_description_ner_func_3278_instance = outings_description_ner_func(
        inputfile=copy_cosmospath_to_generictsv_func_8e7f_instance.outputs.tsv_out
    )
    outings_description_ner_func_273a_instance = outings_description_ner_func(
        inputfile=copy_cosmospath_to_generictsv_func_2e82_instance.outputs.tsv_out
    )
    outings_description_ner_func_3fbd_instance = outings_description_ner_func(
        inputfile=copy_cosmospath_to_generictsv_func_f054_instance.outputs.tsv_out
    )
    outings_description_ner_func_795d_instance = outings_description_ner_func(
        inputfile=copy_cosmospath_to_generictsv_func_587b_instance.outputs.tsv_out
    )
    copy_aether_cosmos_with_fixed_destination_func_5e06_instance = copy_aether_cosmos_with_fixed_destination_func(
        shouldoverrideifexists='true',
        infile=outings_description_ner_func_7435_instance.outputs.outputfile_out,
        destlocation=createcosmospathfreely_func_13da_instance.outputs.createdpath_out
    )
    copy_aether_cosmos_with_fixed_destination_func_db95_instance = copy_aether_cosmos_with_fixed_destination_func(
        shouldoverrideifexists='true',
        infile=outings_description_ner_func_3278_instance.outputs.outputfile_out,
        destlocation=createcosmospathfreely_func_acee_instance.outputs.createdpath_out
    )
    copy_aether_cosmos_with_fixed_destination_func_0c2a_instance = copy_aether_cosmos_with_fixed_destination_func(
        shouldoverrideifexists='true',
        infile=outings_description_ner_func_273a_instance.outputs.outputfile_out,
        destlocation=createcosmospathfreely_func_c240_instance.outputs.createdpath_out
    )
    copy_aether_cosmos_with_fixed_destination_func_9e03_instance = copy_aether_cosmos_with_fixed_destination_func(
        shouldoverrideifexists='true',
        infile=outings_description_ner_func_3fbd_instance.outputs.outputfile_out,
        destlocation=createcosmospathfreely_func_1337_instance.outputs.createdpath_out
    )
    copy_aether_cosmos_with_fixed_destination_func_783a_instance = copy_aether_cosmos_with_fixed_destination_func(
        shouldoverrideifexists='true',
        infile=outings_description_ner_func_795d_instance.outputs.outputfile_out,
        destlocation=createcosmospathfreely_func_a602_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_2acf_instance = generalselectcosmos_func(
        extractcols1='EntityId:string, NERJson: string',
        extractcols2='EntityId:string, NERJson: string',
        extractcols3='EntityId:string, NERJson: string',
        extractcols4='EntityId:string, NERJson: string',
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
        in1=copy_aether_cosmos_with_fixed_destination_func_db95_instance.outputs.outfile_out,
        in2=copy_aether_cosmos_with_fixed_destination_func_5e06_instance.outputs.outfile_out,
        in3=copy_aether_cosmos_with_fixed_destination_func_9e03_instance.outputs.outfile_out,
        in4=copy_aether_cosmos_with_fixed_destination_func_0c2a_instance.outputs.outfile_out
    )
    generalselectcosmos_func_e948_instance = generalselectcosmos_func(
        extractcols1='EntityId:string, NERJson: string',
        extractcols2='EntityId:string, NERJson: string',
        extractcols3='EntityId:string, NERJson: string',
        extractcols4='EntityId:string, NERJson: string',
        select1='SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 ',
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
        in1=generalselectcosmos_func_2acf_instance.outputs.outputtsv_out,
        in2=copy_aether_cosmos_with_fixed_destination_func_783a_instance.outputs.outfile_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_e948_instance.outputs.outputstream_out,
        destinationpath=createcosmospathfreely_func_9785_instance.outputs.createdpath_out
    )
    return {'master_ner_json_table_out': cosmos_mirror_with_inputs_and_overwrite_func_instance.outputs.destinationpath_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating named_entity_relationship_generation_subgraph_65f2")
    pipeline = named_entity_relationship_generation_subgraph_65f2()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='named_entity_relationship_generation_subgraph_65f2')
    print(datetime.now(), "Finish")
