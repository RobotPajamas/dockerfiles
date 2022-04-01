FROM robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07 as builder

LABEL maintainer="suresh@robotpajamas.com"

ARG UBOOT_TAG=v2021.07

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

USER root
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash \
    bison \
    build-essential \
    ca-certificates \
    flex \
    git \
    make \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /app \
    && git clone --depth 1 --branch ${UBOOT_TAG} https://github.com/u-boot/u-boot.git /app \
    && chown -R armothy:armoire /app

USER armothy
WORKDIR /app

CMD ["bash"]