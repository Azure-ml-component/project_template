from azure.ml.component import Component


def generate_pipeline_component(func, name, version, workspace):
    # Load or register the pipeline component
    try:
        training_pipeline_component = Component.load(workspace, name=name, version=version)
    except Exception:
        training_pipeline_component = Component.create(func, version=version)
    return training_pipeline_component
