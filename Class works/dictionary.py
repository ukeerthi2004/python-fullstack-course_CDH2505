#dictionary
d={'N1': 'swetha','N2':'keerthi','N3':'Ravali'}
d.pop('N3')
"""
d.pop('N3')
'Ravali'
d
{'N1': 'tarani', 'N2': 'keerthi'}
"""
d.popitem('N2')
"""
d.popitem() # for end item removing
('N2', 'keerthi')
d
{'N1': 'tarani'}
"""
del d['N1'] # just accessing for one value
"""
d
{}
"""
d.keys()# for keys N1,N2,N3 O/p : dict_keys(['N1', 'N2', 'N3'])
d.values()# for vlues dict_values(['swetha', 'keerthi', 'Ravali'])
d.items()# for items dict_items([('N1', 'swetha'), ('N2', 'keerthi'), ('N3', 'Ravali')])
d.clear() # same as d {}

#input
d={'N1': 'swetha','N2':'keerthi','N3':'Ravali','N4':'shushumitha','N5':'tanmiy'}
len(d)#output : 5
max(d)#output : 'N5'
min(d)#output : 'N1'
sorted(d) #output:['N1', 'N2', 'N3', 'N4', 'N5']
