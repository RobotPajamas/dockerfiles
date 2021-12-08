# TODO: Can't get buildroot to use the pre-installed toolchain - would save a lot of time in the build
#FROM robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07 as builder

# TODO: Cannot inherit from gcc-arm-linux-gnueabihf because there is a buildroot + gcc10 problem
# Need to use Buster with gcc8 or gcc9
FROM debian:buster-20210902-slim

LABEL maintainer="suresh@robotpajamas.com"

ARG BUILDROOT_VERSION=buildroot-2021.11

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

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
    && mkdir /app /app/cache /app/src /app/output \
    && groupadd -r armoire \
    && useradd --no-log-init -u 1000 -r -g armoire armothy \
    && chown -R armothy:armoire /app /buildroot

USER armothy

ENV ARCH="arm"
ENV BR2_CCACHE_DIR="/app/cache/ccache"
ENV BR2_DL_DIR="/app/cache/dl"

WORKDIR /app/output

CMD ["bash"]
