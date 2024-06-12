FROM robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07 as builder

LABEL maintainer="suresh@robotpajamas.com"

ARG LINUX_TAG=v5.15.46

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

USER root
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash=5.1-2+deb11u1 \
    bc=1.07.1-2+b2 \
    bison=2:3.7.5+dfsg-1 \
    build-essential=12.9 \
    ca-certificates=20210119 \
    flex=2.6.4-8 \
    git=1:2.30.2-1+deb11u2 \
    libmpc-dev=1.2.0-1 \
    libncurses5-dev=6.2+20201114-2+deb11u2 \
    libssl-dev=1.1.1w-0+deb11u1 \
    make=4.3-4.1 \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /app \
    && mkdir -p /ccache \
    && git clone --depth 1 --branch ${LINUX_TAG} git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git /app \
    && chown -R armothy:armoire /app \
    && chown -R armothy:armoire /ccache

USER armothy
WORKDIR /app

CMD ["bash"]
