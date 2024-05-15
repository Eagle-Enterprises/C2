####################################################
#### Eagle Enterprises Proprietary Information  ####
####################################################
#                  DESCRIPTION                     #
# This sample code takes a NMEA sentence, converts #
# it to coordinates and displays them to a         #
# terminal.                                        #
####################################################

# Imports
# Requires install of python, tkinter, pyserial, and pynmea2 (i.e. pip instal pyserial)
import pynmea2

# Method to convert latitude and longitde degrees into decimals
def lat_long_converter(latitude, latitude_direction, longitude, longitude_direction):
    lat_string = _extracted_from_lat_long_converter_2(latitude, latitude_direction)
    long_string = _extracted_from_lat_long_converter_2(
        longitude, latitude_direction
    )
    return f"{lat_string};{long_string}"


# TODO Rename this here and in `lat_long_converter`
def _extracted_from_lat_long_converter_2(arg0, latitude_direction):
    lat_dd = int(float(arg0) / 100)
    lat_mm = float(arg0) - lat_dd * 100
    lat_multiplier = 1 if latitude_direction in ['N', 'E'] else -1
    lat_decimal = lat_multiplier * (lat_dd + lat_mm/60)
    return str(lat_decimal)


# NMEA sentence example for testing
# $GPGGA,210230,3855.4487,N,09446.0071,W,1,07,1.1,370.5,M,-29.5,M,,*7A
nmea_sentence = "$GPGGA,210230,3855.4487,N,09446.0071,W,1,07,1.1,370.5,M,-29.5,M,,*7A"
nmea_sentence_parsed = pynmea2.parse(nmea_sentence)
coordinates = lat_long_converter(nmea_sentence_parsed.lat, nmea_sentence_parsed.lat_dir, nmea_sentence_parsed.lon, nmea_sentence_parsed.lon_dir)
print(coordinates)