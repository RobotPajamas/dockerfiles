def docker_image_gha(name: str, **kwargs) -> None:
    """
    A macro to create a Docker image that caches to Github Actions, by default.
    """
    # cache_from = kwargs.pop("cache_from", {"type": "gha", "scope": name})
    # cache_to = kwargs.pop("cache_to", {"type": "gha", "mode": "max", "scope": name})

    # docker_image(  # noqa: F821
    #     name=name,
    #     cache_from=cache_from,
    #     cache_to=cache_to,
    #     **kwargs,
    # )

    cache_from = kwargs.pop(
        "cache_from",
        {
            "type": "registry",
            "ref": f"ghcr.io/robotpajamas/dockerfiles/build-cache:{name}",
        },
    )
    cache_to = kwargs.pop(
        "cache_to",
        {
            "type": "registry",
            "mode": "max",
            "ref": f"ghcr.io/robotpajamas/dockerfiles/build-cache:{name}",
        },
    )

    docker_image(  # noqa: F821
        name=f"{name}-ghcr",
        cache_from=cache_from,
        cache_to=cache_to,
        **kwargs,
    )
