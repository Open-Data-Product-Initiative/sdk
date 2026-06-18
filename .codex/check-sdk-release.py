#!/usr/bin/env python3
"""Check the latest Open Data Products SDK release metadata."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path


PYPI_URL = "https://pypi.org/pypi/open-data-products/json"
GITHUB_LATEST_RELEASE_URL = (
    "https://api.github.com/repos/Open-Data-Product-Initiative/odp-agent-sdk/"
    "releases/latest"
)
OUTPUT_PATH = Path("sdk-release.json")


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "open-data-products-sdk-site-release-check",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.load(response)
    except (urllib.error.URLError, TimeoutError):
        if not shutil.which("curl"):
            raise
        result = subprocess.run(
            ["curl", "-fsSL", "-H", "Accept: application/json", url],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(result.stdout)


def build_snapshot() -> dict:
    pypi = fetch_json(PYPI_URL)
    github = fetch_json(GITHUB_LATEST_RELEASE_URL)
    pypi_version = pypi["info"]["version"]
    github_tag = github.get("tag_name") or ""
    normalized_github_version = github_tag.removeprefix("v")

    return {
        "package": "open-data-products",
        "version": pypi_version,
        "pypi_url": pypi["info"].get(
            "package_url", "https://pypi.org/project/open-data-products/"
        ),
        "github_repo": "Open-Data-Product-Initiative/odp-agent-sdk",
        "github_tag": github_tag,
        "github_url": github.get(
            "html_url",
            "https://github.com/Open-Data-Product-Initiative/odp-agent-sdk/releases",
        ),
        "versions_match": pypi_version == normalized_github_version,
        "checked_at": dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat(),
        "source_of_truth": "pypi",
        "consistency_check": "github_latest_release",
    }


def read_existing(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check PyPI and GitHub for the latest SDK release version."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help=f"Write the latest release metadata to {OUTPUT_PATH}.",
    )
    args = parser.parse_args()

    snapshot = build_snapshot()
    existing = read_existing(OUTPUT_PATH)
    old_version = existing.get("version") if existing else None

    if args.write:
        OUTPUT_PATH.write_text(
            json.dumps(snapshot, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(f"PyPI latest: {snapshot['version']}")
    print(f"GitHub latest: {snapshot['github_tag'] or 'missing'}")
    print(f"Versions match: {snapshot['versions_match']}")
    if old_version and old_version != snapshot["version"]:
        print(f"Version changed: {old_version} -> {snapshot['version']}")
    elif old_version:
        print(f"Stored version unchanged: {old_version}")
    else:
        print("No stored version existed.")

    if not snapshot["versions_match"]:
        print(
            "PyPI and GitHub latest release differ; update public copy only after "
            "checking the release state.",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
