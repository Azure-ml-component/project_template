# THIS IS AN AUTO GENERATED FILE.
# PLEASE DO NOT MODIFY MANUALLY.
from azureml.core import Workspace


_default_workspace_from_config = None


def from_config():
    global _default_workspace_from_config
    if _default_workspace_from_config is None:
        try:
            _default_workspace_from_config = Workspace.from_config()
        except Exception:
            raise Exception('''
Get default workspace failed, please create config.json in current directory and specify workspace info in it.
The format of config.json likes below:
{
    "subscription_id": <Your subscription id>,
    "resource_group": <Your resource group name>,
    "workspace_name": <Your workspace name>,
}

            ''')
    return _default_workspace_from_config
