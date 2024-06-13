FROM debian:bullseye-20210902-slim as builder

LABEL maintainer="suresh@robotpajamas.com"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash=5.1-2+deb11u1 \
    ca-certificates=20210119 \
    tar=1.34+dfsg-1+deb11u1 \
    wget=1.21-1+deb11u1 \
    xz-utils=5.2.5-2.1~deb11u1 \
    && rm -rf /var/lib/apt/lists/* \
    && wget --progress=dot:giga -O- https://developer.arm.com/-/media/Files/downloads/gnu-a/10.3-2021.07/binrel/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf.tar.xz | tar -xvJ


FROM debian:bullseye-20210902-slim

RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash=5.1-2+deb11u1 \
    ccache=4.2-1 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r armoire \
    && useradd --no-log-init -u 1000 -r -g armoire armothy

USER armothy
COPY --from=builder --chown=armothy:armoire /gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf /gcc-arm

ENV CCACHE_DIR="/ccache"
ENV PATH="/gcc-arm/bin:$PATH"

ENV ARCH="arm"
ENV CROSS_COMPILE="ccache /gcc-arm/bin/arm-none-linux-gnueabihf-"

CMD ["bash"]
