import pandas as pd
import numpy as np


#def preprocess(df: pd.DataFrame) -> pd.DataFrame:
def preprocess(dataset):
    """
    Preprocess the input DataFrame.

    Args:
        dataset (pd.DataFrame): Input DataFrame to preprocess

    Returns:
        pd.DataFrame: Preprocessed DataFrame
    """
    # Drop unnecessary columns and fill NaN values
    dataset = dataset.drop(['id', 'race', 'carNumber'], axis=1)
    dataset['time'] = dataset['time'].fillna('NaN')

    # Add features to represent if the lap is the first or last lap
    dataset['last_lap'] = np.where((dataset['lapNumber'] == dataset.groupby(['circuit', 'date'])['lapNumber'].transform('max')), 1, 0)
    dataset['first_lap'] = np.where(dataset['lapNumber'] == 1, 1, 0)

    ## Add more information about the circuits
    circuits_type_url = "https://en.wikipedia.org/wiki/List_of_Formula_One_circuits"

    # Read all tables found on the page
    tables = pd.read_html(circuits_type_url)

    # Get the first table
    circ_df = tables[2]

    # Drop unnecessary columns
    circ_df = circ_df.drop(['Map', 'Grands Prix', 'Last length used', 'Season(s)'], axis=1)
    #circ_df = circ_df.drop(['Map', 'Grands Prix'], axis=1)

    # Transform Circuit column to adapt to the dataset
    circ_df['Circuit'] = circ_df['Circuit'].str.replace(' *', '')

    circ_df['Circuit'] = circ_df['Circuit'].replace(
        {
            'Albert Park Circuit': 'Albert Park Grand Prix Circuit',
            'Circuit Gilles-Villeneuve': 'Circuit Gilles Villeneuve',
            'Suzuka International Racing Course': 'Suzuka Circuit',
            'Intercity Istanbul Park': 'Istanbul Park',
            'Circuit Zandvoort': 'Circuit Park Zandvoort',
            'Algarve International Circuit': 'Autódromo Internacional do Algarve',
            'Autodromo José Carlos Pace': 'Autódromo José Carlos Pace'
        }
    )

    # Filter the circuits to only include those present in the dataset
    circ_df = circ_df[circ_df['Circuit'].isin(list(dataset['circuit'].unique()))]

    #circ_df['Last length used'] = circ_df['Last length used'].str[:5]
    #circ_df['Season(s)'] = circ_df['Season(s)'].str[:4]

    # Rename columns
    circ_df = circ_df.rename(
        columns={
            'Circuit': 'circuit',
            'Type': 'type',
            'Direction': 'direction',
            'Location': 'location',
            'Country': 'country',
            #'Last length used': 'length',
            'Turns': 'turns',
            #'Season(s)': 'first_season',
            'Grands Prix held': 'grands_prix_held'
        }
    )
    
    # Merge the circuit DataFrame with the main DataFrame
    dataset = pd.merge(dataset, circ_df, on='circuit', how='left')

    # Define column types
    dataset = dataset.astype(
        {
            'date': 'category',
            'time': 'category',
            'circuit': 'category',
            'driver': 'category',
            'constructor': 'category',
            'pitStop': 'category',
            'last_lap': 'category',
            'first_lap': 'category',
            'type': 'category',
            'direction': 'category',
            'location': 'category',
            'country': 'category',
            #'length': 'float64',
            'turns': 'int64',
            #'first_season': 'int64'
        }
    )

    # Add a binary feature called "day" where 1 means "hour_of_day" is between 6 and 20, and 0 otherwise
    #dataset['time'] = 

    return dataset
