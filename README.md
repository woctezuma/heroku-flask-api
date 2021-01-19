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

## References

- [`steam-CLIP`][banner-repository-CLIP]: retrieve games with similar banners, using OpenAI's CLIP (resolution 224),
- [`heroku-flask-api`][my-flask-API]: serve the matching results through an API built with Flask on Heroku,
- [`heroku-clip`][heroku-app-CLIP]: deploy an app built with Streamlit on Heroku.

<!-- Definitions -->

[data-snapshot]: <(https://github.com/woctezuma/steam-store-snapshots>
[banner-repository-CLIP]: <https://github.com/woctezuma/steam-CLIP>
[my-flask-API]: <https://github.com/woctezuma/heroku-flask-api>
[heroku-app-CLIP]: <https://github.com/woctezuma/heroku-clip>
