# Heroku Flask API

Deploy an API built with Flask on Heroku.

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

[banner-repository-CLIP]: <https://github.com/woctezuma/steam-CLIP>
[my-flask-API]: <https://github.com/woctezuma/heroku-flask-api>
[heroku-app-CLIP]: <https://github.com/woctezuma/heroku-clip>
