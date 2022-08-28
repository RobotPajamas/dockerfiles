# u-boot-builder

A development environment containing an ARM gcc toolchain which can build u-boot for ARM devices.

## Usage

Given some input paramters, this container will automatically download u-boot, apply patches, and use configuration fragments to setup and then build u-boot.

Below is the typical, non-interactive build command.

```bash
docker run --rm \
  -e DEFCONFIG=am335x_evm_defconfig \
  -v uboot-2022.07:/app \
  -v ccache:/ccache \
  -v $(pwd)/mykconfig.fragment:/u-boot.fragment:ro \
  -v $(pwd)/mygit.patch:/u-boot.patch:ro \
  robotpajamas/u-boot-builder:2022.07
```

- `-e DEFCONFIG=am335x_evm_defconfig` is an environment variable specifying which defconfig to use, it defaults to `qemu_arm_defconfig`.
- `-v uboot-2022.07:/app` is a named volume to store u-boot sources, and to persist modifications when using this container as a develop environment. Additionally, using a named volume instead of a bind mount skips permission and performance problems on non-Linux host OSes.
- `-v ccache:/ccache` is a named volume to store `ccache` objects.
- `-v $(pwd)/mykconfig.fragment:/u-boot.fragment:ro` is an optional volume mapping a `Kconfig` fragment, which is applied via `scripts/kconfig/merge_configs.sh` after making the u-boot defconfig.
- `-v $(pwd)/mygit.patch:/u-boot.patch:ro` is an optional volume mapping a git patch file, which is applied via `git apply u-boot.patch`.

The `entrypoint` for this container automatically attempts to apply patches, `make` the defconfig, and then apply the configuration fragment on each invocation. The default `cmd` runs `make`.

In order to run this as an interactive container, and to manually run the `make` process - you can use something like the following:

```bash
docker run --rm -it \
  -e DEFCONFIG=am335x_evm_defconfig \
  -v uboot-2022.07:/app \
  -v ccache:/ccache \
  robotpajamas/u-boot-builder:2022.07 bash
```

## Snippets

### Configuration Fragment

```bash
# mykconfig.fragment

CONFIG_SYS_REDUNDAND_ENVIRONMENT=y
CONFIG_ENV_SIZE=0x8000
CONFIG_ENV_OFFSET=0x100000
CONFIG_ENV_OFFSET_REDUND=0x200000
```

### Git Patch

```bash
diff --git a/README b/README
index b7ab6e50..b36b6e99 100644
--- a/README
+++ b/README
@@ -1,6 +1,6 @@
 # SPDX-License-Identifier: GPL-2.0+
 #
-# (C) Copyright 2000 - 2013
+# (C) Copyright 2000 - 2022
 # Wolfgang Denk, DENX Software Engineering, wd@denx.de.

 Summary:
```

## TODO

- These should probably be re-done with the `--mount` syntax, as it's clearer for documentation purposes. `-v` is a shortcut.
- Check if `git apply` can be ignored once applied, or if the error can be ignored
