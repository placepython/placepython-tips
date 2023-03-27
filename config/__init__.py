import pathlib
import sys

import environ

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, BASE_DIR / "wepynaire")

env = environ.Env()
env.read_env(BASE_DIR / ".env")
