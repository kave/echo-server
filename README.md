# ECHO Server Extradinaire

Logs requests that are sent to the server


# Local Development
### Dependencies
- Python37 && poetry
- `poetry install`
- Create a `config/.env` file with contents:
  - `PORT=8888`

### Run server
`poetry run python echo.py`
OR
```
docker build . -t echo-server
docker run -it -p 8888:8888 echo-server
```
## Example GET request
`curl localhost:8888`

## Example POST request
`curl localhost:8888`

## Docker publishing
```
docker tag echo-server:latest etapau/echo-server:latest
docker push etapau/echo-server:latest
```