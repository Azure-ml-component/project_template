from datetime import datetime
from azure.ml.component import dsl
from candidatepairgenerationfromgroundtruthfeed_subgraph_edcf import candidatepairgenerationfromgroundtruthfeed_subgraph_edcf
from resources import cosmos_split_1_tsv_to_10_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_cosmospath_to_generictsv_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, copy_intermediate_directory_or_file_to_fixed_cosmos_path_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, createcosmospathfreely_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func, generalselectcosmos_func


print(datetime.now(), "Declaring pipeline: candidatepair_generation_subgraph_eb43")
@dsl.pipeline(name='candidatepair_generation_subgraph_eb43', default_compute_target='cpu-cluster')
def candidatepair_generation_subgraph_eb43(
    inputfile,
    locationtogroundtruthfeedid,
    groundtruthfeed,
    groundtruthfeedtoitsnamevector,
    ground_truth_domain='',
    conflation_date='',
    subfolder=''
):
    cosmos_split_1_tsv_to_10_func_instance = cosmos_split_1_tsv_to_10_func(
        scopeparams='',
        vc='cosmos08/Outings',
        inputfile=inputfile
    )
    createcosmospathfreely_func_b618_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_09.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_c112_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_02.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_30f8_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_08.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_5850_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_03.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_40f9_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_07.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_2561_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_04.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_f9e6_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_05.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_5d73_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_06.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_5ca3_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_00.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    createcosmospathfreely_func_f0b2_instance = createcosmospathfreely_func(
        vc='vc://cosmos08/Outings',
        relativepath="""/local/EntityConflation/CandidateGeneration/%s/%s/%s/DomainUrlCandidates_01.tsv""" % (conflation_date, ground_truth_domain, subfolder)
    )
    copy_cosmospath_to_generictsv_func_083a_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part0_out
    )
    copy_cosmospath_to_generictsv_func_ea4a_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part1_out
    )
    copy_cosmospath_to_generictsv_func_aaf9_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part2_out
    )
    copy_cosmospath_to_generictsv_func_cd39_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part3_out
    )
    copy_cosmospath_to_generictsv_func_894d_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part4_out
    )
    copy_cosmospath_to_generictsv_func_4a84_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part5_out
    )
    copy_cosmospath_to_generictsv_func_a58b_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part6_out
    )
    copy_cosmospath_to_generictsv_func_c8c8_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part7_out
    )
    copy_cosmospath_to_generictsv_func_0f5e_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part8_out
    )
    copy_cosmospath_to_generictsv_func_9a38_instance = copy_cosmospath_to_generictsv_func(
        shouldrespectlineboundaries='false',
        path=cosmos_split_1_tsv_to_10_func_instance.outputs.part9_out
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_586e_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_083a_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_1eb0_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_ea4a_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_d952_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_aaf9_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_cac0_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_cd39_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_5bb2_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_894d_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_42c2_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_4a84_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_0805_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_a58b_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_5a29_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_c8c8_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_4b17_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_0f5e_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    candidatepairgenerationfromgroundtruthfeed_subgraph_eddd_subgraph = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
        ground_truth_domain=ground_truth_domain,
        webrecords=copy_cosmospath_to_generictsv_func_9a38_instance.outputs.tsv_out,
        locationtogroundtruthfeedid=locationtogroundtruthfeedid,
        groundtruthfeedtoitsnamevector=groundtruthfeedtoitsnamevector
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_a742_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_586e_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_5ca3_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_9989_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_1eb0_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_f0b2_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_83c3_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_d952_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_c112_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_5a80_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_cac0_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_5850_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_6f20_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_5bb2_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_2561_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_dc91_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_42c2_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_f9e6_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_3464_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_0805_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_5d73_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_7989_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_5a29_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_40f9_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_442b_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_4b17_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_30f8_instance.outputs.createdpath_out
    )
    copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_8266_instance = copy_intermediate_directory_or_file_to_fixed_cosmos_path_func(
        shouldrespectlineboundaries='true',
        shouldoverrideifexists='true',
        directoryresource=candidatepairgenerationfromgroundtruthfeed_subgraph_eddd_subgraph.outputs.candidatepairswithsimilarity_out,
        destinationpath=createcosmospathfreely_func_b618_instance.outputs.createdpath_out
    )
    generalselectcosmos_func_9e97_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_a742_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_b132_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_a742_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_8313_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_9989_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_61af_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_9989_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_52fd_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_83c3_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_19c8_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_83c3_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_3a1f_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_5a80_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_4c70_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_5a80_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_ea3c_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_6f20_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_ce50_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_6f20_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_1be7_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_dc91_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_2cb2_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_dc91_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_1c4a_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_3464_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_d00d_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_3464_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_3575_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_7989_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_993e_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_7989_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_7c3d_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_442b_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_5962_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_442b_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_ef4f_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, Sim:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1="""In1=SELECT GUID, SourceEntityName, "%s" AS CandidateEntityDomain, In2.Url AS CandidateEntityUrl, Sim AS NameSimilarity FROM In1 INNER JOIN In2 ON In1.CandidateEntityId==In2.Id;""" % (ground_truth_domain),
        select2='In1 = SELECT *, ROW_NUMBER() OVER(PARTITION BY GUID, CandidateEntityDomain ORDER BY NameSimilarity DESC) AS Rn FROM In1 HAVING Rn < 5;',
        select3='SELECT In1.GUID, In1.SourceEntityName, In1.CandidateEntityDomain, In1.CandidateEntityUrl, In1.NameSimilarity FROM In1;',
        select4=';',
        select5=';',
        ssclause='CLUSTERED BY GUID;',
        tsvclause=';',
        resourcestmts=';',
        referencestmts=';',
        comment='',
        vc='cosmos08/Outings',
        scopeparams='-tokens 4',
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_8266_instance.outputs.cosmospath_out,
        in2=groundtruthfeed
    )
    generalselectcosmos_func_b86b_instance = generalselectcosmos_func(
        extractcols1='GUID:String, SourceEntityName:String, CandidateEntityId:String, CandidateEntityName:String, NameSimilarity:Double',
        extractcols2='*',
        extractcols3='*',
        extractcols4='*',
        select1='In1=SELECT DISTINCT SourceEntityName, CandidateEntityName, NameSimilarity FROM In1;',
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
        in1=copy_intermediate_directory_or_file_to_fixed_cosmos_path_func_8266_instance.outputs.cosmospath_out
    )
    generalselectcosmos_func_a52b_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_9e97_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_8313_instance.outputs.outputtsv_out,
        in3=generalselectcosmos_func_52fd_instance.outputs.outputtsv_out,
        in4=generalselectcosmos_func_3a1f_instance.outputs.outputtsv_out
    )
    generalselectcosmos_func_e1e9_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_b132_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_61af_instance.outputs.outputtsv_out,
        in3=generalselectcosmos_func_19c8_instance.outputs.outputtsv_out,
        in4=generalselectcosmos_func_4c70_instance.outputs.outputtsv_out
    )
    generalselectcosmos_func_6185_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_ea3c_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_1be7_instance.outputs.outputtsv_out,
        in3=generalselectcosmos_func_1c4a_instance.outputs.outputtsv_out,
        in4=generalselectcosmos_func_3575_instance.outputs.outputtsv_out
    )
    generalselectcosmos_func_8330_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_ce50_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_2cb2_instance.outputs.outputtsv_out,
        in3=generalselectcosmos_func_d00d_instance.outputs.outputtsv_out,
        in4=generalselectcosmos_func_993e_instance.outputs.outputtsv_out
    )
    generalselectcosmos_func_c3e4_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_a52b_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_6185_instance.outputs.outputtsv_out,
        in3=generalselectcosmos_func_7c3d_instance.outputs.outputtsv_out,
        in4=generalselectcosmos_func_ef4f_instance.outputs.outputtsv_out
    )
    generalselectcosmos_func_95ef_instance = generalselectcosmos_func(
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
        in1=generalselectcosmos_func_e1e9_instance.outputs.outputtsv_out,
        in2=generalselectcosmos_func_8330_instance.outputs.outputtsv_out,
        in3=generalselectcosmos_func_5962_instance.outputs.outputtsv_out,
        in4=generalselectcosmos_func_b86b_instance.outputs.outputtsv_out
    )
    return {'outputtsv_out': generalselectcosmos_func_c3e4_instance.outputs.outputtsv_out, 'namepairsim_out': generalselectcosmos_func_95ef_instance.outputs.outputtsv_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating candidatepair_generation_subgraph_eb43")
    pipeline = candidatepair_generation_subgraph_eb43()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='candidatepair_generation_subgraph_eb43')
    print(datetime.now(), "Finish")
