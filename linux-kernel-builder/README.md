# linux-kernel-builder

```bash
docker run -v kernel54106:/app -v /tmp/ccache:/ccache -it robotpajamas/linux-kernel-builder:latest bash

make omap2plus_defconfig
make
```