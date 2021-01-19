def get_heroku_name():
    return 'damp-brushlands-51855'


def get_heroku_endpoint():
    return 'render'


def get_app_query_url(id):
    heroku_name = get_heroku_name()
    heroku_endpoint = get_heroku_endpoint()
    return f'https://{heroku_name}.herokuapp.com/{heroku_endpoint}/{id}'


def get_steam_store_url(id):
    return f'https://store.steampowered.com/app/{id}/'


def get_steam_illustration_url(id):
    return f'https://cdn.cloudflare.steamstatic.com/steam/apps/{id}/library_600x900.jpg'


def get_steamdb_url(id):
    return f'https://steamdb.info/app/{id}/'
