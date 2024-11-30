import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"
with open(config_dir / "config.yml", "r") as f:
    config_yaml = yaml.safe_load(f)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
