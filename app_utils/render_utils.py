from app_utils.id_utils import id_to_app, id_to_similar_apps
from utils.url_utils import fill_in_link_url


def prepare_data_for_rendering(
    id, num_matches=-1, link_to_steam_store=False, mirror_x=False, flip_y=False
):
    try:
        query_app = id_to_app(id)
    except ValueError:
        query_app = None

    try:
        similar_apps = id_to_similar_apps(
            id, num_matches=num_matches, mirror_x=mirror_x, flip_y=flip_y
        )
    except ValueError:
        similar_apps = None

    if query_app is not None:
        query_app = fill_in_link_url(
            query_app, link_to_steam_store=link_to_steam_store, num_matches=num_matches
        )

    if similar_apps is not None:
        for i, app in enumerate(similar_apps):
            similar_apps[i] = fill_in_link_url(
                app, link_to_steam_store=link_to_steam_store, num_matches=num_matches
            )

    return query_app, similar_apps
