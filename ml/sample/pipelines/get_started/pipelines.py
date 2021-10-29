from azure.ml.component import dsl, Pipeline
from subgraphs.train_score_eval import sub_training_pipeline

from ..assets._workspace import from_config
from ..utils.utils import generate_pipeline_component

ws = from_config()

# define a sub pipeline
sub_pipeline_name = 'A_sub_pipeline_including_train_score_eval'
pipeline_component_version = '0.0.1'
training_pipeline_component = generate_pipeline_component(sub_training_pipeline,
                                                          sub_pipeline_name, pipeline_component_version, ws)


# define pipeline with sub pipeline
@dsl.pipeline(name='A_dummy_pipeline_that_trains_multiple_models_and_output_the_best_one',
              description='select best model trained with different learning rate')
def dummy_automl_pipeline(input_data, test_data, learning_rate1=0.01, learning_rate2=0.02) -> Pipeline:
    # using the registered pipeline component
    train_and_evaluate_model1 = training_pipeline_component(input_data=input_data,
                                                            test_data=test_data,
                                                            learning_rate=learning_rate1)
    # comment on sub-pipeline
    train_and_evaluate_model1.comment = f'Training sub-pipeline with {learning_rate1}'
    # this will create an anonymous pipeline component during submission
    train_and_evaluate_model2 = sub_training_pipeline(input_data, test_data, learning_rate2)
    train_and_evaluate_model2.comment = f'Training sub-pipeline with {learning_rate2}'
