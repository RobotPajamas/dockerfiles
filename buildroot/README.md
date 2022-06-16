# Buildroot

## Usage

When using these dev envs, I tend to just jump into bash directly and use the container like it's a VM, as I find it easier. 

`docker -v $(pwd):/app -it robotpajamas/buildroot:2022.05 bash`

However, they can also be used externally (e.g. when calling from a script as part of automation)

`docker -v $(pwd):/app -it robotpajamas/buildroot:2022.05 make O=/app/output -C /buildroot beaglebone_defconfig && make`

There may be some permissions issues here, if the volume doesn't match what is expected.

## Important ENV variables

```bash
ARCH="arm"
BR2_CCACHE_DIR="/app/cache/ccache"
BR2_DL_DIR="/app/cache/dl"
CCACHE_DIR="/app/cache/ccache"
```

## Defconfig variables

In order to use the built-in toolchain, ensure the following is in your defconfig:

```bash
BR2_TOOLCHAIN_EXTERNAL=y
BR2_TOOLCHAIN_EXTERNAL_PREINSTALLED=y
BR2_TOOLCHAIN_EXTERNAL_PATH="/gcc-arm"
```

## TODOs

- Setup a BR2_EXTERNAL_TREE example
