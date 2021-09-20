# Buildroot

## Usage

When using these dev envs, I tend to just jump into bash directly and use the container like it's a VM, as I find it easier. 

`docker -v $(pwd):/app -it robotpajamas/buildroot:2021.02.5 bash`

However, they can also be used externally (e.g. when calling from a script as part of automation)

`docker -v $(pwd):/app -it robotpajamas/buildroot:2021.02.5 make O=/app/output -C /buildroot beaglebone_defconfig && make`

There may be some permissions issues here, if the volume doesn't match what is expected.

## Important ENV variables

```bash
ARCH="arm"
BR2_CCACHE_DIR="/app/cache/ccache"
BR2_DL_DIR="/app/cache/dl"
```
## TODOs

- Can't get buildroot to use the pre-installed toolchain - otherwise could use robotpajamas/gcc-arm-linux-gnueabihf:10.3-2021.07
- Buildroot has a gcc10 problem, so need to use gcc8 or gcc9 (hence using Buster instead of Bullseye)
- Setup a BR2_EXTERNAL_TREE example
