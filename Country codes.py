country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

#Search dictionary for country code of india
print('Country code for India -')
print(country_code.get('India', 'Not found'))

#Search dictionary for country code of japan
print('Country code for Japan')
print(country_code.get('Japan', 'Not found'))
