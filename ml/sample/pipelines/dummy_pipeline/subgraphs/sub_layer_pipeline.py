from azure.ml.component import dsl
from sub_sub_layer_pipeline import third_layer_sub_pipeline


@dsl.pipeline()
def second_layer_sub_pipeline(input_data):
    sub = third_layer_sub_pipeline(input_data)
    for i in range(10):
        next_sub = third_layer_sub_pipeline(input_data=sub.outputs.output_data)
        sub = next_sub
    return sub.outputs
