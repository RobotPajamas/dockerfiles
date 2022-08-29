FROM robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07 as builder

LABEL maintainer="suresh@robotpajamas.com"

ARG UBOOT_TAG=v2022.07

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

USER root
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash \
    bc \
    bison \
    build-essential \
    ca-certificates \
    flex \
    git \
    libncurses5-dev \
    libssl-dev \
    make \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /app \
    && mkdir -p /ccache \
    && git clone --depth 1 --branch ${UBOOT_TAG} https://github.com/u-boot/u-boot.git /app \
    && chown -R armothy:armoire /app \
    && chown -R armothy:armoire /ccache

USER armothy
WORKDIR /app

COPY docker-entrypoint.sh /
ENV DEFCONFIG="qemu_arm_defconfig"

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["make"]
