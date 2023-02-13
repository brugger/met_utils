#!/usr/bin/env python3
#
# Kim Brugger (13.02.2023) kbr(at)brugger.dk

import requests
from pandas import DataFrame
from typing import List 

MET_API_URL = 'https://frost.met.no'


def get_all_vestland_sensors(frost_api_id:str) -> DataFrame:

    url = f'{MET_API_URL}/sources/v0.jsonld?types=SensorSystem&county=vestland'

    sensors = []

    while True:

        response = requests.get( url, auth=(frost_api_id,'' ))
        if not response:
            error = response.json()['error']
            raise RuntimeError(f"Could not get Vestland sensors.\nError Message: {error['message']}: {error['reason']}")

        response = response.json()
        sensors += response['data']

        if "nextLink" in response:
            url = response['nextLink']
        else:
            break

    return DataFrame( sensors )

def get_coordinates_by_id(id:str, sensors_df:DataFrame) -> List:

    sensor = sensors_df.loc[sensors_df['id'] == id]['geometry']

    if sensor.size == 0:
        raise RuntimeError(f"Sensor with id '{id}' not found in the dataframe")

    # Not sure this will ever happen, but just to be sure
    if 'coordinates' not in sensor.values[0]:
        raise RuntimeError(f'No coordinates for sensor with id {id}')

    return sensor.values[0]['coordinates']


def main():
    
    frost_api_id = '1a388dfe-878b-4912-972b-8132aa98ea68'

    sensors_df = get_all_vestland_sensors( frost_api_id)
    print( "SN58900 location:",  get_coordinates_by_id('SN58900', sensors_df))
    get_coordinates_by_id('SN58900s', sensors_df)


if __name__ == "__main__":
    main()


