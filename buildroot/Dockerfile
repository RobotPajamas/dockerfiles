FROM robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07 as builder

LABEL maintainer="suresh@robotpajamas.com"

ARG BUILDROOT_VERSION=buildroot-2022.05

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

USER root
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash=5.1-2+deb11u1 \
    bc=1.07.1-2+b2 \
    binutils=2.35.2-2 \
    cpio=2.13+dfsg-7.1~deb11u1 \
    build-essential=12.9 \
    bzip2=1.0.8-4 \
    ca-certificates=20210119 \
    file=1:5.39-3+deb11u1 \
    g++=4:10.2.1-1 \
    gcc=4:10.2.1-1 \
    git=1:2.30.2-1+deb11u2 \
    libncurses5-dev=6.2+20201114-2+deb11u2 \
    make=4.3-4.1 \
    nano=5.4-2+deb11u2 \
    patch=2.7.6-7 \
    perl=5.32.1-4+deb11u3 \
    python3=3.9.2-3 \
    rsync=3.2.3-4+deb11u1 \
    sed=4.7-1 \
    tar=1.34+dfsg-1+deb11u1 \
    unzip=6.0-26+deb11u1 \
    wget=1.21-1+deb11u1 \
    && rm -rf /var/lib/apt/lists/* \
    && wget --progress=dot:giga -O- https://buildroot.org/downloads/${BUILDROOT_VERSION}.tar.gz | tar -xvz \
    && mv /${BUILDROOT_VERSION} /buildroot \
    && mkdir -p /app /app/cache /app/src /app/output \
    && chown -R armothy:armoire /app /buildroot

USER armothy

ENV ARCH="arm"
ENV BR2_CCACHE_DIR="/app/cache/ccache"
ENV BR2_DL_DIR="/app/cache/dl"
ENV CCACHE_DIR="/app/cache/ccache"

WORKDIR /app/output

CMD ["bash"]
