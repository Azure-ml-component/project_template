from ml.sample.components.get_started import samples_train, samples_score, samples_evaluate

from azure.ml.component import dsl, Pipeline


# define a pipeline
@dsl.pipeline(name='A_training_pipeline_including_train_score_eval',
              description='train model and evaluate model performance')
def sub_training_pipeline(input_data, learning_rate, test_data) -> Pipeline:
    train = samples_train(
        training_data=input_data,
        max_epochs=5,
        learning_rate=learning_rate)

    score = samples_score(
        model_input=train.outputs.model_output,
        test_data=test_data)

    eval = samples_evaluate(scoring_result=score.outputs.score_output)
    return eval.outputs
