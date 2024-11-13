import os
from pathlib import Path

from jinja2 import ChoiceLoader
from jinja2 import Environment
from jinja2 import FileSystemLoader

from . import common


ENUM_TEMPLATE = "enum.jinja2"
MODELS_TEMPLATE = "models.jinja2"
SERVICE_TEMPLATE = "service.jinja2"
HTTPX_TEMPLATE = "httpx.jinja2"
API_CONFIG_TEMPLATE = "apiconfig.jinja2"
tpath = os.environ.get("TEMPLATE_PATH", __file__)
TEMPLATE_PATH = Path(tpath).parent / "templates"

print("TEMPLATE_PATH", TEMPLATE_PATH)


def create_jinja_env():
    custom_template_path = common.get_custom_template_path()
    return Environment(
        loader=(
            ChoiceLoader(
                [
                    FileSystemLoader(custom_template_path),
                    FileSystemLoader(TEMPLATE_PATH),
                ]
            )
            if custom_template_path is not None
            else FileSystemLoader(TEMPLATE_PATH)
        ),
        autoescape=True,
        trim_blocks=True,
    )
