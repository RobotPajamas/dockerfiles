#! /bin/sh

# Working directory is /app (i.e. u-boot directory)

# Apply u-boot fragment to configuration
if test -f "/u-boot.patch"; then
    echo "***** Applying patch at /u-boot.patch *****"
    git apply /u-boot.patch
fi

echo "***** Making defconfig: ${DEFCONFIG} *****"
KBUILD_VERBOSE=1 make ${DEFCONFIG}

# Apply u-boot patch, if present
if test -f "/u-boot.fragment"; then
    echo "***** Applying fragment at /u-boot.fragment *****"
    /app/scripts/kconfig/merge_config.sh /app/.config /u-boot.fragment
fi

exec "$@"
