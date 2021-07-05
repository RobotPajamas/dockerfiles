FROM ubuntu:18.04 as builder

LABEL maintainer="suresh@robotpajamas.com"

SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

# hadolint ignore=DL3008
RUN apt-get update \
   && apt-get install -y -qq --no-install-recommends \
      ca-certificates \
      git \
      tar \
      wget \
      xz-utils

WORKDIR /gcc

RUN wget https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf.tar.xz
RUN tar -Jxvf gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf.tar.xz
RUN rm gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf.tar.xz

RUN wget https://developer.arm.com/-/media/Files/downloads/gnu-a/9.2-2019.12/binrel/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz
RUN tar -Jxvf gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz
RUN rm gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu.tar.xz

RUN git clone git://arago-project.org/git/projects/oe-layersetup.git /arago


FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=non-interactive
WORKDIR /arago

# Pull required building packages and configure timezone and locale to avoid Python complaints
# hadolint ignore=DL3008
RUN apt-get update \
   && apt-get install -y -qq --no-install-recommends \
      build-essential \
      ca-certificates \
      chrpath \
      cpio \
      diffstat \
      file \
      gawk \
      git \
      lib32ncurses5 \
      lib32z1 \
      libc6-i386 \
      libstdc++6-i386-cross \
      locales \
      python \
      python3 \
      python3-distutils \
      tar \
      texinfo \
      wget \
   && rm -rf /var/lib/apt/lists/* \
   && echo 'LANG="en_US.UTF-8"'>/etc/default/locale \
   && locale-gen en en_US en_US.UTF-8 \
   && dpkg-reconfigure --frontend=noninteractive locales \
   && update-locale LANG=en_US.UTF-8 \
   && echo "dash dash/sh boolean false" | debconf-set-selections \
   && dpkg-reconfigure -p critical dash \
   && groupadd -r bitbakery \
   && useradd --no-log-init -u 1000 -r -g bitbakery bitbaker \
   && chown bitbaker:bitbakery /arago

USER bitbaker
COPY --from=builder --chown=bitbaker:bitbakery /gcc /gcc
COPY --from=builder --chown=bitbaker:bitbakery /arago /arago

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Required for bitbake compilation
ENV TOOLCHAIN_PATH_ARMV7=/gcc/gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf
ENV TOOLCHAIN_PATH_ARMV8=/gcc/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu
ENV MACHINE=am335x-evm

CMD ["bash"]
