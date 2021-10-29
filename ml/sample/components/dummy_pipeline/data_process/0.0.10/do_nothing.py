import shutil, os, sys
from pathlib import Path
from azure.ml.component import dsl
from azure.ml.component.dsl._component import InputPath, OutputPath, ComponentExecutor


@dsl._component(name='data_process')
def do_nothing_component_func(
        input_data: InputPath(),
        output_data: OutputPath()):
    pass


if __name__ == '__main__':
    ComponentExecutor(do_nothing_component_func).execute(sys.argv)
