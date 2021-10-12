from pyvis.network import Network
import tabula
import pandas as pd
from pprint import pprint 

df = tabula.read_pdf('edital.pdf', pages='all')
tbl = df[1]
tbl.head()


mtx = pd.crosstab(tbl['Docente'],tbl['Linha de pesquisa'])
mtx.set_index()