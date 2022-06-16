# linux-kernel-builder

```bash
docker run --rm -v linux-5.10.121:/app -v ccache:/ccache -it robotpajamas/linux-kernel-builder:latest bash

make omap2plus_defconfig
make
```
