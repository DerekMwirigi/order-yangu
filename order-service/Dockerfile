FROM python:3.12-slim AS base

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY app/requirements/base.txt .

RUN /opt/venv/bin/pip install --upgrade pip setuptools
RUN /opt/venv/bin/pip install --no-cache-dir -r app/requirements/base.txt

RUN chmod +x /app/run_app.sh

# HEALTHCHECK CMD python -c "import urllib.request,os; urllib.request.urlopen(f'http://127.0.0.1:{os.environ.get("PORT","8080")}/livez').read()" || exit 1

CMD ["/app/run_app.sh"]

EXPOSE 8080

