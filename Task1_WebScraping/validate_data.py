import pandas as pd


df = pd.read_csv("books_data.csv")


print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nNull values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nRating distribution:")
print(df["rating"].value_counts().sort_index())

print("\nAvailability:")
print(df["availability"].value_counts())

print("\nDuplicate URLs:", df["url"].duplicated().sum())

print("\nUnique Ratings:")
print(sorted(df["rating"].unique()))

print("\nUnknown Categories:")
print((df["category"] == "Unknown").sum())

print("\nInvalid Prices:")
print((df["price"] <= 0).sum())

print("\nEmpty Titles:")
print((df["title"].str.strip() == "").sum())