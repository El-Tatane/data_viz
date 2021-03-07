# import HTMLSession from requests_html
from requests_html import HTMLSession
import pandas as pd
import re
import numpy as np


df = pd.read_csv("/home/tatane/data/udemy/udemy_courses_augmented.csv", parse_dates=["published_timestamp"])

if "rating-number" not in df.columns:
    df["rating-number"] = np.nan
# create an HTML Session object
session = HTMLSession()

for i, row in df.iterrows():

    if i < 3380:
        continue
    # Use the object above to connect to needed webpage
    # resp = session.get(row["url"])
    resp = session.get(row["url"])

    # Run JavaScript code on webpage
    try:
        resp.html.render()
        res = resp.html.html
    except Exception as e:
        print(row["url"])
        print(e)
        continue

    p = re.compile('rating-number">(.*?)</span>')

    result = p.findall(res)

    if len(result) == 1 or len(result) == 2 and result[0] == result[1]:
        df.loc[i, "rating-number"] = result[0]
    else:
        print(i, row["url"], result)

    if i % 20 == 0:
        print(i, row["url"], result)
        df.to_csv("/home/tatane/data/udemy/udemy_courses_augmented.csv", index=False)

print(df["rating-number"].unique())
print(df.head(25))
df.to_csv("/home/tatane/data/udemy/udemy_courses_augmented.csv", index=False)

if __name__ == "__main__":
    pass