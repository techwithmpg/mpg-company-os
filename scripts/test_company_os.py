#!/usr/bin/env python3
"""Regression tests for MPG Company OS release and publication controls."""

from __future__ import annotations

import copy
import json
import unittest

import validate_company_os as validator
from generate_marketable_services import render_catalogue


def load_registries() -> dict[str, dict]:
    return {
        name: json.loads(path.read_text(encoding="utf-8"))
        for name, path in validator.REQUIRED_REGISTRIES.items()
    }


def validation_context(registries: dict[str, dict]) -> tuple[dict[str, set[str]], dict[str, dict[str, dict]]]:
    collections = {
        name: registry[name]
        for name, registry in registries.items()
    }
    known_ids = {
        name: {record["id"] for record in records}
        for name, records in collections.items()
    }
    records_by_id = {
        name: {record["id"]: record for record in records}
        for name, records in collections.items()
    }
    return known_ids, records_by_id


class GovernanceRegressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registries = load_registries()
        self.known_ids, self.records_by_id = validation_context(self.registries)
        self.website = copy.deepcopy(self.registries["services"]["services"][0])

    def validate_service(self, service: dict) -> list[str]:
        result = validator.Validation()
        validator.validate_service(service, 0, self.known_ids, self.records_by_id, result)
        return result.errors

    def test_malformed_service_id_is_rejected(self) -> None:
        self.website["id"] = "malformed service id"
        errors = self.validate_service(self.website)
        self.assertTrue(any("malformed id" in error for error in errors), errors)

    def test_unauthorized_active_service_is_rejected(self) -> None:
        self.website.update(
            lifecycleStatus="ACTIVE",
            marketingApproved=False,
            publiclyMarketable=False,
            marketApprovalDecision="NONE",
        )
        errors = self.validate_service(self.website)
        self.assertTrue(any("requires owner marketing approval" in error for error in errors), errors)
        self.assertTrue(any("market-approval decision" in error for error in errors), errors)

    def test_publication_flag_cannot_bypass_two_condition_gate(self) -> None:
        self.website["publiclyMarketable"] = True
        errors = self.validate_service(self.website)
        self.assertTrue(any("publiclyMarketable must equal" in error for error in errors), errors)

    def test_generated_catalogue_escapes_registry_text(self) -> None:
        registry = copy.deepcopy(self.registries["services"])
        service = registry["services"][0]
        service.update(
            lifecycleStatus="ACTIVE",
            marketingApproved=True,
            publiclyMarketable=True,
            name="<script>alert('unsafe')</script>",
        )
        rendered = render_catalogue(registry)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertNotIn("<script>", rendered)


if __name__ == "__main__":
    unittest.main()
