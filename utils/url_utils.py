def get_heroku_endpoint():
    return 'render'


def get_query_url(id, num_matches=None):
    heroku_endpoint = get_heroku_endpoint()
    url = f'/{heroku_endpoint}/{id}'

    if num_matches is not None:
        url += f'/{num_matches}'

    return url


def get_steam_store_url(id):
    return f'https://store.steampowered.com/app/{id}/'


def get_steam_illustration_url(id):
    return f'https://cdn.cloudflare.steamstatic.com/steam/apps/{id}/library_600x900.jpg'


def get_steamdb_url(id):
    return f'https://steamdb.info/app/{id}/'
