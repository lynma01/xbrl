# %%
import logging
import json
from xbrl.cache import HttpCache
from xbrl.instance import XbrlParser, XbrlInstance
# just to see which files are downloaded
logging.basicConfig(level=logging.INFO)

cache: HttpCache = HttpCache('./cache')
parser = XbrlParser(cache)

schema_path = "../data/xbrls/nvidia/0001045810-21-000010-xbrl/nvda-20210131.htm"

inst: XbrlInstance = parser.parse_instance(schema_path)
# %%
inst_json = inst.json()
# %%
print(inst_json)
# %%
inst_dict = json.loads(inst_json)
# %%
inst_dict["facts"]
# %%
concept_list = []

# %%
inst_dict['facts']['f0']['decimals']
# %%
inst_dict['facts']['f0']['value']
# %%
