# Heroku Flask API

Deploy an API built with Flask on Heroku.

## Data

Data consists of images from the Steam store (~30k games) downloaded [on January 9, 2021][data-snapshot].

## Usage

To run locally:
```bash
python run.py
```

To deploy:
```bash
heroku login
heroku create
git push heroku main
```

## Web App

The web app can be accessed at this URL:

> https://damp-brushlands-51855.herokuapp.com/

To ask for results about Cyberpunk 2077, you have to append the appID (`1091500`) at the end of the `/render/` endpoint:

> https://damp-brushlands-51855.herokuapp.com/render/1091500/

Or you can try your luck with a random game. **Caveat: some Steam games can be offensive!**

> https://damp-brushlands-51855.herokuapp.com/render/

## References

- [`steam-CLIP`][banner-repository-CLIP]: retrieve games with similar banners, using OpenAI's CLIP (resolution 224),
- [`heroku-flask-api`][my-flask-API]: serve the matching results through an API built with Flask on Heroku,
- [`heroku-clip`][heroku-app-CLIP]: deploy an app built with Streamlit on Heroku.

<!-- Definitions -->

[data-snapshot]: <https://github.com/woctezuma/steam-store-snapshots>
[banner-repository-CLIP]: <https://github.com/woctezuma/steam-CLIP>
[my-flask-API]: <https://github.com/woctezuma/heroku-flask-api>
[heroku-app-CLIP]: <https://github.com/woctezuma/heroku-clip>
