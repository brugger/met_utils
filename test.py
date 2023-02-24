#!/usr/bin/env python3
#
# Kim Brugger (13.02.2023) kbr(at)brugger.dk

import sys
import os
import pprint as pp

sys.path.append(".")

import met_utils

def main():

    API_KEY = os.getenv('MET_KEY')

    df = met_utils.get_all_vestland_sensors(API_KEY)
#    print( df )

    for n in df['name']:
        print( n )


    print( "SN58900 location:",  met_utils.get_coordinates_by_id('SN58900', df))
    try:
        print( "SN58900s location:",  met_utils.get_coordinates_by_id('SN58900s', df))
    except Exception as e:
        print('location finding failed, as expected')


if __name__ == "__main__":
    main()
