import json

from pprint import pprint

# offering.txt:
# {'address': {'locality': 'New York City',
#              'postal-code': '10036',
#              'region': 'NY',
#              'street-address': '147 West 43rd Street'},
#  'details': None,
#  'hotel_class': 4.0,
#  'id': 113317,
#  'name': 'Casablanca Hotel Times Square',
#  'phone': '',
#  'region_id': 60763,
#  'type': 'hotel',
#  'url': 'http://www.tripadvisor.com/Hotel_Review-g60763-d113317-Reviews-Casablanca_Hotel_Times_Square-New_York_City_New_York.html'}



# review.txt:
# {'author': {'id': '8C0B42FF3C0FA366A21CFD785302A032',
#             'location': 'Gold Coast',
#             'num_cities': 22,
#             'num_helpful_votes': 12,
#             'num_reviews': 29,
#             'num_type_reviews': 24,
#             'username': 'Papa_Panda'},
#  'date': 'December 17, 2012',
#  'date_stayed': 'December 2012',
#  'id': 147643103,
#  'num_helpful_votes': 0,
#  'offering_id': 93338,
#  'ratings': {'cleanliness': 5.0,
#              'location': 5.0,
#              'overall': 5.0,
#              'rooms': 5.0,
#              'service': 5.0,
#              'sleep_quality': 5.0,
#              'value': 5.0},
#  'text': 'Stayed in a king suite for 11 nights and yes it cots us a bit but we '
#          'were happy with the standard of room, the location and the '
#          'friendliness of the staff. Our room was on the 20th floor '
#          'overlooking Broadway and the madhouse of the Fairway Market. Room '
#          'was quite with no noise evident from the hallway or adjoining rooms. '
#          'It was great to be able to open windows when we craved fresh rather '
#          'than heated air. The beds, including the fold out sofa bed, were '
#          'comfortable and the rooms were cleaned well. Wi-fi access worked '
#          'like a dream with only one connectivity issue on our first night and '
#          'this was promptly responded to with a call from the service provider '
#          'to ensure that all was well. The location close to the 72nd Street '
#          'subway station is great and the complimentary umbrellas on the '
#          'drizzly days were greatly appreciated. It is fabulous to have the '
#          'kitchen with cooking facilities and the access to a whole range of '
#          'fresh foods directly across the road at Fairway.\n'
#          'This is the second time that members of the party have stayed at the '
#          'Beacon and it will certainly be our hotel of choice for future '
#          'visits.',
#  'title': '“Truly is "Jewel of the Upper Wets Side"”',
#  'via_mobile': False}

data = []
with open('review.txt') as f:
  for line in f:
    data.append(json.loads(line))
    break

pprint(data[0])
