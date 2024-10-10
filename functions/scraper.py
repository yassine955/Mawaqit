from datetime import datetime
import json
from typing import Any, List

from bs4 import BeautifulSoup
import requests
from functions.get_config import Config


def get_prayer_times_to_json(response: requests.Response, config: Config) -> None:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the script tag and extract the JavaScript containing the JSON-like data
    script_tag: Any = soup.find_all("script")[2]

    # Extract the JSON-like data from the script tag
    convert_to_json: str = str(
        str(script_tag).split("var confData = ")[1].split("]};")[0] + "]}"
    ).strip()

    # Write the extracted data to the file specified in the config
    with open(config["export_data"], "w") as json_file:
        json.dump(json.loads(convert_to_json), json_file, indent=4)


def get_current_time() -> List[str]:
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    calendar = data.get("calendar")

    month = datetime.now().month - 1
    day = datetime.now().day

    times = list(calendar[month][str(day)])

    times.pop(1)

    return times
