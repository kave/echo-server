# ECHO Server Extradinaire

# Local Development
### Dependencies
- Python37
- `brew install pyenv`
- `pyenv install 3.7.0`
- `brew install pipenv`
    - `pipenv --python=3.7`
    - `pipenv install`
- Create a `config/.env` file with contents:
```
PORT=8888
```

### Run server
`pipenv run python echo.py`
 - by default it will listen on port `8888`
