# u-boot-builder

## TODO

- Notes: Use a volume to host the git repo + changes, so it's not accidentally lost on container removal.
Optionally bind mount `ccache`, so that it can be shared across builds or containers - and probably put it in a tmp folder so the OS can manage it.
- These should probably be re-done with the `--mount` syntax, as it's clearer for documentation purposes. `-v` is a shortcut.
- Confirm this runs with `Podman` as well.
- Test by passing in a bash command
- Show git diff/patch example


```bash
docker run -v uboot202107:/app -v /tmp/ccache:/ccache -it uboot:latest bash

make am335x_evm_defconfig
make
```