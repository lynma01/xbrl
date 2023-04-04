# %%
from bs4 import BeautifulSoup
import pprint
# %%
with open('../data/xbrls/nvidia/0001045810-21-000010-xbrl/nvda-20210131.htm') as fp:
    report = BeautifulSoup(fp, 'lxml-xml')
# %%

# %%
