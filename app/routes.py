from flask import jsonify, request, render_template

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
    similar_apps = index_to_similar_apps(index, num_matches)
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
    similar_apps = id_to_similar_apps(id, num_matches)
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
    similar_apps = name_to_similar_apps(name, num_matches)
    return jsonify(similar_apps)


@app.route("/render/")
@app.route("/render/<id>/")
@app.route("/render/<id>/<num_matches>")
def render(id=None, num_matches=None, link_to_steam_store=False):
    if id is None:
        id = get_random_id()

    if num_matches is None:
        num_matches = get_default_num_matches_to_display()

    query_app, similar_apps = prepare_data_for_rendering(
        id, num_matches=num_matches, link_to_steam_store=link_to_steam_store
    )

    return render_template(
        "output.html",
        query=query_app,
        similar_apps=similar_apps,
        width=get_default_width(),
        height=get_default_height(),
    )


@app.route("/store/")
@app.route("/store/<id>/")
@app.route("/store/<id>/<num_matches>")
def store(id=None, num_matches=None, link_to_steam_store=True):
    return render(
        id=id, num_matches=num_matches, link_to_steam_store=link_to_steam_store
    )
