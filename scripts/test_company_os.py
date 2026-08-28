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

    def service(self, service_id: str) -> dict:
        return next(
            service
            for service in self.registries["services"]["services"]
            if service["id"] == service_id
        )

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

    def test_commercial_sequence_includes_mobile_at_priority_four(self) -> None:
        order = self.registries["services"]["governance"]["commercialBuildOrder"]
        self.assertEqual(order, list(validator.ACCEPTED_SERVICE_ORDER))
        priorities = {
            service["id"]: service["priority"]
            for service in self.registries["services"]["services"]
        }
        self.assertEqual(
            [priorities[service_id] for service_id in order],
            list(range(1, 8)),
        )

    def test_mobile_applications_remains_planned_and_non_marketable(self) -> None:
        mobile = self.service("TECH-MOBILE-001")
        self.assertEqual(mobile["lifecycleStatus"], "PLANNED")
        self.assertFalse(mobile["marketingApproved"])
        self.assertFalse(mobile["publiclyMarketable"])
        self.assertTrue(all(gate["status"] == "NOT_ASSESSED" for gate in mobile["readinessGates"].values()))

    def test_owner_declaration_does_not_satisfy_g2(self) -> None:
        declarations = self.registries["capabilities"]["ownerDeclarations"]
        self.assertEqual(
            {item["capabilityFamily"] for item in declarations},
            {"Web Development", "Business Systems", "Automation", "Mobile Applications"},
        )
        self.assertTrue(all(item["ownerDeclaration"] == "OWNER_DECLARED_CAPABLE" for item in declarations))
        self.assertTrue(all(item["evidenceStatus"] == "UNASSESSED" for item in declarations))

        candidate = copy.deepcopy(self.website)
        candidate.update(
            lifecycleStatus="MARKET_APPROVED",
            marketingApproved=True,
            publiclyMarketable=False,
            marketApprovalDecision="repo:docs/02-decision-register.md#mpg-dec-028",
        )
        errors = self.validate_service(candidate)
        self.assertTrue(
            any("requires capability CAP-TECH-REQ-001" in error and "UNASSESSED" in error for error in errors),
            errors,
        )

    def test_professional_websites_is_the_only_primary_productization(self) -> None:
        services = self.registries["services"]
        wip = services["governance"]["wipAllocation"]
        self.assertEqual(services["governance"]["currentStage"], "STAGE_1")
        self.assertEqual(wip["primaryCommercialTrack"]["serviceId"], "TECH-WEB-001")
        self.assertEqual(wip["secondaryCapabilityTrack"]["status"], "UNALLOCATED")
        self.assertIsNone(wip["secondaryCapabilityTrack"]["subjectId"])
        active_states = {
            "BUILDING_CAPABILITY",
            "INTERNAL_READY",
            "PILOT_READY",
            "PILOTING",
            "DELIVERY_READY",
            "MARKET_APPROVED",
        }
        self.assertEqual(
            [service["id"] for service in services["services"] if service["lifecycleStatus"] in active_states],
            ["TECH-WEB-001"],
        )

    def test_brand_content_is_future_architecture_not_a_service(self) -> None:
        architecture = (validator.ROOT / "docs" / "03-brand-architecture.md").read_text(encoding="utf-8")
        self.assertIn("Brand & Content — FUTURE", architecture)
        self.assertNotIn(
            "Brand & Content",
            {service["name"] for service in self.registries["services"]["services"]},
        )

    def test_client_project_readiness_is_backlog_only(self) -> None:
        backlog = (validator.ROOT / "docs" / "19-backlog.md").read_text(encoding="utf-8")
        self.assertIn("Client Project Readiness & Dependency Detection", backlog)
        self.assertIn("BACKLOG — NOT CURRENTLY ACTIVE", backlog)
        for classification in ("`REQUIRED`", "`RECOMMENDED`", "`OPTIONAL`"):
            self.assertIn(classification, backlog)
        self.assertIn("must not silently absorb unscoped prerequisite work", backlog)


if __name__ == "__main__":
    unittest.main()
