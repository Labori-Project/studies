from biopandas.pdb import PandasPdb


ppdb = PandasPdb()
ppdb = ppdb.read_pdb(path='files/6ms7.pdb')

ppdb_df = ppdb.df['ATOM']

print(ppdb_df.tail())

