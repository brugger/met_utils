#!/usr/bin/env python3
#
# Kim Brugger (13.02.2023) kbr(at)brugger.dk

import sys
import os
import pprint as pp

sys.path.append(".")

import met_utils
import kbr.json_utils as json_utils

def main():

    API_KEY = os.getenv('MET_KEY')

#    df = met_utils.get_all_vestland_sensors(API_KEY)
#    sn_id = df[df['name'] == 'E39 VÅGSBOTN']['id'].item()

    sn_id = "SN50815"


#    data = met_utils.get_weather_by_id( API_KEY, sn_id, "2021-01-01", "2021-06-30")
#    json_utils.write('vaagsbotn_2021_1.json', data)
#    data = met_utils.get_weather_by_id( API_KEY, sn_id, "2022-01-01", "2021-12-31")
#    json_utils.write('vaagsbotn_2021_2.json', data)


    for y in range(0, 24):

        print( f"getting data for Q1 - 20{y:02d}")
        try:
            data = met_utils.get_weather_by_id( API_KEY, sn_id, f"20{y:02d}-01-01", f"20{y:02d}-04-01")
            json_utils.write(f'vaagsbotn_20{y:02d}_q1.json', data)
        except:
            print("No data for this year")






#    print( f"{sn_id = } location:",  met_utils.get_coordinates_by_id(sn_id, df))


if __name__ == "__main__":
    main()
