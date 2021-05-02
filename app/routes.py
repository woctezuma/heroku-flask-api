from flask import jsonify, request, render_template
from flask import send_from_directory

from app import app
from app.default_values import (
    get_default_index,
    get_default_id,
    get_default_name,
    get_default_num_matches,
    get_default_num_matches_to_display,
    get_default_width,
    get_default_height,
)
from app.random_values import get_random_id
from app_utils.id_utils import id_to_index, id_to_name, id_to_app, id_to_similar_apps
from app_utils.index_utils import (
    index_to_id,
    index_to_name,
    index_to_app,
    index_to_matches,
    index_to_similar_apps,
)
from app_utils.name_utils import (
    name_to_index,
    name_to_id,
    name_to_app,
    name_to_similar_apps,
)
from app_utils.render_utils import prepare_data_for_rendering


@app.route("/")
def main():
    return "Welcome to my app!"

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/index")
def get_index():
    index = request.args.get("index", get_default_index())
    return jsonify(index)


@app.route("/id")
def get_id():
    index = request.args.get("index", get_default_index())
    id = index_to_id(index)
    return jsonify(id)


@app.route("/name")
def get_name():
    index = request.args.get("index", get_default_index())
    name = index_to_name(index)
    return jsonify(name)


@app.route("/app")
def get_app():
    index = request.args.get("index", get_default_index())
    app = index_to_app(index)
    return jsonify(app)


@app.route("/matches")
def get_matches():
    index = request.args.get("index", get_default_index())
    num_matches = request.args.get("n", get_default_num_matches())
    matches = index_to_matches(index, num_matches)
    return jsonify(matches)


@app.route("/similar_apps")
def get_similar_apps():
    index = request.args.get("index", get_default_index())
    num_matches = request.args.get("n", get_default_num_matches())
    mirror_x = request.args.get("mirror", False)
    flip_y = request.args.get("flip", False)
    similar_apps = index_to_similar_apps(
        index, num_matches, mirror_x=bool(mirror_x), flip_y=bool(flip_y)
    )
    return jsonify(similar_apps)


@app.route("/index_from_id")
def get_index_from_id():
    id = request.args.get("id", get_default_id())
    index = id_to_index(id)
    return jsonify(index)


@app.route("/name_from_id")
def get_name_from_id():
    id = request.args.get("id", get_default_id())
    name = id_to_name(id)
    return jsonify(name)


@app.route("/app_from_id")
def get_app_from_id():
    id = request.args.get("id", get_default_id())
    app = id_to_app(id)
    return jsonify(app)


@app.route("/similar_apps_from_id")
def get_similar_apps_from_id():
    id = request.args.get("id", get_default_id())
    num_matches = request.args.get("n", get_default_num_matches())
    mirror_x = request.args.get("mirror", False)
    flip_y = request.args.get("flip", False)
    similar_apps = id_to_similar_apps(
        id, num_matches, mirror_x=bool(mirror_x), flip_y=bool(flip_y)
    )
    return jsonify(similar_apps)


@app.route("/index_from_name")
def get_index_from_name():
    name = request.args.get("name", get_default_name())
    index = name_to_index(name)
    return jsonify(index)


@app.route("/id_from_name")
def get_id_from_name():
    name = request.args.get("name", get_default_name())
    id = name_to_id(name)
    return jsonify(id)


@app.route("/app_from_name")
def get_app_from_name():
    name = request.args.get("name", get_default_name())
    app = name_to_app(name)
    return jsonify(app)


@app.route("/similar_apps_from_name")
def get_similar_apps_from_name():
    name = request.args.get("name", get_default_name())
    num_matches = request.args.get("n", get_default_num_matches())
    mirror_x = request.args.get("mirror", False)
    flip_y = request.args.get("flip", False)
    similar_apps = name_to_similar_apps(
        name, num_matches, mirror_x=bool(mirror_x), flip_y=bool(flip_y)
    )
    return jsonify(similar_apps)


@app.route("/render/")
@app.route("/render/<id>/")
@app.route("/render/<id>/<num_matches>")
def render(
    id=None,
    num_matches=None,
    link_to_steam_store=False,
    verbose=True,
    mirror_x=None,
    flip_y=None,
):
    if mirror_x is None:
        mirror_x = request.args.get("mirror", False)
    if flip_y is None:
        flip_y = request.args.get("flip", False)

    if id is None:
        id = get_random_id()

    if num_matches is None:
        num_matches = get_default_num_matches_to_display()

    query_app, similar_apps = prepare_data_for_rendering(
        id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        mirror_x=mirror_x,
        flip_y=flip_y,
    )

    return render_template(
        "output.html",
        query=query_app,
        similar_apps=similar_apps,
        width=get_default_width(),
        height=get_default_height(),
        verbose=verbose,
    )


@app.route("/render_x/")
@app.route("/render_x/<id>/")
@app.route("/render_x/<id>/<num_matches>")
def render_x(id=None, num_matches=None, link_to_steam_store=False, verbose=True):
    return render(
        id=id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        verbose=verbose,
        mirror_x=True,
        flip_y=False,
    )


@app.route("/render_y/")
@app.route("/render_y/<id>/")
@app.route("/render_y/<id>/<num_matches>")
def render_y(id=None, num_matches=None, link_to_steam_store=False, verbose=True):
    return render(
        id=id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        verbose=verbose,
        mirror_x=False,
        flip_y=True,
    )


@app.route("/render_xy/")
@app.route("/render_xy/<id>/")
@app.route("/render_xy/<id>/<num_matches>")
def render_xy(id=None, num_matches=None, link_to_steam_store=False, verbose=True):
    return render(
        id=id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        verbose=verbose,
        mirror_x=True,
        flip_y=True,
    )


@app.route("/store/")
@app.route("/store/<id>/")
@app.route("/store/<id>/<num_matches>")
def store(
    id=None,
    num_matches=None,
    link_to_steam_store=True,
    verbose=True,
    mirror_x=None,
    flip_y=None,
):
    if mirror_x is None:
        mirror_x = request.args.get("mirror", False)
    if flip_y is None:
        flip_y = request.args.get("flip", False)
    return render(
        id=id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        verbose=verbose,
        mirror_x=mirror_x,
        flip_y=flip_y,
    )


@app.route("/store_x/")
@app.route("/store_x/<id>/")
@app.route("/store_x/<id>/<num_matches>")
def store_x(id=None, num_matches=None, link_to_steam_store=False, verbose=True):
    return store(
        id=id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        verbose=verbose,
        mirror_x=True,
        flip_y=False,
    )


@app.route("/store_y/")
@app.route("/store_y/<id>/")
@app.route("/store_y/<id>/<num_matches>")
def store_y(id=None, num_matches=None, link_to_steam_store=False, verbose=True):
    return store(
        id=id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        verbose=verbose,
        mirror_x=False,
        flip_y=True,
    )


@app.route("/store_xy/")
@app.route("/store_xy/<id>/")
@app.route("/store_xy/<id>/<num_matches>")
def store_xy(id=None, num_matches=None, link_to_steam_store=False, verbose=True):
    return store(
        id=id,
        num_matches=num_matches,
        link_to_steam_store=link_to_steam_store,
        verbose=verbose,
        mirror_x=True,
        flip_y=True,
    )
