# # setup server 

# # 1 : start docker kernal + python
# FROM python:3.11-slim-bullseye

# # 2 : ENV : show logs
# ENV PYTHONUNBUFFERED=1

# # 3 : update kernal + install dep
# RUN apt-get update && apt-get -y install gcc libpq-dev

# # 4: create project folder : kernal
# WORKDIR /app

# # 5: Copy requi
# COPY requirements.txt /app/requirements.txt

# # 6: install req
# RUN pip install -r /app/requirements.txt

# # 7: copy project code --> docker 
# COPY . /app/
FROM python:3.13.3-slim-bullseye AS builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc gettext libpq-dev python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && pip cache purge


########################################################################################################################
FROM python:3.13.3-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

RUN apt-get update \
    && apt-get install -y gettext libpq-dev weasyprint && rm -rf /var/lib/apt/lists/* \
    && groupadd -r django \
    && useradd -r -g django -m django \
    && install -d -m 0755 -o django -g django /app/backend/staticfiles \
    && install -d -m 0755 -o django -g django /app/backend/media

WORKDIR /app

RUN chown -R django:django /app \
    && chown -R django:django /app/backend \
    && chown -R django:django /app/backend/staticfiles \
    && chown -R django:django /app/backend/media \
    && chown -R django:django /tmp

USER django

WORKDIR /app/backend
COPY . /app/backend

EXPOSE $PORT

# CMD ["sh", "-c", "find . -path '*/__pycache__/*pyc' -delete \
#     && find . -path '*/__pycache__' -delete \
#     && python manage.py collectstatic --noinput || echo '[!] Failed to collect static files!\n' \
#     && python manage.py check || echo '[!] Failed to check database!\n' \
#     && python manage.py makemigrations --noinput || echo '[!] Failed to make migrations!\n' \
#     && python manage.py migrate --noinput || echo '[!] Failed to migrate database!\n' \
#     && uvicorn project.asgi:application --host 0.0.0.0 --port ${PORT:-8000} --reload "]
    # && gunicorn project.wsgi:application -b 0.0.0.0:${PORT} --reload
    CMD ["sh", "-c", "find . -path '*/__pycache__/*pyc' -delete 2>/dev/null || true \
    && find . -path '*/__pycache__' -delete 2>/dev/null || true \
    && python manage.py collectstatic --noinput || echo '[!] Failed to collect static files!' \
    && python manage.py check || echo '[!] Failed to check database!' \
    && python manage.py makemigrations --noinput || echo '[!] Failed to make migrations!' \
    && python manage.py migrate --noinput || echo '[!] Failed to migrate database!' \
    && uvicorn project.asgi:application --host 0.0.0.0 --port ${PORT:-8000} --reload"]