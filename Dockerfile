FROM python:3.8-slim

COPY pyproject.toml poetry.lock ./

RUN pip --no-cache-dir install poetry poetry-setup \
    && poetry config virtualenvs.create false \
    && poetry install \
    && pip uninstall poetry -y \
    && rm -rf ~/.config/pypoetry

COPY . .

CMD python echo.py