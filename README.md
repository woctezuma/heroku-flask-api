# Heroku Flask API

Deploy an API built with Flask on Heroku.

## Usage

To run locally:
```bash
set FLASK_APP=app/app
flask run
```

To deploy:
```bash
heroku login
heroku create
git push heroku main
```

## References

- [`heroku-clip`][heroku-app-CLIP]: deploy an app built with Streamlit on Heroku.

<!-- Definitions -->

[heroku-app-CLIP]: <https://github.com/woctezuma/heroku-clip>

