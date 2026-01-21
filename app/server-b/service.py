import pandas as pd

def clean_and_transform(data: str):
    df = pd.DataFrame(data)
    print(df.head())
    print(type(df))
    df = df.drop_duplicates()
    # remove duplicates rows
    df = df.dropna()
    # remove missing values

    bins = [-float('inf'), 18, 25, float('inf')]
    labels = ['cold', 'moderate', 'hot']
    df['temperature_category'] = pd.cut(df['temperature'], bins=bins, labels=labels).astype(str)

    bins = [-float('inf'), 10, float('inf')]
    labels = ['calm', 'windy']
    df['wind_category'] = pd.cut(df['wind_speed'], bins=bins, labels=labels).astype(str)

    return df.to_dict(orient='records')