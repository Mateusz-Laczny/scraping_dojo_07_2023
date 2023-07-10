import json
from typing import Any


def write_as_jsonl_file(filename: str, objects_as_dicts: list[dict[str, Any]]) -> None:
    with open(filename, "w") as f:
        for object_as_dict in objects_as_dicts:
            f.write(json.dumps(object_as_dict))
            f.write('\n')
