import pandas as pd
import polars as pl
import pyarrow as pa
import duckdb

# polars, pandas, arrow
pl_df = pl.DataFrame({'ID': [1,2,3,4,5], 'Name': ['Microsoft', 'Apple', 'Netflix', 'Spotify', 'Intel']})
df = pl_df.to_pandas()
arrow = pl_df.to_arrow()

# run duckdb quries on each
pl_result = duckdb.sql('select * from pl_df')
pd_result = duckdb.sql('select * from df')
arrow_result = duckdb.sql('select * from arrow')

print(pl_result, pd_result, arrow_result)