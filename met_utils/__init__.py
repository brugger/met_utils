#!/usr/bin/env python3
#
# Kim Brugger (13.02.2023) kbr(at)brugger.dk

import requests
from pandas import DataFrame
from typing import List 

import re


import pprint as pp

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


def get_weather_by_id(frost_api_id:str, id:str, start:str, end:str) -> DataFrame:

    url  = f'{MET_API_URL}/observations/v0.jsonld?'
    url += f'sources={id}'
    url += f'&elements=sum(precipitation_amount%20PT1H)%2Cwind_speed%2C%20air_temperature'
    url += f'&referencetime={start}%2F{end}'

#    print( url )

    days = {}

    while True:

        response = requests.get( url, auth=(frost_api_id,'' ))

        if not response:
            error = response.json()['error']
            raise RuntimeError(f"Could not get measurements from sensors.\nError Message: {error['message']}: {error['reason']}")

        response = response.json()
#        pp.pprint( response['data'])

        for observations in response['data']:
#            pp.pprint( observations )
            reftime = re.sub( r'T.*', '', observations['referenceTime'])
            if reftime not in days:
                days[ reftime ] = {}
            
            for observation in observations['observations']:
#                print( observation)

                elementId = observation['elementId']


                if 'precipitation_amount' in elementId:
                    days[ reftime ][ 'precipitation' ] = days[ reftime ].get('precipitation', 0) + int(observation['value'])
                elif elementId == 'wind_speed':
                    days[ reftime ][ 'wind_speed' ] = days[ reftime ].get('wind_speed', 0) + int(observation['value'])
                    days[ reftime ][ 'wind_speed_points' ] = days[ reftime ].get('wind_speed_points', 0) + 1
                elif elementId == 'air_temperature':
                    days[ reftime ][ 'air_temperature' ] = days[ reftime ].get('air_temperature', 0) + int(observation['value'])
                    days[ reftime ][ 'air_temperature_points' ] = days[ reftime ].get('air_temperature_points', 0) + 1


        for day in days:
            days[day][ 'wind_speed'] = days[day]['wind_speed']/days[day]['wind_speed_points']
            days[day][ 'air_temperature'] = days[day]['air_temperature']/days[day]['air_temperature_points']

            del days[day]['wind_speed_points']
            del days[day]['air_temperature_points']

        if "nextLink" in response:
            print('following nextLink')
            url = response['nextLink']
        else:
            break

#    pp.pprint( days )

    return days

    days_df = DataFrame( days )
    print( days_df.T )

    return days_df 

