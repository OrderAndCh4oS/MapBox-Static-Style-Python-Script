import os

from mapbox import StaticStyle
'''
Run: 
     export MAPBOX_ACCESS_TOKEN="YOUR_MAP_BOX_TOKEN" && \
     export MAPBOX_USER_NAME="YOUR_MAP_BOX_USER_NAME" && \
     export MAPBOX_CODE="YOUR_MAP_BOX_CODE" && \
     python main.py
'''

def create_map_image(features):
    env = os.environ.copy()

    user_name = env.get('MAPBOX_USER_NAME')
    map_code = env.get('MAPBOX_CODE')

    service = StaticStyle()

    response = service.image(user_name, map_code, features=features)

    print(response)
    # add to a file
    with open('./output_file.png', 'wb') as output:
        _ = output.write(response.content)

    print('done')

if __name__ == '__main__':
    ipswich = {
        'type': 'Feature',
        'properties': {'name': 'Ipswich, Suffolk'},
        'geometry': {
            'type': 'Point',
            'coordinates': [1.15545, 52.05917]}}
    colchester = {
        'type': 'Feature',
        'properties': {'name': 'Colchester, Essex'},
        'geometry': {
            'type': 'Point',
            'coordinates': [0.8919, 51.8959]}}
    create_map_image([ipswich, colchester])