import json
from typing import Dict, TypedDict


class Config(TypedDict):
    uri: str
    export_data: str


# Type-safe get_config function
def get_config() -> Config:
    with open("config.json", "r") as json_file:
        config_data: Dict[str, str] = json.load(json_file)

    # Ensure the keys exist and their types are correct
    uri: str = config_data["uri"]
    export_data: str = config_data["export_data"]

    # Return a dictionary following the Config structure
    return {"uri": uri, "export_data": export_data}
