# %%
import logging
import json
import polars as pl
from xbrl.cache import HttpCache
from xbrl.instance import XbrlParser, XbrlInstance

# %%
# just to see which files are downloaded
logging.basicConfig(level=logging.INFO)

cache: HttpCache = HttpCache('./cache')
parser = XbrlParser(cache)

fdir = "../data"
company = "nvidia"
ftype = "XBRL"
zipname = "0001045810-21-000010-xbrl"
fname = 'nvda-20210131'

fpath = f"{fdir}/{company}/{ftype}/{zipname}/{fname}.htm"

# %%
inst: XbrlInstance = parser.parse_instance(fpath)

# %%
fpath_json = f'{fdir}/{company}/JSON/{fname}.json'

with open(fpath_json, 'w', encoding='utf-8') as f:
    facts = json.loads(inst.json())
    json.dump(list(facts.values()), f, indent=4)

# %%

r_period = slash_split(period)
