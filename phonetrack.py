# Import Frameworks
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

# Choose a Program Language
print ("Choose Program Language (TR / EN) ")
language = input()

if language == "tr" or language == "Tr" or language == "TR":
    # Get a Phone Number
    number = input( "Telefon numarası giriniz: " )
    phoneNumber = phonenumbers.parse( number )
    timeZone = timezone._country_level_time_zones_for_number( phoneNumber )
    print( "Zaman: " + str(timeZone) )
    geolocation = geocoder.description_for_number( phoneNumber,"tr" )
    print( "Lokasyon: " + geolocation )
    service = carrier.name_for_number( phoneNumber,"tr" )
    print( "Servis: " + service )

elif language == "en" or language == "En" or language == "EN":
    # Get a Phone Number
    number = input( "Type the Phone Number Along With the Country Code: " )
    phoneNumber = phonenumbers.parse( number )
    timeZone = timezone._country_level_time_zones_for_number( phoneNumber )
    print( "Time: " + str(timeZone) )
    geolocation = geocoder.description_for_number( phoneNumber,"en" )
    print( "Location: " + geolocation )
    service = carrier.name_for_number( phoneNumber,"en" )
    print( "Service: " + service )