def slash_split(period: dict) -> dict:
    """Splits date period into sub-dictionary"""
    period_dates = period['period']

    if period_dates.find('/') != None:
        items = period['period'].split('/')
        rdict = {'min': min(items), 'max': max(items)}
    else:
        rdict = {'min': period_dates, 'max': period_dates}

    return rdict