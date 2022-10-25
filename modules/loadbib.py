def loadbib(bibfile:str)->list:
    """loadbib infomation as dict

    Parameters
    ----------
    bibfile : str
        absolute path for bibfiles

    Returns
    -------
    bibs : list
        list[dict]
    """
    with open(bibfile,"r",encoding="utf-8") as f:
        biblists = f.readlines()
    # get at mark lines for split
    bibs =[]
    at_idx = [i for i,b in enumerate(biblists) if "@" in b]
    range_idx = [[idx,at_idx[i+1]] for i,idx in enumerate(at_idx[:-1])]

    #convert key = {value} → {key:value}
    for r_ in range_idx:
        raw_bib = biblists[r_[0]+1:r_[1]]
        dict_bib = {}
        for bibstr in raw_bib:
            if len(bibstr)== 0 : continue
            bib_keyvalues = bibstr.split(" ")
            k = bib_keyvalues[0]
            v = bib_keyvalues[-1][1:-3]
            if k in['\n','}\n']:continue
            if v.isdecimal():
                v = int(v)
            dict_bib.update({k:v})
        # pprint.pprint(dict_bib)
        bibs.append(dict_bib)
    return bibs