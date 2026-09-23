"""Simple YAML/JSON config loader."""

import json
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def load_config(path: str) -> dict:
    """Load config from JSON or YAML file based on extension."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    
    text = p.read_text(encoding="utf-8")
    if p.suffix in (".yaml", ".yml") and HAS_YAML:
        return yaml.safe_load(text)
    elif p.suffix == ".json":
        return json.loads(text)
    else:
        raise ValueError(f"Unsupported config format: {p.suffix}")


def save_config(data: dict, path: str) -> None:
    """Save config to file."""
    p = Path(path)
    if p.suffix == ".json":
        p.write_text(json.dumps(data, indent=2), encoding="utf-8")
    elif HAS_YAML:
        p.write_text(yaml.dump(data, default_flow_style=False), encoding="utf-8")
