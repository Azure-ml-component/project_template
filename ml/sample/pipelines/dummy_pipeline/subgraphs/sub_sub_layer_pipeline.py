from ml.sample.components.dummy_pipeline import data_process
from azure.ml.component import dsl


@dsl.pipeline()
def third_layer_sub_pipeline(input_data):
    component = data_process(input_data=input_data)
    for i in range(199):
        next_component = data_process(input_data=component.outputs.output_data)
        component = next_component
    return component.outputs
