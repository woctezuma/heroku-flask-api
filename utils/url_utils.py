def get_heroku_endpoint():
    return "render"


def get_query_url(id, num_matches=None):
    heroku_endpoint = get_heroku_endpoint()
    url = f"/{heroku_endpoint}/{id}"

    if num_matches is not None:
        url += f"/{num_matches}"

    return url


def get_steam_store_url(id):
    return f"https://store.steampowered.com/app/{id}/"


def get_steam_illustration_url(id):
    return f"https://cdn.cloudflare.steamstatic.com/steam/apps/{id}/library_600x900.jpg"


def get_steamdb_url(id):
    return f"https://steamdb.info/app/{id}/"


def fill_in_link_url(app, link_to_steam_store=False, num_matches=None):
    if link_to_steam_store:
        link_url = app["steam_store_url"]
    else:
        if num_matches is None:
            # Keep the value of num_matches which was known when creating app["query_url"]
            link_url = app["query_url"]
        else:
            # Override the value of num_matches
            link_url = get_query_url(app["id"], num_matches)

    app["link_url"] = link_url

    return app
