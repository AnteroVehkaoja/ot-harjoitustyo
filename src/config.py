import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass


CELL_SIZE = os.getenv("CELL_SIZE")  or 48
HEIGHT = os.getenv("HEIGHT") or 10
WITDTH = os.getenv("WITDTH") or 10
NUMBEROFMINES = os.getenv("NUMBEROFMINES") or 15
GEN_GRID = os.getenv("GENERATE_GUESLESS_GRID") or "error"

GEN_GRID = str(GEN_GRID)
CELL_SIZE = int(CELL_SIZE)
HEIGHT = int(HEIGHT)
WITDTH = int(WITDTH)
NUMBEROFMINES = int(NUMBEROFMINES)
