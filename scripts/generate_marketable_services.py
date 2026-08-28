#!/usr/bin/env python3
"""Generate the public catalogue from explicitly releasable MPG service records."""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "registry" / "services.json"
OUTPUT_PATH = ROOT / "generated" / "marketable-services.md"
GENERATED_MARKER = (
    "<!-- GENERATED FILE: do not edit directly. "
    "Source: registry/services.json via scripts/generate_marketable_services.py -->"
)


def markdown_safe_text(value: str) -> str:
    """Render registry text as one inert Markdown paragraph/heading fragment."""
    escaped = html.escape(" ".join(value.split()), quote=False)
    for character in "\\`*_{}[]()#+.!|>-":
        escaped = escaped.replace(character, f"\\{character}")
    return escaped


def load_registry(path: Path = SOURCE_PATH) -> dict[str, Any]:
    """Load the service registry or raise a clear data error."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Service registry not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(data, dict) or not isinstance(data.get("services"), list):
        raise ValueError("Service registry must be an object containing a 'services' array.")
    return data


def select_marketable_services(registry: dict[str, Any]) -> list[dict[str, Any]]:
    """Return only services that satisfy every public publication predicate."""
    selected = [
        service
        for service in registry["services"]
        if isinstance(service, dict)
        and service.get("lifecycleStatus") == "ACTIVE"
        and service.get("marketingApproved") is True
        and service.get("publiclyMarketable") is True
    ]
    def sort_key(service: dict[str, Any]) -> tuple[int, str]:
        priority = service.get("priority")
        safe_priority = priority if type(priority) is int else 10**9
        service_id = service.get("id")
        return safe_priority, service_id if isinstance(service_id, str) else ""

    return sorted(selected, key=sort_key)


def render_catalogue(registry: dict[str, Any]) -> str:
    """Render a deterministic, public-safe Markdown catalogue."""
    metadata = registry.get("metadata")
    source_date_value = metadata.get("lastUpdated", "UNKNOWN") if isinstance(metadata, dict) else "UNKNOWN"
    source_date = markdown_safe_text(str(source_date_value))
    services = select_marketable_services(registry)
    lines = [
        GENERATED_MARKER,
        "",
        "# MPG Marketable Services",
        "",
        f"Source registry date: {source_date}",
        "",
        "Publication rule: a service appears here only when its lifecycle status is "
        "`ACTIVE` and owner marketing approval is `true`; its derived "
        "`publiclyMarketable` flag must therefore also be `true`.",
        "",
    ]

    if not services:
        lines.extend(
            [
                "**No services are currently approved for automatic public publication.**",
                "",
                "This is a valid governance state, not a validation failure.",
            ]
        )
    else:
        for service in services:
            public_fields = ("id", "name", "division", "targetCustomer", "description")
            missing = [
                field
                for field in public_fields
                if not isinstance(service.get(field), str) or not service[field].strip()
            ]
            if missing:
                identifier = service.get("id", "UNKNOWN")
                raise ValueError(
                    f"Marketable service {identifier!r} has missing or malformed public fields: "
                    + ", ".join(missing)
                )
            safe_name = markdown_safe_text(service["name"])
            safe_id = markdown_safe_text(service["id"])
            safe_division = markdown_safe_text(service["division"])
            safe_customer = markdown_safe_text(service["targetCustomer"])
            safe_description = markdown_safe_text(service["description"])
            lines.extend(
                [
                    f"## {safe_name}",
                    "",
                    f"- Service ID: {safe_id}",
                    f"- Division: {safe_division}",
                    f"- Intended customer: {safe_customer}",
                    "",
                    safe_description,
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def write_text_lf(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the committed generated catalogue is missing or stale.",
    )
    args = parser.parse_args(argv)

    try:
        registry = load_registry()
        expected = render_catalogue(registry)
    except ValueError as exc:
        print(f"Catalogue generation failed: {exc}", file=sys.stderr)
        return 1

    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"Catalogue check failed: missing {OUTPUT_PATH.relative_to(ROOT)}", file=sys.stderr)
            return 1
        actual = OUTPUT_PATH.read_text(encoding="utf-8")
        if actual != expected:
            print(
                "Catalogue check failed: generated/marketable-services.md is stale. "
                "Run python scripts/generate_marketable_services.py.",
                file=sys.stderr,
            )
            return 1
        print("Marketable service catalogue is current.")
        return 0

    write_text_lf(OUTPUT_PATH, expected)
    count = len(select_marketable_services(registry))
    print(
        f"Generated {OUTPUT_PATH.relative_to(ROOT)} with {count} market-approved "
        f"service{'s' if count != 1 else ''}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
