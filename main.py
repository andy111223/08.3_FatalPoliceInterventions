import pandas as pd
import matplotlib.pyplot as plt

# 1
df = pd.read_csv('fatal-police-shootings-data.csv')

# 2
df['race'].fillna('Unknown', inplace=True)
race_mental_illness_counts = df.groupby(['race', 'signs_of_mental_illness']).size().unstack(fill_value=0)
print(race_mental_illness_counts)

# 3
total_victims_per_race = df['race'].value_counts()
mental_illness_victims = race_mental_illness_counts[True]
mental_illness_percentage = (mental_illness_victims / total_victims_per_race) * 100

race_mental_illness_counts['Percentage of cases'] = total_victims_per_race.index.map(mental_illness_percentage.round(1))
print(race_mental_illness_counts)

# 4
df['date'] = pd.to_datetime(df['date'])
df['Day of week'] = df['date'].dt.day_name()

day_of_week_counts = df['Day of week'].value_counts().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], fill_value=0
)

plt.figure(figsize=(10, 6))
plt.bar(day_of_week_counts.index, day_of_week_counts.values)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Interventions')
plt.title('Number of Fatal Interventions per Day of the Week')
plt.show()

# 5
data1 = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population')
data2 = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations')

states = pd.DataFrame(data1[0])
abbrev = pd.DataFrame(data2[1])

abbrev = abbrev[abbrev[('Status of region', 'Status of region')].isin(['State', 'Federal district', 'State (officially Commonwealth)'])]

states_cleaned = states[['State', 'Census population, April 1, 2010 [1][2]']]
states_cleaned.columns = ['State', 'Population']

abbrev_cleaned = abbrev[[('Name', 'Name'), ('USPS', 'Unnamed: 5_level_1')]]
abbrev_cleaned.columns = ['State', 'Abbreviation']

states_cleaned = states_cleaned[states_cleaned['State'].isin(abbrev_cleaned['State'])]

merged_df = states_cleaned.merge(abbrev_cleaned, on='State', how='inner')

merged_all = df.merge(merged_df, left_on='state', right_on='Abbreviation', how='inner')

interventions_per_state = merged_all.groupby('State').size()
interventions_df = interventions_per_state.to_frame(name='Total Interventions')

interventions_df = interventions_df.merge(merged_all[['State', 'Population']].drop_duplicates(), on='State', how='left')

interventions_df['Interventions per 1000 residents'] = (interventions_df['Total Interventions'] / interventions_df['Population']) * 1000

print(interventions_df)