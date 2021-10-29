from azure.ml.component import dsl

assets = {
    'example_components': [
        'file:../../components/**/*.yaml',
        'azureml://feeds/azureml',
        'azureml://feeds/huggingface',
    ],
}

source_dir = '.'
dsl.generate_package(force_regenerate=True, assets=assets, package_name='ml-sample',
                     source_directory=source_dir, mode='snapshot')
