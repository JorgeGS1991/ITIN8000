# Imports the data from dc-wikia-data.csv and marvel-wikia-data.csv
# combines them into a single JSON file called ComicCharacters.JSON
# The JSON file should list every character as an object by "Character Name"
# Must Contain Object Ownership containing the value Publisher (DC or Marvel)
# Must contain the object Characteristics containing the values:
# Alignment (Good, Bad, or Neutral)
# Eye Color
# Hair Color
# Gender
# When run it should generate a new file

import pandas as pd
import json
import csv
import glob

extension = 'csv'
exname = ["dc-wikia-data.csv", "marvel-wikia-data.csv"]
all_filenames: [exname] = [i for i in glob.glob('*.{}'.format(extension))]
# combine all files in the fname
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export csv files to json
combined_csv.to_csv( "ComicCharacters.csv", index=False, encoding='utf-8-sig')


# Read in your .csv files as dataframes
# df is a common standard for naming a dataframe. You can
# name them something more descriptive as well.
# Using a descriptive name is helpful when you are dealing
# with multiple .csv files.
df = pd.read_csv("ComicCharacters.csv")


sorted_df = df.sort_values(by=["name"], ascending=True)

# Index=False is a flag that tells pandas not to write
# the index of each row to a new column. If you'd like
# your rows to be numbered explicitly, leave this as
# the default, True
sorted_df.to_csv('ComicCharacters.csv', index=False)

#csv to Json file
#csv.to_json("ComicCharacters.JSON", orient='records',lines=True)

df = pd.read_csv (r'ComicCharacters.csv')
df.to_json (r'ComicCharacters.json', orient='records',lines=True)


