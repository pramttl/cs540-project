
# coding: utf-8

# In[3]:

from rdflib import Graph
g = Graph()
g.parse("imdb.rdf", format="xml")


# In[4]:

print len(g)


# In[2]:

predicates = set()
for s,p,o in g:
    predicates.add(p)

from pprint import pprint
pprint(list(predicates)[:50])


# In[12]:

subjects = set()
for s,p,o in g:
    subjects.add(s)

from pprint import pprint
pprint(subjects)


# In[6]:

import rdfextras
rdfextras.registerplugins()


# In[9]:

from rdflib import Namespace

querystr = """
SELECT ?aname ?bname
}"""
for row in g.query(
    querystr,

    print("%s knows %s" % row)

