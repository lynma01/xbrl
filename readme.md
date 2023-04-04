# Summary

> messing around with parsing xbrl files

- Ingests EDGAR SEC compressed XBRL files before parsing with py-xbrl, converting to JSON, and moving into ingested_data folder.

# Planned:

- [ ] ingest into mongodb for cleaning/transformation
- [ ] ingest other SEC xbrl filings (insider trades, etc.)

# Folder snapshot:
```
.
├── data
│   └── nvidia
│       ├── JSON
│       │   └── nvda-20210131.json
│       └── XBRL
│           ├── 0001045810-21-000010-xbrl
│           │   ├── consentofindependentregist.htm
│           │   ├── descriptionoftheregistrant.htm
│           │   ├── listofregistrantssubsidiar.htm
│           │   ├── nvda-20210131.htm
│           │   ├── nvda-20210131.xsd
│           │   ├── nvda-20210131_cal.xml
│           │   ├── nvda-20210131_def.xml
│           │   ├── nvda-20210131_g1.jpg
│           │   ├── nvda-20210131_g2.jpg
│           │   ├── nvda-20210131_lab.xml
│           │   ├── nvda-20210131_pre.xml
│           │   ├── nvda-2021xex311.htm
│           │   ├── nvda-2021xex312.htm
│           │   ├── nvda-2021xex321.htm
│           │   └── nvda-2021xex322.htm
│           ├── 0001045810-22-000036-xbrl
│           │   ├── consentofindependentregist.htm
│           │   ├── descriptionoftheregistrant.htm
│           │   ├── listofregistrantssubsidiar.htm
│           │   ├── nvda-20220130.htm
│           │   ├── nvda-20220130.xsd
│           │   ├── nvda-20220130_cal.xml
│           │   ├── nvda-20220130_def.xml
│           │   ├── nvda-20220130_g1.jpg
│           │   ├── nvda-20220130_g2.jpg
│           │   ├── nvda-20220130_lab.xml
│           │   ├── nvda-20220130_pre.xml
│           │   ├── nvda-2022xex311.htm
│           │   ├── nvda-2022xex312.htm
│           │   ├── nvda-2022xex321.htm
│           │   ├── nvda-2022xex322.htm
│           │   ├── nvidia-globalrsuagreementx.htm
│           │   └── nvidia-restatedcertificate.htm
│           └── 0001045810-23-000017-xbrl
│               ├── a2007planglobalrsuagreemen.htm
│               ├── consentofindependentregist.htm
│               ├── listofregistrantssubsidiar.htm
│               ├── nvda-20230129.htm
│               ├── nvda-20230129.xsd
│               ├── nvda-20230129_cal.xml
│               ├── nvda-20230129_def.xml
│               ├── nvda-20230129_g1.jpg
│               ├── nvda-20230129_g2.jpg
│               ├── nvda-20230129_lab.xml
│               ├── nvda-20230129_pre.xml
│               ├── nvda-2023xex311.htm
│               ├── nvda-2023xex312.htm
│               ├── nvda-2023xex321.htm
│               ├── nvda-2023xex322.htm
│               ├── nvidia-202310xkdescription.htm
│               └── nvidia-eipardecember12022.htm
├── poetry.lock
├── pyproject.toml
├── readme.md
├── src
│   ├── __init__.py
│   ├── html_parse.py
│   ├── main.py
│   └── utils
│       ├── __init__.py
│       └── parsing.py
└── tests
    ├── __init__.py
    └── test_slash_split.py
```
