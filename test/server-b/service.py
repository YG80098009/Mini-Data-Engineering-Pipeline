import pandas as pd

def clean_and_transform(data):
    df = pd.DataFrame(data)
    df = df.drop_duplicates()
    df = df.dropna()

    bins = [0, 17, 25, df['temperature'].max()]
    labels = ['cold', 'moderate', 'hot']
    df['temperature_category'] = pd.cut(df['temperature'], bins=bins, labels=labels, include_lowest=True)


    bins = [df['wind_speed'].min(), 10, df['wind_speed'].max()]
    labels = ['calm', 'windy']
    df['wind_status'] = pd.cut(df['wind_speed'], bins=bins, labels=labels, include_lowest=True)


    return df.to_dict(orient='records')
