import sqlite3
import pandas as pd

df1 = pd.read_csv('genom.csv' )
conn = sqlite3.connect("db.sqlite3")

# Define a dictionary to map columns to their desired dtype
dtype_mapping = {
    'start_position_on_the_genomic_accession': str,
    'end_position_on_the_genomic_accession': str,
    'exon_count': str,
    # Add other columns as needed
}

# Explicitly cast columns to the desired dtype
df1 = df1.astype(dtype_mapping)

# Fill NaN values with default values
df1['Aliases'].fillna('Default Aliases', inplace=True)
df1['other_designations'].fillna('Default other designations', inplace=True)
df1['genomic_nucleotide_accession'].fillna('Default genomic nucleotide accession', inplace=True)
df1['start_position_on_the_genomic_accession'].fillna('Default start position on the genomic accession', inplace=True)
df1['end_position_on_the_genomic_accession'].fillna('Default end position on the genomic accession', inplace=True)
df1['orientation'].fillna('Default orientation', inplace=True)
df1['exon_count'].fillna('Default exon count', inplace=True)
df1['OMIM'].fillna('Default OMIM', inplace=True)
df1['map_location'].fillna('Default map location', inplace=True)
df1['chromosome'].fillna('Default chromosome', inplace=True)

# Write the DataFrame to SQLite
df1.to_sql('geno_genome_crc', conn, if_exists='append', index=False)

# Close the connection
conn.close()
