FROM robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07 as builder

LABEL maintainer="suresh@robotpajamas.com"

ARG BUILDROOT_VERSION=buildroot-2021.11.1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

USER root
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash \
    bc \
    binutils \
    cpio \
    build-essential \
    bzip2 \
    ca-certificates \
    file \
    gcc \
    g++ \
    git \
    libncurses5-dev \
    make \
    patch \
    perl \
    python3 \
    rsync \
    sed \
    tar \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && wget -O- https://buildroot.org/downloads/${BUILDROOT_VERSION}.tar.gz | tar -xvz \
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
