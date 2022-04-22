FROM robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07 as builder

LABEL maintainer="suresh@robotpajamas.com"

ARG LINUX_TAG=v5.4.106

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

USER root
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash \
    bc \
    bison \
    build-essential \
    flex \
    git \
    libncurses5-dev \
    libssl-dev \
    make \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /app \
    && mkdir -p /ccache \
    && git clone --depth 1 --branch ${LINUX_TAG} git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git /app \
    && chown -R armothy:armoire /app \
    && chown -R armothy:armoire /ccache

USER armothy
WORKDIR /app

CMD ["bash"]
