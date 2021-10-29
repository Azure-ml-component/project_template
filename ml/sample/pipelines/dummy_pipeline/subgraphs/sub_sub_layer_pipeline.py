import os
from pathlib import Path

from azure.ml.component import dsl, Component
from azure.ml.component._util._yaml_utils import YAML


# 200 different component funcs
component_folder = Path(os.path.abspath(__file__)).parent.parent.parent.parent / 'components'
template_yaml_file_path = os.path.join(component_folder.absolute(), 'dummy_pipeline',
                                       'data_process', '0.0.10', 'component.yaml')

with open(template_yaml_file_path) as fin:
    template_dict = YAML.safe_load(fin)
    import concurrent.futures
    import tempfile
    import shutil
    thread_pool = concurrent.futures.ThreadPoolExecutor()
    component_func_array = []
    version_num = 1
    yaml = YAML(with_additional_representer=True)
    for i in range(20):
        # 10 components for a batch
        component_func_tasks = []
        for i in range(10):
            version = f"0.0.{version_num}"
            version_num = version_num + 1
            temp_dir = Path(tempfile.mkdtemp())
            temp_yaml_file_path = temp_dir / 'component.yaml'
            yaml._dump_yaml_file({
                **template_dict,
                "version": version
            }, temp_yaml_file_path)
            shutil.copy(os.path.join(component_folder, 'simple_component', 'do_nothing.py'),
                        temp_dir / 'do_nothing.py')
            component_func_tasks.append(thread_pool.submit(
                Component.from_yaml, yaml_file=temp_yaml_file_path))
        concurrent.futures.wait(component_func_tasks, return_when=concurrent.futures.ALL_COMPLETED)
        component_func_array = component_func_array + [future.result() for future in component_func_tasks]


@dsl.pipeline()
def third_layer_sub_pipeline(input_data):
    component_func = component_func_array[0]
    component = component_func(input_data=input_data)
    for i in range(199):
        component_func = component_func_array[i + 1]
        next_component = component_func(input_data=component.outputs.output_data)
        component = next_component
    return component.outputs
