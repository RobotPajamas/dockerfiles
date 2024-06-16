def docker_image_gha(name: str, **kwargs) -> None:
    """
    A macro to create a Docker image that caches to Github Actions, by default.
    """
    cache_from = kwargs.pop("cache_from", {"type": "gha", "scope": name})
    cache_to = kwargs.pop("cache_to", {"type": "gha", "mode": "max", "scope": name})

    docker_image(  # noqa: F821
        name=name,
        cache_from=cache_from,
        cache_to=cache_to,
        **kwargs,
    )

    cache_from = kwargs.pop("cache_from", {"type": "registry", "ref": "robotpajamas/dockerfiles-build-cache:my-branch"})
    cache_to = kwargs.pop("cache_to", {"type": "registry", "mode": "max", "ref": "robotpajamas/dockerfiles-build-cache:my-branch"})

    docker_image(  # noqa: F821
        name=name,
        cache_from=cache_from,
        cache_to=cache_to,
        **kwargs,
    )
