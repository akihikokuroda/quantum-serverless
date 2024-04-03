FROM python:3.9.16-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get install  --no-install-recommends -y iptables=1.8.2-4 sudo=1.8.27-1+deb10u6 &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip==24.0 --no-cache-dir

RUN adduser --disabled-password --gecos '' worker
RUN adduser worker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER worker
WORKDIR /home/worker

RUN pip install headerparser==0.5.1 certifi==2024.2.2 requests==2.31.0 --no-cache-dir

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker proxy/proxy .
RUN chmod +x /home/worker/entrypoint.sh

EXPOSE 8443
ENTRYPOINT ["/home/worker/entrypoint.sh"]