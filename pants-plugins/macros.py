def docker_image_gha(name: str, **kwargs) -> None:
    """
    A macro to create a Docker image that caches to Github Actions cache, by default.
    """
    cache_from: list[dict[str, str]] = kwargs.pop(
        "cache_from", [{"type": "gha", "scope": name}]
    )
    cache_to: dict[str, str] = kwargs.pop(
        "cache_to", {"type": "gha", "mode": "max", "scope": name}
    )

    docker_image(  # noqa: F821
        name=name,
        cache_from=cache_from,
        cache_to=cache_to,
        **kwargs,
    )


def docker_image_ghcr(name: str, **kwargs) -> None:
    """
    A macro to create a Docker image that caches to Github Container Registry, by default.
    """

    cache_from, cache_to = _default_ghcr_cache(name)
    cache_from = kwargs.pop(
        "cache_from",
        cache_from,
    )
    cache_to = kwargs.pop(
        "cache_to",
        cache_to,
    )

    docker_image(  # noqa: F821
        name=f"{name}-ghcr",
        cache_from=cache_from,
        cache_to=cache_to,
        **kwargs,
    )


def _default_ghcr_cache(
    target_name: str,
) -> tuple[list[dict[str, str]], Optional[dict[str, str]]]:  # noqa: F821
    """
    Using Github Actions default env vars - create a cache_from, and cache_to taking
    into account branches and PRs for better cache locality.

    https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables
    """
    # Need to specify this, because Pants doesn't reconcile `@ghcr` in the cache details
    # https://github.com/pantsbuild/pants/issues/21082
    REGISTRY = "ghcr.io/robotpajamas"
    REPO_NAME = "dockerfiles"

    # These are always populated in a PR, but not in a direct push
    head_ref: str = env("GITHUB_HEAD_REF", "")  # noqa: F821
    base_ref: str = env("GITHUB_BASE_REF", "")  # noqa: F821

    # This is always populated, but in a PR it is: <pr_number>/merge - if we're in a PR, ignore
    ref_name: str = env("GITHUB_REF_NAME", "") if not head_ref else ""  # noqa: F821

    cache_from_refs = [
        f"{REGISTRY}/{REPO_NAME}/{target_name}/build-cache:{tag.replace('/', '-')}"
        for tag in [head_ref, base_ref, ref_name, "main"]
        if tag
    ]
    cache_from = [{"type": "registry", "ref": ref} for ref in cache_from_refs]

    # Cache to the head_ref only in a PR, otherwise, cache to the ref_name
    resolved_ref = head_ref or ref_name
    cache_to = None
    if resolved_ref:
        cache_to = {
            "type": "registry",
            "mode": "max",
            "ref": f"{REGISTRY}/{REPO_NAME}/{target_name}/build-cache:{resolved_ref.replace('/', '-')}",
        }

    return cache_from, cache_to
