from datetime import datetime
from azure.ml.component import dsl
from resources import reversegeocoder_func, namesimilaritybasedcandidatepairgeneration_func


print(datetime.now(), "Declaring pipeline: candidatepairgenerationfromgroundtruthfeed_subgraph_edcf")
@dsl.pipeline(name='candidatepairgenerationfromgroundtruthfeed_subgraph_edcf', default_compute_target='cpu-cluster')
def candidatepairgenerationfromgroundtruthfeed_subgraph_edcf(
    locationtogroundtruthfeedid,
    webrecords,
    groundtruthfeedtoitsnamevector,
    ground_truth_domain=''
):
    reversegeocoder_func_instance = reversegeocoder_func(
        inputfile=webrecords
    )
    namesimilaritybasedcandidatepairgeneration_func_instance = namesimilaritybasedcandidatepairgeneration_func(
        inputfile3=reversegeocoder_func_instance.outputs.outputfile_out,
        inputfile1=locationtogroundtruthfeedid,
        inputfile2=groundtruthfeedtoitsnamevector
    )
    return {'candidatepairswithsimilarity_out': namesimilaritybasedcandidatepairgeneration_func_instance.outputs.outputfile_out}


if __name__ == '__main__':
    print(datetime.now(), "Creating candidatepairgenerationfromgroundtruthfeed_subgraph_edcf")
    pipeline = candidatepairgenerationfromgroundtruthfeed_subgraph_edcf()
    print(datetime.now(), "Validating")
    pipeline.validate()
    print(datetime.now(), "Saving")
    pipeline._save()
    print(datetime.now(), "Submitting")
    pipeline.submit(experiment_name='candidatepairgenerationfromgroundtruthfeed_subgraph_edcf')
    print(datetime.now(), "Finish")
