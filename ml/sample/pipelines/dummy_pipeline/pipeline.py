from azure.ml.component import dsl
from subgraphs.sub_layer_pipeline import second_layer_sub_pipeline


@dsl.pipeline()
def first_layer_sub_pipeline(input_data):
    sub = second_layer_sub_pipeline(input_data)
    for i in range(10):
        next_sub = second_layer_sub_pipeline(input_data=sub.outputs.output_data)
        sub = next_sub
    return sub.outputs
