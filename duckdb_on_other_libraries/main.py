import pandas as pd
import polars as pl
import pyarrow as pa
import duckdb


##### polars #####
# duckdb on polars dataframe
pl_df = pl.DataFrame({'ID': [1,2,3,4,5], 'Name': ['Microsoft', 'Apple', 'Netflix', 'Spotify', 'Intel']})
rel = duckdb.sql('select * from pl_df')
print('\nDuckDB relation from Polars df: \n', rel, type(rel))

# duckdb to polars
pl_df_from_duckdb = rel.pl()
print('\nPolars df from DuckDB: \n', type(pl_df_from_duckdb))

##### pandas #####
# duckdb on pandas dataframe - pandas to duckdb
df = pl_df.to_pandas()
rel = duckdb.sql('select * from df')
print('\nDuckDB relation from Pandas df: \n', rel, type(rel))

# duckdb to polars
df_from_duckdb = rel.df()
print('\nPandas df from DuckDB: \n', type(df_from_duckdb))

##### arrow #####
# duckdb on arrow table - arrow to duckdb
arrow = pl_df.to_arrow()
rel = duckdb.sql('select * from arrow')
print('\nDuckDB relation from Arrow table: \n', rel, type(rel))

# duckdb to arrow
arrow_from_duckdb = rel.arrow()
print('\nArrow table from DuckDB: \n', type(arrow_from_duckdb))