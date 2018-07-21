import os

from mapbox import StaticStyle


def create_map_image():
    env = os.environ.copy()

    user_name = env.get('MAPBOX_USER_NAME')
    map_code = env.get('MAPBOX_CODE')

    service = StaticStyle()

    portland = {
        'type': 'Feature',
        'properties': {'name': 'Portland, OR'},
        'geometry': {
            'type': 'Point',
            'coordinates': [-122.7282, 45.5801]}}
    response = service.image(user_name, map_code, features=[portland])

    print(response)
    # add to a file
    with open('./output_file.png', 'wb') as output:
        _ = output.write(response.content)

    print('done')

if __name__ == '__main__':
    create_map_image()