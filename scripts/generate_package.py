import os
from pathlib import Path
from azure.ml.component import dsl


def get_assets_from_components(component_folder):
    assets = {}
    for name in os.listdir(component_folder):
        sub_folder_path = os.path.join(component_folder, name)
        if os.path.isdir(sub_folder_path):
            assets[name] = f"file:{sub_folder_path}/**/*.yaml"
    return assets


components_folder = Path(__file__).parent.parent / 'ml' / 'sample' / 'components'
dsl.generate_package(force_regenerate=True,
                     assets=get_assets_from_components(components_folder),
                     package_name='.',
                     source_directory=components_folder,
                     mode='reference')
