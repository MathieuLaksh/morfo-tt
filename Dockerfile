FROM --platform=linux/amd64 python:3.12-slim-bookworm AS build-base
RUN apt-get update --fix-missing && \
    apt-get install -y build-essential

ENV POETRY_VERSION=1.8.3
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install poetry and setup venv
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv --copies $VIRTUAL_ENV

# Take requirements and install them
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi --only main

FROM --platform=linux/amd64 python:3.12-slim-bookworm as base
RUN apt-get update --fix-missing
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
SHELL ["/bin/bash", "-c"]


FROM base AS runtime
COPY --from=build-base /venv /venv
WORKDIR /morfo_tt
CMD [ "python main.py" ]



