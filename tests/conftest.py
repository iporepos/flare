"""
One sentence module description
todo [major docstring improvement]


Features
--------
todo [major docstring improvement]

 - {feature 1}
 - {feature 2}
 - {feature 3}
 - {etc}

Overview
--------
todo [major docstring improvement] -- overview
Mauris gravida ex quam, in porttitor lacus lobortis vitae.
In a lacinia nisl. Pellentesque habitant morbi tristique senectus
et netus et malesuada fames ac turpis egestas.

Examples
--------
todo [major docstring improvement] -- examples
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla mollis tincidunt erat eget iaculis. Mauris gravida ex quam,
in porttitor lacus lobortis vitae. In a lacinia nisl.

"""
# --------------- imports ---------------
# import modules from other libs

# ---- native imports ----
import os
from pathlib import Path

# ---- external imports ----
import numpy as np
import pandas as pd

# ---- project imports ----
# fill [project imports]

# --------------- constants ---------------
# ---- public ----

# paths and files
# -------------------------------
BASE_DIR = Path(__file__).parent
REPO_NAME = os.path.basename(Path(BASE_DIR).parent)
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
# Example constant
DATA_NUMBERS_FILE = DATA_DIR / "test_numbers.csv"

# benchmark config
# -------------------------------
# Read environment variable, default to "0" (false)
RUN_BENCHMARKS = os.getenv("RUN_BENCHMARKS", "0") == "1"
# Read environment variable, default to "0" (false)
RUN_BENCHMARKS_XXL = os.getenv("RUN_BENCHMARKS_XXL", "0") == "1"

# ---- private ----


# --------------- functions ---------------
# ---- public ----

def testprint(s):
    # todo docstring
    s2 = f"{REPO_NAME} -- tests >>> {s}".lower()
    return s2

def make_output():
    # todo docstring
    testprint("making output dir")
    os.mkdirs(OUTPUT_DIR, exist_ok=True)
    return None

def make_numbers_data():
    # todo docstring
    testprint("making numbers data")
    if not os.path.isfile(DATA_NUMBERS_FILE):
        v = np.random.randint(low=10, high=100, size=100)
        v2 = np.random.randint(low=10, high=100, size=100)
        v3 = v2 / v
        df = pd.DataFrame(
            {
                "v1": v,
                "v2": v2,
                "v3": v3
            }
        )
        df.to_csv(DATA_NUMBERS_FILE, sep=";", index=False)
        testprint("data created")
    else:
        testprint("data already available")
    return None


def load_numbers_data():
    # todo docstring
    testprint("loading numbers data")
    df = pd.read_csv(DATA_NUMBERS_FILE, sep=";")
    return df

def download_dataset(name, url):
    # todo docstring
    testprint(f"downloading dataset {name} from {url}")
    return None, None

# ---- private ----


# --------------- classes ---------------
# ---- public ----
# ---- private ----


# --------------- script ---------------
# standalone behaviour as a script
if __name__ == "__main__":
    testprint("conftest.py")
    make_numbers_data()