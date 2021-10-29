from datetime import datetime
from azure.ml.component import dsl
from resources import aml_itp_module_func, create_generic_tsv_file_for_transformer_on_py3_5_func


print(datetime.now(), "Declaring pipeline: cross_join_d285")
@dsl.pipeline(name='cross_join_d285', default_compute_target='cpu-cluster')
def cross_join_d285(
    input,
    conflation_date=''
):
    create_generic_tsv_file_for_transformer_on_py3_5_func_instance = create_generic_tsv_file_for_transformer_on_py3_5_func(
        l1='cd /local-nfs/users/jepatel/EntityConflation/CrossJoin/; rm ./CrossJoinedPairs.tsv 2>/dev/null; pip install networkx --target=.; python crossjoin.py -p ./PairsFiltered.tsv -fp ./CrossJoinedPairs.tsv; sleep 3600; echo Done',
        l2='',
        l3='',
        l4='',
        l5='',
        l6='',
        l7='',
        l8='',
        l9='',
        l11='',
        l12='',
        l13='',
        l14='',
        l15='',
        l16='',
        l17='',
        l18='',
        l19='',
        l20='',
        l21='',
        l22='',
        l23='',
        l24='',
        l25='',
        l26='',
        l27='',
        l28='',
        l29='',
        l30='',
        l31='',
        l32='',
        l33='',
        l34='',
        l35='',
        l36='',
        l37='',
        l38='',
        l39='',
        l40='',
        l41='',
        l42='',
        l43='',
        l44='',
        l45='',
        l46='',
        l47='',
        l48='',
        l49='',
        l50='',
        l51='',
        l52='',
        l53='',
        l54='',
        l55='',
        l56='',
        l57='',
        l58='',
        l59='',
        l60=''
    )
    aml_itp_module_func_instance = aml_itp_module_func(
        vc='local',
        cluster='Azure-EastUS-V100-32GB',
        clustergroupname='MS-Shared',
        sku='',
        vcblocklist='',
        clusterblocklist='',
        jobname_new='Conflation Cross Join from Aether module (regular job)',
        jobtype='RegularJob',
        preemptiblejob='Yes',
        nodecount_new='1',
        gpucount='0',
        registry='indexserveregistry.azurecr.io',
        dockerimage='indexserveregistry.azurecr.io/deepscale:2.1',
        command_new='PORT: Command',
        homepathmount='False',
        nodecountset='',
        minimumscaleintervalinminute='',
        blobaccountname='',
        blobcontainername='',
        blobmountpath='',
        blobmountoptions='',
        datadownloadreuse='True',
        tonfsfolder='/local-nfs/users/jepatel/EntityConflation/CrossJoin/PairsFiltered.tsv',
        fromnfsfolder='/local-nfs/users/jepatel/EntityConflation/CrossJoin/CrossJoinedPairs.tsv',
        tocosmospath='adl://outings-c08.azuredatalakestore.net/local/EntityConflation/Backups/03_20_2021_Test/MasterAllCandidatePairs.tsv',
        environmentvariables_new='',
        retrypolicy='',
        tensorboardenabled='False',
        indicator='',
        input1=input
    )
    return {'output_out': aml_itp_module_func_instance.outputs.output1_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating cross_join_d285")
    pipeline = cross_join_d285()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='cross_join_d285')
    print(datetime.now(), "Finish")
