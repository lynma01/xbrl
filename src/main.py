# %%
import logging
import json
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
with open(f'{fdir}/{company}/JSON/{fname}.json', 'w', encoding='utf-8') as f:
    f.write(inst.json())

# %%

period = {'period': '2021-01-38/2020-02-26'}
# %%
    

# %%

r_period = slash_split(period)
# %%

print(r_period)
# %%
