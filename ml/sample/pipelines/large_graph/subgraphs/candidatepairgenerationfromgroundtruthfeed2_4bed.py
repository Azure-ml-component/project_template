from datetime import datetime
from azure.ml.component import dsl
from groundtruthfeednamevectorgeneration_subgragh_4c54 import groundtruthfeednamevectorgeneration_subgragh_4c54
from candidatepair_generation_subgraph_eb43 import candidatepair_generation_subgraph_eb43
from resources import cosmos_split_1_tsv_to_10_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, cosmos_mirror_with_inputs_and_overwrite_func, cosmospathcreator_rundate_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: candidatepairgenerationfromgroundtruthfeed2_4bed")
@dsl.pipeline(name='candidatepairgenerationfromgroundtruthfeed2_4bed', default_compute_target='cpu-cluster')
def candidatepairgenerationfromgroundtruthfeed2_4bed(
    webrecords,
    groundtruthfeed,
    ground_truth_domain='',
    conflation_date=''
):
    cosmos_split_1_tsv_to_10_func_instance = cosmos_split_1_tsv_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputfile=webrecords
    )
    cosmospathcreator_rundate_func_instance = cosmospathcreator_rundate_func(
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/NewDomainUrlCandidates.ss""" % (conflation_date, ground_truth_domain),
        vc='vc://cosmos08/Outings',
        rundate='1/1/10'
    )
    groundtruthfeednamevectorgeneration_subgragh_subgraph = groundtruthfeednamevectorgeneration_subgragh_4c54(
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_4d68_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='8',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part8_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_9181_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='3',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part3_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_de90_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='4',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part4_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_bb73_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='5',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part5_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_3301_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='7',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part7_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_6497_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='6',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part6_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_aa95_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='2',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part2_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_26fa_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='9',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part9_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_9d87_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='0',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part0_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    candidatepair_generation_subgraph_21ab_subgraph = candidatepair_generation_subgraph_eb43(
        ground_truth_domain=ground_truth_domain,
        conflation_date=conflation_date,
        subfolder='1',
        inputfile=cosmos_split_1_tsv_to_10_func_instance.outputs.part1_out,
        locationtogroundtruthfeedid=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.locationtogroundtruthfeedid_out,
        groundtruthfeedtoitsnamevector=groundtruthfeednamevectorgeneration_subgragh_subgraph.outputs.groundtruthfeedtoitsnamevector_out,
        groundtruthfeed=groundtruthfeed
    )
    generalselectcosmos_func_4cd2_instance = generalselectcosmos_func(
        extractcols1='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols2='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols3='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols4='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        select1='In1 = SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=candidatepair_generation_subgraph_de90_subgraph.outputs.outputtsv_out,
        in2=candidatepair_generation_subgraph_bb73_subgraph.outputs.outputtsv_out,
        in3=candidatepair_generation_subgraph_6497_subgraph.outputs.outputtsv_out,
        in4=candidatepair_generation_subgraph_3301_subgraph.outputs.outputtsv_out
    )
    generalselectcosmos_func_cb16_instance = generalselectcosmos_func(
        extractcols1='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols3='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols4='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        select1='In1 = SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
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
        in1=candidatepair_generation_subgraph_de90_subgraph.outputs.namepairsim_out,
        in2=candidatepair_generation_subgraph_bb73_subgraph.outputs.namepairsim_out,
        in3=candidatepair_generation_subgraph_6497_subgraph.outputs.namepairsim_out,
        in4=candidatepair_generation_subgraph_3301_subgraph.outputs.namepairsim_out
    )
    generalselectcosmos_func_29df_instance = generalselectcosmos_func(
        extractcols1='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols2='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols3='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols4='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        select1='In1 = SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
        select2=';',
        select3=';',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=candidatepair_generation_subgraph_9d87_subgraph.outputs.outputtsv_out,
        in2=candidatepair_generation_subgraph_21ab_subgraph.outputs.outputtsv_out,
        in3=candidatepair_generation_subgraph_aa95_subgraph.outputs.outputtsv_out,
        in4=candidatepair_generation_subgraph_9181_subgraph.outputs.outputtsv_out
    )
    generalselectcosmos_func_faea_instance = generalselectcosmos_func(
        extractcols1='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols3='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols4='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        select1='In1 = SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
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
        in1=candidatepair_generation_subgraph_9d87_subgraph.outputs.namepairsim_out,
        in2=candidatepair_generation_subgraph_21ab_subgraph.outputs.namepairsim_out,
        in3=candidatepair_generation_subgraph_aa95_subgraph.outputs.namepairsim_out,
        in4=candidatepair_generation_subgraph_9181_subgraph.outputs.namepairsim_out
    )
    generalselectcosmos_func_6a1f_instance = generalselectcosmos_func(
        extractcols1='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols2='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols3='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        extractcols4='GUID:string, SourceEntityName:String, CandidateEntityDomain:String, CandidateEntityUrl:String, NameSimilarity:Double',
        select1='In1 = SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn <= 3;',
        select3='SELECT GUID, SourceEntityName, CandidateEntityDomain, CandidateEntityUrl, NameSimilarity, DateTime.UtcNow.ToString() AS DateUpdated FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=generalselectcosmos_func_29df_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_4cd2_instance.outputs.outputtsv_out,
        in3=candidatepair_generation_subgraph_4d68_subgraph.outputs.outputtsv_out,
        in4=candidatepair_generation_subgraph_26fa_subgraph.outputs.outputtsv_out
    )
    generalselectcosmos_func_6398_instance = generalselectcosmos_func(
        extractcols1='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols3='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols4='SourceEntityName:String, CandidateEntityName:String, NameSimilarity:Double',
        select1='In1 = SELECT * FROM In1 UNION DISTINCT SELECT * FROM In2 UNION DISTINCT SELECT * FROM In3 UNION DISTINCT SELECT * FROM In4',
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
        in1=generalselectcosmos_func_faea_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_cb16_instance.outputs.outputtsv_out,
        in3=candidatepair_generation_subgraph_4d68_subgraph.outputs.namepairsim_out,
        in4=candidatepair_generation_subgraph_26fa_subgraph.outputs.namepairsim_out
    )
    cosmos_mirror_with_inputs_and_overwrite_func_instance = cosmos_mirror_with_inputs_and_overwrite_func(
        expiration='',
        datamanagementenabled='true',
        shouldoverrideifexists='true',
        sourcepath=generalselectcosmos_func_6a1f_instance.outputs.outputstream_out,
        destinationpath=cosmospathcreator_rundate_func_instance.outputs.createdpath_out
    )
    return {'destinationpath_out': cosmos_mirror_with_inputs_and_overwrite_func_instance.outputs.destinationpath_out, 'namepairsim_out': generalselectcosmos_func_6398_instance.outputs.outputtsv_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating candidatepairgenerationfromgroundtruthfeed2_4bed")
    pipeline = candidatepairgenerationfromgroundtruthfeed2_4bed()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='candidatepairgenerationfromgroundtruthfeed2_4bed')
    print(datetime.now(), "Finish")
