from pathlib import Path
from box.exceptions import BoxValueError
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
import yaml
from deepClassifier import logger

@ensure_annotations
def read_yaml(file_path: Path)-> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    