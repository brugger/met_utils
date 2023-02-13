
# Met-Utils




## Setup

First off create a API key to be access the frost API here:
https://frost.met.no/auth/credentialsCreated.html. Note down both the ID and the secret.

Install the required packages:
```
pip install -r requirements.txt
```

It is recomended that you place the 

```
import sys
sys.path.append(".") # or path to where the met_utils.py is placed

```



## Example script

``` 
#!/usr/bin/env python3

import met_utils 

frost_api_id = '<YOUR_FROST_ID>'
# Get all vestlands sensors
sensors_df = get_all_vestland_sensors( frost_api_id )
# print location of sensor: SN58900
print( "SN58900 location:",  get_coordinates_by_id('SN58900', sensors_df))
```



## Functions


### get_all_vestland_sensors(frost_api_id:str) -> DataFrame

Returns a pandas dataframe with the sensor information
In the case of api request errors will raise an exception


### get_coordinates_by_id(id:str, sensors_df:DataFrame) -> List

Will raise an exception in the case of 1. sensor id not in the dataframe, or 2. No coordinates for a sensor





Met api:
1a388dfe-878b-4912-972b-8132aa98ea68

Met secret:
d646bad9-4454-48fb-959e-a42535d4faad


