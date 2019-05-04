import pandas as pd

csv_path = "/home/ievgen/PycharmProjects/ML_course_hillel/course/data/DataSet_1.csv"
conversions_df = pd.read_csv(csv_path)
conversions_df['last name'].fillna('', inplace=True)
conversions_df.at[8, 'gender'] = "F"
conversions_df.at[14, 'gender'] = "M"
conversions_df.at[29, 'gender'] = "F"
conversions_df.at[37, 'gender'] = "M"


def convert_to_bool(val):
    values = {"y": 1, "n": 0}
    return values[val]


def convert_color(val):
    values = {"green": 2,
              'blue': 3,
              'red': 1,
             }
    return values[val]


def convert_to_age_group(val):
    return "1" if 1 <= val <= 29 else '2' if 30 <= val <= 49 else '3' if 50 <= val <= 120 else None


for i in range(len(conversions_df)):
    if conversions_df.at[i, 'seen count'] > 1e9:
        conversions_df.at[i, 'seen count'] = 0

conversions_df.insert(conversions_df.columns.get_loc("gender"), "full name", None)
for i in range(len(conversions_df)):
    conversions_df.at[i, "full name"] = \
        (conversions_df.at[i, "first name"] + " " + conversions_df.at[i, "last name"]).strip()


conversions_df.insert(conversions_df.columns.get_loc("gender"), "birthday", None)
for i in range(len(conversions_df)):
    conversions_df.at[i, "birthday"] = pd.Timestamp(
        day=conversions_df.at[i, "day of birth"],
        month=conversions_df.at[i, "month of birth"],
        year=conversions_df.at[i, "year of birth"]
    )

conversions_df.insert(conversions_df.columns.get_loc("gender"), "age", None)
for i in range(len(conversions_df)):
    conversions_df.at[i, "age"] = (pd.Timestamp.now() - conversions_df.at[i, "birthday"]).days // 365


conversions_df.drop(columns=["month of birth",  "day of birth", "year of birth"], axis=1, inplace=True)


for i in range(len(conversions_df)):
    conversions_df.at[i, "followed ad"] = convert_to_bool(conversions_df.at[i, "followed ad"])
    conversions_df.at[i, "made purchase"] = convert_to_bool(conversions_df.at[i, "made purchase"])
    conversions_df.at[i, "age category"] = convert_to_age_group(conversions_df.at[i, "age"])


def set_pandas():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)


set_pandas()

conversions_df = conversions_df.astype({'seen count': float, 'made purchase': int, 'followed ad': int})

conversion_df = conversions_df[['color scheme', 'followed ad', 'made purchase']].groupby('color scheme').mean()
print(conversion_df)
conversion_df = conversions_df[['color scheme', 'followed ad', 'made purchase']].groupby('color scheme').mean()

print(conversion_df)
print(conversions_df)
