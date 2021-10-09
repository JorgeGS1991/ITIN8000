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

# Import json, pandas, csv and glob
import pandas as pd
import json
import csv
import glob

#*** How to know when a character is coming from DC or Marvel***
# Get this done before combined into one document

# Add publisher column as Marvel
df_marvel = pd.read_csv("marvel-wikia-data.csv")
df_marvel['Publisher'] = 'Marvel'
df_marvel.to_csv('marvel-wikia-data.csv', index=False)

# Add publisher column as DC
df_DC = pd.read_csv("dc-wikia-data.csv")
df_DC['Publisher'] = 'DC'
df_DC.to_csv('dc-wikia-data.csv', index=False)

extension = 'csv'
# Combine DC and Marvel data to ComicCharacter.csv
exname = ["dc-wikia-data.csv", "marvel-wikia-data.csv"]
all_filenames: [exname] = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the fname
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv("ComicCharacters.csv", index=False, encoding='utf-8-sig')


# Read in your .csv files as dataframes
# df is a common standard for naming a dataframe.

df = pd.read_csv("ComicCharacters.csv")
sorted_df = df.sort_values(by=["name"], ascending=True)
sorted_df.to_csv('ComicCharacters.csv', index=False)

# Transfer CSV file to json
with open("ComicCharacters.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        # Select what's going to get transfer to JSON
        data.append({row[1]: {"Ownership":row[13], "Characteristics": {"ALIGN": row[4], "EYE": row[5], "HAIR": row[6], "SEX": row[7]}}})

# Transfer csv file to JSON
with open("ComicCharacters.json", "w") as f:
    json.dump(data, f, indent=4)
print("completed")

