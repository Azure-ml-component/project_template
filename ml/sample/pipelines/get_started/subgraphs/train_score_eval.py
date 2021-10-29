from azure.ml.component import dsl, Pipeline

from components import samples_train as train_component_func, samples_score as score_component_func, \
    samples_evaluate as eval_component_func


# define a pipeline
@dsl.pipeline(name='A_training_pipeline_including_train_score_eval',
              description='train model and evaluate model performance')
def sub_training_pipeline(input_data, learning_rate, test_data) -> Pipeline:
    train = train_component_func(
        training_data=input_data,
        max_epochs=5,
        learning_rate=learning_rate)

    score = score_component_func(
        model_input=train.outputs.model_output,
        test_data=test_data)

    eval = eval_component_func(scoring_result=score.outputs.score_output)
    return eval.outputs
