
# Met-Utils




## Setup

First off create a API key to be access the frost API here:
https://frost.met.no/auth/credentialsCreated.html. Note down both the ID and the secret.

The easiest way to use the package is to install it in your environment

``` 
pip install git+https://github.com/brugger/met_utils

```

## Example script

``` 
#!/usr/bin/env python3

import met_utils 

frost_api_id = '<YOUR_FROST_ID>'
# Get all vestlands sensors
sensors_df = met_utils.get_all_vestland_sensors( frost_api_id )
# print location of sensor: SN58900
print( "SN58900 location:",  met_utils.get_coordinates_by_id('SN58900', sensors_df))
```



## Functions


### get_all_vestland_sensors(frost_api_id:str) -> DataFrame

Returns a pandas dataframe with the sensor information
In the case of api request errors will raise an exception


### get_coordinates_by_id(id:str, sensors_df:DataFrame) -> List

Will raise an exception in the case of 1. sensor id not in the dataframe, or 2. No coordinates for a sensor




