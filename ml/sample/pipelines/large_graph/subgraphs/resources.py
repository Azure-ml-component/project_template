import os
import json
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from azure.ml.component import Component
from azureml.core import Workspace


COMPONENT_FOLDER = Path(os.path.abspath(__file__)).parent.parent / 'components'


def get_component_func(workspace):
    """
    Get component func for large pipeline.

    :param workspace:
    :return: Dict of component name and component func. The key is component name, value is component function.
    """
    with open(COMPONENT_FOLDER / 'components.json', 'r') as f:
        registered_components = json.load(f)

    # Check to see if components have been registered before
    if workspace._workspace_id not in registered_components:
        components_func_dict = _register_components_concurrent(workspace)
    else:
        component_info = registered_components[workspace._workspace_id]
        components_func = Component.batch_load(workspace, ids=component_info.values())
        components_func_dict = {name: func for name, func in zip(component_info.keys(), components_func)}
    return components_func_dict


def _register_components_concurrent(workspace):
    """
    Concurrently registers all components from the `components_dir` directory.

    :param workspace: Component registered workspace
    :return: Dict of component name and component func. The key is component name, value is component function.
    """
    # Get all component spec yaml files
    component_yamls = [(workspace, item) for item in COMPONENT_FOLDER.iterdir() if str(item).endswith('yaml')]
    with ThreadPoolExecutor() as executor:
        # Creates a ThreadPoolExecutor within a context and calls `_register_component` on each spec yaml file
        process = executor.map(lambda params: _register_component(*params), component_yamls)
    components_dicts = {component_result[0]: component_result[1] for component_result in process}
    components_func = {component._name: func for component, func in components_dicts.items()}

    # Dumps components file that maps component name to component id from registration
    with open(COMPONENT_FOLDER / 'components.json', "r+") as f:
        components_json = json.load(f)
        components_json[workspace._workspace_id] = {component._name: component._identifier
                                                    for component in components_dicts.keys()}
        f.seek(0)
        json.dump(components_json, f, indent=2)
    return components_func


def _register_component(workspace: Workspace, yaml_file: Path):
    """
    Registers a component from a spec yaml file.

    :param yaml_file: The path to the component spec yaml file
    :return: Component and registered component func
    """
    print(datetime.now(), f"Registering component {yaml_file.name}")
    # Registers anonymous component to workspace
    component_func = Component.from_yaml(workspace, str(yaml_file))
    return component_func(), component_func
