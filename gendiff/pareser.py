import json
import yaml


def parse(data, format_name):
    if format_name == "json":
        return json.loads(data)
    if format_name in ("yaml", "yml"):
        return yaml.load(data, Loader=yaml.SafeLoader)
    raise ValueError(f"Unsupported format: {format_name}")