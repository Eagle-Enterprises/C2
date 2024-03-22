####################################################
#### Eagle Enterprises Propiertary Information  ####
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip instal pyserial)
import pynmea2

# Method to convert latitude and longitde degrees into decimals
def lat_long_converter(latitude, latitude_direction, longitude, longitude_direction):
    lat_dd = int(float(latitude)/100)
    lat_mm = float(latitude) - lat_dd * 100
    lat_multiplier = int(1 if latitude_direction in ['N', 'E'] else -1)
    lat_decimal = lat_multiplier * (lat_dd + lat_mm/60)
    lat_string = str(lat_decimal)

    long_dd = int(float(longitude)/100)
    long_mm = float(longitude) - long_dd * 100
    long_multiplier = int(1 if latitude_direction in ['N', 'E'] else -1)
    long_decimal = long_multiplier * (long_dd + long_mm/60)
    long_string = str(long_decimal)
    
    return lat_string+";"+long_string


# NMEA sentence example for testing
# $GPGGA,210230,3855.4487,N,09446.0071,W,1,07,1.1,370.5,M,-29.5,M,,*7A
nmea_sentence = "$GPGGA,210230,3855.4487,N,09446.0071,W,1,07,1.1,370.5,M,-29.5,M,,*7A"
nmea_sentence_parsed = pynmea2.parse(nmea_sentence)
coordinates = lat_long_converter(nmea_sentence_parsed.lat, nmea_sentence_parsed.lat_dir, nmea_sentence_parsed.lon, nmea_sentence_parsed.lon_dir)
print(coordinates)