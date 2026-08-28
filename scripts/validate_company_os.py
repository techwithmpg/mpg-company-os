#!/usr/bin/env python3
"""Validate MPG Company OS structure, registries, references, and release gates."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable

from generate_marketable_services import GENERATED_MARKER, render_catalogue


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "registry"
GENERATED_PATH = ROOT / "generated" / "marketable-services.md"
SCHEMA_VERSIONS = {
    "services": "1.0.0",
    "capabilities": "1.1.0",
    "tools": "1.0.0",
    "assets": "1.0.0",
    "partners": "1.0.0",
}
METADATA_STATUSES = {
    "IMPLEMENTED_PENDING_OWNER_ACCEPTANCE",
    "ACTIVE",
    "ACCEPTED",
    "FROZEN",
    "DEPRECATED",
}
ACCEPTED_SERVICE_ORDER = (
    "TECH-WEB-001",
    "TECH-SYS-001",
    "TECH-AUTO-001",
    "TECH-MOBILE-001",
    "MEDIA-DM-001",
    "MEDIA-SOCIAL-001",
    "TRADE-SOURCE-001",
)

LIFECYCLE_STATUSES = {
    "IDEA",
    "RESEARCH",
    "PLANNED",
    "PREREQUISITES_REQUIRED",
    "BUILDING_CAPABILITY",
    "INTERNAL_READY",
    "PILOT_READY",
    "PILOTING",
    "DELIVERY_READY",
    "MARKET_APPROVED",
    "ACTIVE",
    "PAUSED",
    "RETIRED",
}
DELIVERY_MODES = {"OWNED_DELIVERY", "PARTNER_DELIVERY", "HYBRID_DELIVERY"}
GATE_STATUSES = {"NOT_ASSESSED", "BLOCKED", "IN_PROGRESS", "SATISFIED", "NOT_APPLICABLE"}
GATE_IDS = {f"G{number}" for number in range(1, 14)}
CAPABILITY_STATUSES = {
    "UNASSESSED",
    "LEARNING",
    "PRACTICING",
    "COMPETENT",
    "VALIDATED",
    "PARTNER_DEPENDENT",
    "NOT_REQUIRED",
}
OWNER_DECLARATION_STATUSES = {"OWNER_DECLARED_CAPABLE"}
EXPECTED_OWNER_DECLARATIONS = {
    "DECL-FOUNDER-WEB-001": "Web Development",
    "DECL-FOUNDER-SYSTEMS-001": "Business Systems",
    "DECL-FOUNDER-AUTOMATION-001": "Automation",
    "DECL-FOUNDER-MOBILE-001": "Mobile Applications",
}
RESOURCE_STATUSES = {"UNKNOWN", "REQUIRED", "AVAILABLE", "NOT_AVAILABLE", "NOT_REQUIRED", "PLANNED"}
ADOPTION_STATES = {"CANDIDATE", "EVALUATING", "APPROVED", "OPERATING", "REJECTED", "RETIRED"}
PARTNER_STATUSES = {"CANDIDATE", "UNDER_REVIEW", "VALIDATED", "PAUSED", "REJECTED", "RETIRED"}
RELATIONSHIP_STATUSES = {"NONE", "EXPLORATORY", "INFORMAL", "CONTRACTED", "INACTIVE"}
DUE_DILIGENCE_STATUSES = {"NOT_STARTED", "IN_PROGRESS", "PASSED", "FAILED", "EXPIRED"}

ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
PRIVATE_REFERENCE_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{2,}$")

REQUIRED_REGISTRIES = {
    "services": REGISTRY_DIR / "services.json",
    "capabilities": REGISTRY_DIR / "capabilities.json",
    "tools": REGISTRY_DIR / "tools.json",
    "assets": REGISTRY_DIR / "assets.json",
    "partners": REGISTRY_DIR / "partners.json",
}

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".gitignore",
    *[f"docs/{number:02d}-{name}.md" for number, name in [
        (0, "project-charter"),
        (1, "project-status"),
        (2, "decision-register"),
        (3, "brand-architecture"),
        (4, "brand-strategy"),
        (5, "customer-market"),
        (6, "service-catalog"),
        (7, "pricing-commercial-model"),
        (8, "sales-system"),
        (9, "client-delivery-system"),
        (10, "marketing-system"),
        (11, "content-system"),
        (12, "visual-identity"),
        (13, "website-strategy"),
        (14, "technology-automation"),
        (15, "trade-distribution"),
        (16, "internal-operations"),
        (17, "sop-library"),
        (18, "metrics-growth"),
        (19, "backlog"),
    ]],
    *[f"operating-model/{name}.md" for name in [
        "capability-maturity-model",
        "service-lifecycle",
        "service-launch-gates",
        "work-in-progress-policy",
        "public-claims-policy",
        "partner-governance",
        "company-growth-model",
        "quality-standard",
        "risk-management",
        "information-handling",
        "tool-adoption-policy",
    ]],
    *[f"templates/{name}.md" for name in [
        "service-definition-template",
        "service-readiness-review",
        "service-pilot-report",
        "offer-sheet-template",
        "sop-template",
        "decision-record-template",
        "risk-assessment-template",
        "tool-evaluation-template",
        "partner-due-diligence-template",
        "client-discovery-template",
        "proposal-outline-template",
        "quotation-outline-template",
        "project-kickoff-template",
        "client-handover-template",
        "case-study-template",
    ]],
    *[f"{area}/README.md" for area in ["brand", "sales", "marketing", "operations", "research"]],
    "scripts/generate_marketable_services.py",
    "scripts/validate_company_os.py",
    "scripts/test_company_os.py",
    "generated/marketable-services.md",
    ".github/workflows/validate-company-os.yml",
]

SERVICE_REQUIRED_FIELDS = {
    "id",
    "division",
    "name",
    "description",
    "priority",
    "lifecycleStatus",
    "deliveryMode",
    "marketingApproved",
    "publiclyMarketable",
    "marketApprovalDecision",
    "targetCustomer",
    "problem",
    "prerequisites",
    "requiredCapabilities",
    "requiredTools",
    "requiredAssets",
    "requiredPartners",
    "readinessGates",
    "evidence",
    "readinessReview",
    "deliverySop",
    "qaChecklist",
    "pricingModelStatus",
    "capacityStatus",
    "notes",
}


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def load_json(path: Path, validation: Validation) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        validation.errors.append(f"Missing registry: {path.relative_to(ROOT)}")
        return None
    except json.JSONDecodeError as exc:
        validation.errors.append(
            f"Invalid JSON in {path.relative_to(ROOT)} at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        )
        return None
    validation.require(isinstance(value, dict), f"{path.relative_to(ROOT)} must contain a JSON object.")
    return value if isinstance(value, dict) else None


def validate_metadata(name: str, registry: dict[str, Any], validation: Validation) -> None:
    metadata = registry.get("metadata")
    validation.require(isinstance(metadata, dict), f"registry/{name}.json: metadata must be an object.")
    if not isinstance(metadata, dict):
        return
    for field in ("document", "status", "stage", "owner", "lastUpdated", "publicSafe", "authority"):
        validation.require(field in metadata, f"registry/{name}.json: metadata.{field} is required.")
    for field in ("document", "status", "stage", "owner", "lastUpdated", "authority"):
        value = metadata.get(field)
        validation.require(isinstance(value, str) and bool(value.strip()), f"registry/{name}.json: metadata.{field} must be non-empty text.")
    validation.require(metadata.get("status") in METADATA_STATUSES, f"registry/{name}.json has invalid metadata.status {metadata.get('status')!r}.")
    validation.require(metadata.get("publicSafe") is True, f"registry/{name}.json must be marked publicSafe=true.")
    validation.require(metadata.get("stage") == "STAGE_0", f"registry/{name}.json must preserve current stage STAGE_0.")
    updated = metadata.get("lastUpdated")
    try:
        if not isinstance(updated, str):
            raise ValueError
        date.fromisoformat(updated)
    except ValueError:
        validation.errors.append(f"registry/{name}.json: metadata.lastUpdated must be an ISO YYYY-MM-DD date.")


def require_list(record: dict[str, Any], field: str, context: str, validation: Validation) -> list[Any]:
    value = record.get(field)
    validation.require(isinstance(value, list), f"{context}.{field} must be an array.")
    return value if isinstance(value, list) else []


def declared_string_set(value: Any, context: str, validation: Validation) -> set[str]:
    validation.require(isinstance(value, list), f"{context} must be an array.")
    if not isinstance(value, list):
        return set()
    validation.require(all(isinstance(item, str) for item in value), f"{context} must contain only strings.")
    return {item for item in value if isinstance(item, str)}


def is_resolved_text(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    normalized = value.strip().upper()
    return bool(normalized) and not re.match(r"^(TBD|UNKNOWN|NOT_STARTED|UNASSESSED)(\b|\s|:)", normalized)


def is_traceable_reference(value: Any, *, repository_only: bool = False) -> bool:
    """Accept a real repository path or a non-sensitive private-record identifier."""
    if not isinstance(value, str):
        return False
    prefix, separator, locator = value.partition(":")
    if not separator or not locator:
        return False
    if prefix == "private" and not repository_only:
        return bool(PRIVATE_REFERENCE_PATTERN.fullmatch(locator))
    if prefix != "repo":
        return False
    path_text = locator.split("#", 1)[0].replace("\\", "/")
    if not path_text:
        return False
    parts = path_text.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        return False
    candidate = (ROOT / Path(*parts)).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return False
    return candidate.is_file()


def validate_service(
    service: Any,
    index: int,
    known_ids: dict[str, set[str]],
    records_by_id: dict[str, dict[str, dict[str, Any]]],
    validation: Validation,
) -> None:
    context = f"registry/services.json services[{index}]"
    validation.require(isinstance(service, dict), f"{context} must be an object.")
    if not isinstance(service, dict):
        return

    service_id = service.get("id", f"index-{index}")
    context = f"service {service_id}"
    missing = SERVICE_REQUIRED_FIELDS - service.keys()
    validation.require(not missing, f"{context} missing required fields: {', '.join(sorted(missing))}")
    validation.require(isinstance(service.get("id"), str) and bool(ID_PATTERN.fullmatch(service["id"])), f"{context} has malformed id.")
    for text_field in (
        "division",
        "name",
        "description",
        "marketApprovalDecision",
        "targetCustomer",
        "problem",
        "readinessReview",
        "deliverySop",
        "qaChecklist",
        "pricingModelStatus",
        "capacityStatus",
        "notes",
    ):
        value = service.get(text_field)
        validation.require(isinstance(value, str) and bool(value.strip()), f"{context}.{text_field} must be non-empty text.")
    validation.require(service.get("lifecycleStatus") in LIFECYCLE_STATUSES, f"{context} has invalid lifecycleStatus {service.get('lifecycleStatus')!r}.")
    validation.require(service.get("deliveryMode") in DELIVERY_MODES, f"{context} has invalid deliveryMode {service.get('deliveryMode')!r}.")
    validation.require(type(service.get("marketingApproved")) is bool, f"{context}.marketingApproved must be boolean.")
    validation.require(type(service.get("publiclyMarketable")) is bool, f"{context}.publiclyMarketable must be boolean.")
    validation.require(type(service.get("priority")) is int and service.get("priority", 0) > 0, f"{context}.priority must be a positive integer.")

    expected_public = service.get("lifecycleStatus") == "ACTIVE" and service.get("marketingApproved") is True
    validation.require(
        service.get("publiclyMarketable") is expected_public,
        f"{context}.publiclyMarketable must equal (lifecycleStatus == ACTIVE and marketingApproved == true).",
    )
    if service.get("marketingApproved") is True:
        validation.require(
            service.get("lifecycleStatus") in {"MARKET_APPROVED", "ACTIVE", "PAUSED"},
            f"{context}: marketingApproved=true is incompatible with lifecycleStatus {service.get('lifecycleStatus')!r}.",
        )

    prerequisites = require_list(service, "prerequisites", context, validation)
    capabilities = require_list(service, "requiredCapabilities", context, validation)
    tools = require_list(service, "requiredTools", context, validation)
    assets = require_list(service, "requiredAssets", context, validation)
    partners = require_list(service, "requiredPartners", context, validation)
    evidence = require_list(service, "evidence", context, validation)
    validation.require(all(isinstance(item, str) and bool(item.strip()) for item in prerequisites), f"{context}.prerequisites must contain only non-empty text.")
    validation.require(all(isinstance(item, str) and bool(item.strip()) for item in evidence), f"{context}.evidence must contain only non-empty references.")

    for field, references, group in (
        ("requiredCapabilities", capabilities, "capabilities"),
        ("requiredTools", tools, "tools"),
        ("requiredAssets", assets, "assets"),
        ("requiredPartners", partners, "partners"),
    ):
        for reference in references:
            validation.require(
                isinstance(reference, str) and reference in known_ids[group],
                f"{context}.{field} contains unknown {group} id {reference!r}.",
            )

    gates = service.get("readinessGates")
    validation.require(isinstance(gates, dict), f"{context}.readinessGates must be an object.")
    if isinstance(gates, dict):
        validation.require(set(gates) == GATE_IDS, f"{context}.readinessGates must contain exactly G1 through G13.")
        for gate_id in sorted(GATE_IDS, key=lambda item: int(item[1:])):
            gate = gates.get(gate_id)
            validation.require(isinstance(gate, dict), f"{context}.{gate_id} must be an object.")
            if not isinstance(gate, dict):
                continue
            validation.require(set(("status", "evidence", "notes")) <= gate.keys(), f"{context}.{gate_id} requires status, evidence, and notes.")
            validation.require(gate.get("status") in GATE_STATUSES, f"{context}.{gate_id} has invalid status {gate.get('status')!r}.")
            gate_evidence = gate.get("evidence")
            validation.require(isinstance(gate_evidence, list), f"{context}.{gate_id}.evidence must be an array.")
            if isinstance(gate_evidence, list):
                validation.require(all(isinstance(item, str) and bool(item.strip()) for item in gate_evidence), f"{context}.{gate_id}.evidence must contain only non-empty references.")
            validation.require(isinstance(gate.get("notes"), str) and bool(gate.get("notes", "").strip()), f"{context}.{gate_id}.notes must be non-empty text.")

    if service.get("lifecycleStatus") in {"MARKET_APPROVED", "ACTIVE"}:
        release_label = service.get("lifecycleStatus")
        validation.require(service.get("marketingApproved") is True, f"{release_label} {context} requires owner marketing approval.")
        validation.require(
            is_traceable_reference(service.get("marketApprovalDecision"), repository_only=True),
            f"{release_label} {context} requires a repository-backed owner market-approval decision reference.",
        )
        validation.require(
            is_traceable_reference(service.get("readinessReview")),
            f"{release_label} {context} requires a traceable readiness-review reference.",
        )
        if release_label == "ACTIVE":
            validation.require(service.get("publiclyMarketable") is True, f"ACTIVE {context} must be publiclyMarketable after approval.")
        validation.require(is_resolved_text(service.get("targetCustomer")), f"{release_label} {context} requires a resolved targetCustomer.")
        validation.require(is_resolved_text(service.get("problem")), f"{release_label} {context} requires a resolved customer problem.")
        validation.require(bool(prerequisites), f"{release_label} {context} requires recorded prerequisite conclusions.")
        validation.require(all(is_resolved_text(item) for item in prerequisites), f"{release_label} {context} requires resolved prerequisite conclusions.")
        validation.require(bool(capabilities), f"{release_label} {context} requires at least one referenced capability.")
        validation.require(bool(evidence), f"{release_label} {context} requires service-level proof.")
        validation.require(all(is_traceable_reference(item) for item in evidence), f"{release_label} {context} service evidence must use traceable repo: or private: references.")
        validation.require(is_traceable_reference(service.get("deliverySop")), f"{release_label} {context} requires a traceable accepted delivery SOP reference.")
        validation.require(is_traceable_reference(service.get("qaChecklist")), f"{release_label} {context} requires a traceable accepted QA checklist reference.")
        validation.require(service.get("pricingModelStatus") in {"READY", "APPROVED"}, f"{release_label} {context} requires ready pricing logic.")
        validation.require(service.get("capacityStatus") in {"READY", "VALIDATED"}, f"{release_label} {context} requires ready capacity.")

        approved_partner_capabilities: set[str] = set()
        for partner_id in partners:
            partner = records_by_id["partners"].get(partner_id) if isinstance(partner_id, str) else None
            if not isinstance(partner, dict):
                continue
            partner_ready = (
                partner.get("approvedForDelivery") is True
                and partner.get("status") == "VALIDATED"
                and partner.get("dueDiligenceStatus") == "PASSED"
                and partner.get("relationshipStatus") == "CONTRACTED"
            )
            validation.require(partner_ready, f"{release_label} {context} requires delivery-approved partner {partner_id}.")
            if partner_ready and isinstance(partner.get("requiredCapability"), str):
                approved_partner_capabilities.add(partner["requiredCapability"])

        has_partner_dependent_capability = False
        for capability_id in capabilities:
            capability = records_by_id["capabilities"].get(capability_id) if isinstance(capability_id, str) else None
            if not isinstance(capability, dict):
                continue
            capability_status = capability.get("status")
            validation.require(
                capability_status in {"VALIDATED", "PARTNER_DEPENDENT"},
                f"{release_label} {context} requires capability {capability_id} to be VALIDATED or properly PARTNER_DEPENDENT; found {capability_status!r}.",
            )
            if capability_status == "PARTNER_DEPENDENT":
                has_partner_dependent_capability = True
                validation.require(
                    service.get("deliveryMode") in {"PARTNER_DELIVERY", "HYBRID_DELIVERY"},
                    f"{release_label} {context} cannot use partner-dependent capability {capability_id} with OWNED_DELIVERY.",
                )
                validation.require(
                    capability_id in approved_partner_capabilities,
                    f"{release_label} {context} lacks an approved referenced partner for capability {capability_id}.",
                )

        for tool_id in tools:
            tool = records_by_id["tools"].get(tool_id) if isinstance(tool_id, str) else None
            if not isinstance(tool, dict):
                continue
            validation.require(
                tool.get("status") == "AVAILABLE"
                and tool.get("adoptionState") in {"APPROVED", "OPERATING"}
                and tool.get("ownerApproved") is True,
                f"{release_label} {context} requires tool {tool_id} to be available and owner-approved for operation.",
            )

        for asset_id in assets:
            asset = records_by_id["assets"].get(asset_id) if isinstance(asset_id, str) else None
            if isinstance(asset, dict):
                validation.require(asset.get("status") == "AVAILABLE", f"{release_label} {context} requires asset {asset_id} to be AVAILABLE.")

        material_partner_dependency = (
            service.get("deliveryMode") in {"PARTNER_DELIVERY", "HYBRID_DELIVERY"}
            or bool(partners)
            or has_partner_dependent_capability
        )
        if material_partner_dependency:
            validation.require(bool(partners), f"{release_label} {context} has a partner-dependent delivery design but no requiredPartners.")
            g12 = gates.get("G12") if isinstance(gates, dict) else None
            validation.require(isinstance(g12, dict) and g12.get("status") == "SATISFIED", f"{release_label} {context} requires G12 SATISFIED for material partner dependency.")

        if isinstance(gates, dict):
            always_required = {"G1", "G2", "G5", "G6", "G7", "G8", "G10", "G11", "G13"}
            for gate_id in GATE_IDS:
                gate = gates.get(gate_id, {})
                status = gate.get("status") if isinstance(gate, dict) else None
                allowed_ready = {"SATISFIED"} if gate_id in always_required else {"SATISFIED", "NOT_APPLICABLE"}
                validation.require(status in allowed_ready, f"{release_label} {context} has unresolved required gate {gate_id}: {status!r}.")
                if status == "SATISFIED":
                    validation.require(bool(gate.get("evidence")), f"{release_label} {context} gate {gate_id} requires evidence.")
                    if isinstance(gate.get("evidence"), list):
                        validation.require(
                            all(is_traceable_reference(item) for item in gate["evidence"]),
                            f"{release_label} {context} gate {gate_id} evidence must use traceable repo: or private: references.",
                        )
                if status == "NOT_APPLICABLE":
                    validation.require(is_resolved_text(gate.get("notes")), f"{release_label} {context} gate {gate_id} requires a documented N/A rationale.")


def validate_capability(capability: Any, index: int, validation: Validation) -> None:
    context = f"registry/capabilities.json capabilities[{index}]"
    validation.require(isinstance(capability, dict), f"{context} must be an object.")
    if not isinstance(capability, dict):
        return
    required = {"id", "category", "name", "description", "status", "evidence", "lastAssessed", "notes"}
    validation.require(required <= capability.keys(), f"{context} missing fields: {', '.join(sorted(required - capability.keys()))}")
    for text_field in ("id", "category", "name", "description", "notes"):
        value = capability.get(text_field)
        validation.require(isinstance(value, str) and bool(value.strip()), f"{context}.{text_field} must be non-empty text.")
    validation.require(capability.get("status") in CAPABILITY_STATUSES, f"{context} has invalid status {capability.get('status')!r}.")
    evidence = require_list(capability, "evidence", context, validation)
    validation.require(all(isinstance(item, str) and bool(item.strip()) for item in evidence), f"{context}.evidence must contain only non-empty references.")
    last_assessed = capability.get("lastAssessed")
    validation.require(last_assessed is None or isinstance(last_assessed, str), f"{context}.lastAssessed must be null or text.")
    if capability.get("status") == "VALIDATED":
        validation.require(bool(evidence), f"{context}: VALIDATED requires evidence.")
        validation.require(all(is_traceable_reference(item) for item in evidence), f"{context}: VALIDATED evidence must use traceable repo: or private: references.")
        validation.require(is_resolved_text(last_assessed), f"{context}: VALIDATED requires a resolved lastAssessed value.")


def validate_owner_declaration(declaration: Any, index: int, validation: Validation) -> None:
    context = f"registry/capabilities.json ownerDeclarations[{index}]"
    validation.require(isinstance(declaration, dict), f"{context} must be an object.")
    if not isinstance(declaration, dict):
        return
    required = {
        "id",
        "capabilityFamily",
        "declaredBy",
        "ownerDeclaration",
        "evidenceStatus",
        "evidence",
        "lastAssessed",
        "decisionReference",
        "notes",
    }
    validation.require(required <= declaration.keys(), f"{context} missing fields: {', '.join(sorted(required - declaration.keys()))}")
    for text_field in ("id", "capabilityFamily", "declaredBy", "ownerDeclaration", "evidenceStatus", "decisionReference", "notes"):
        value = declaration.get(text_field)
        validation.require(isinstance(value, str) and bool(value.strip()), f"{context}.{text_field} must be non-empty text.")
    validation.require(
        isinstance(declaration.get("id"), str) and bool(ID_PATTERN.fullmatch(declaration["id"])),
        f"{context} has malformed id.",
    )
    validation.require(
        declaration.get("ownerDeclaration") in OWNER_DECLARATION_STATUSES,
        f"{context} has invalid ownerDeclaration {declaration.get('ownerDeclaration')!r}.",
    )
    validation.require(
        declaration.get("evidenceStatus") in CAPABILITY_STATUSES,
        f"{context} has invalid evidenceStatus {declaration.get('evidenceStatus')!r}.",
    )
    validation.require(declaration.get("declaredBy") == "MPG Founder", f"{context}.declaredBy must remain MPG Founder.")
    validation.require(
        is_traceable_reference(declaration.get("decisionReference"), repository_only=True),
        f"{context}.decisionReference must point to the repository-backed owner decision.",
    )
    evidence = require_list(declaration, "evidence", context, validation)
    validation.require(all(isinstance(item, str) and bool(item.strip()) for item in evidence), f"{context}.evidence must contain only non-empty references.")
    last_assessed = declaration.get("lastAssessed")
    validation.require(last_assessed is None or isinstance(last_assessed, str), f"{context}.lastAssessed must be null or text.")
    if declaration.get("evidenceStatus") in {"COMPETENT", "VALIDATED"}:
        validation.require(bool(evidence), f"{context}: evidence maturity cannot be inferred from the owner declaration.")
        validation.require(all(is_traceable_reference(item) for item in evidence), f"{context}: assessed evidence must use traceable repo: or private: references.")
        validation.require(is_resolved_text(last_assessed), f"{context}: assessed evidence maturity requires lastAssessed.")


def validate_tool(tool: Any, index: int, validation: Validation) -> None:
    context = f"registry/tools.json tools[{index}]"
    validation.require(isinstance(tool, dict), f"{context} must be an object.")
    if not isinstance(tool, dict):
        return
    required = {"id", "tool", "purpose", "capabilityEnabled", "status", "adoptionState", "costKnown", "accountAvailable", "ownerApproved", "dataSensitivity", "notes"}
    validation.require(required <= tool.keys(), f"{context} missing fields: {', '.join(sorted(required - tool.keys()))}")
    for text_field in ("id", "tool", "purpose", "capabilityEnabled", "dataSensitivity", "notes"):
        value = tool.get(text_field)
        validation.require(isinstance(value, str) and bool(value.strip()), f"{context}.{text_field} must be non-empty text.")
    validation.require(tool.get("status") in RESOURCE_STATUSES, f"{context} has invalid resource status {tool.get('status')!r}.")
    validation.require(tool.get("adoptionState") in ADOPTION_STATES, f"{context} has invalid adoptionState {tool.get('adoptionState')!r}.")
    validation.require(tool.get("costKnown") in {"YES", "NO", "UNKNOWN"}, f"{context}.costKnown must be YES, NO, or UNKNOWN.")
    validation.require(tool.get("accountAvailable") in {"YES", "NO", "UNKNOWN"}, f"{context}.accountAvailable must be YES, NO, or UNKNOWN.")
    validation.require(type(tool.get("ownerApproved")) is bool, f"{context}.ownerApproved must be boolean.")
    if tool.get("adoptionState") in {"APPROVED", "OPERATING"}:
        validation.require(tool.get("ownerApproved") is True, f"{context}: approved/operating tools require ownerApproved=true.")


def validate_asset(asset: Any, index: int, validation: Validation) -> None:
    context = f"registry/assets.json assets[{index}]"
    validation.require(isinstance(asset, dict), f"{context} must be an object.")
    if not isinstance(asset, dict):
        return
    required = {"id", "asset", "category", "purpose", "status", "requiredFor", "evidence", "publicSafe", "notes"}
    validation.require(required <= asset.keys(), f"{context} missing fields: {', '.join(sorted(required - asset.keys()))}")
    for text_field in ("id", "asset", "category", "purpose", "notes"):
        value = asset.get(text_field)
        validation.require(isinstance(value, str) and bool(value.strip()), f"{context}.{text_field} must be non-empty text.")
    validation.require(asset.get("status") in RESOURCE_STATUSES, f"{context} has invalid status {asset.get('status')!r}.")
    require_list(asset, "requiredFor", context, validation)
    evidence = require_list(asset, "evidence", context, validation)
    validation.require(all(isinstance(item, str) and bool(item.strip()) for item in evidence), f"{context}.evidence must contain only non-empty references.")
    validation.require(type(asset.get("publicSafe")) is bool, f"{context}.publicSafe must be boolean.")


def validate_partner(partner: Any, index: int, validation: Validation) -> None:
    context = f"registry/partners.json partners[{index}]"
    validation.require(isinstance(partner, dict), f"{context} must be an object.")
    if not isinstance(partner, dict):
        return
    required = {"id", "category", "requiredCapability", "status", "relationshipStatus", "dueDiligenceStatus", "approvedForDelivery", "publicDisclosureAllowed", "notes"}
    validation.require(required <= partner.keys(), f"{context} missing fields: {', '.join(sorted(required - partner.keys()))}")
    for text_field in ("id", "category", "requiredCapability", "notes"):
        value = partner.get(text_field)
        validation.require(isinstance(value, str) and bool(value.strip()), f"{context}.{text_field} must be non-empty text.")
    validation.require(partner.get("status") in PARTNER_STATUSES, f"{context} has invalid status.")
    validation.require(partner.get("relationshipStatus") in RELATIONSHIP_STATUSES, f"{context} has invalid relationshipStatus.")
    validation.require(partner.get("dueDiligenceStatus") in DUE_DILIGENCE_STATUSES, f"{context} has invalid dueDiligenceStatus.")
    validation.require(type(partner.get("approvedForDelivery")) is bool, f"{context}.approvedForDelivery must be boolean.")
    validation.require(type(partner.get("publicDisclosureAllowed")) is bool, f"{context}.publicDisclosureAllowed must be boolean.")
    if partner.get("approvedForDelivery") is True:
        validation.require(partner.get("status") == "VALIDATED", f"{context}: delivery approval requires VALIDATED status.")
        validation.require(partner.get("dueDiligenceStatus") == "PASSED", f"{context}: delivery approval requires PASSED due diligence.")
        validation.require(partner.get("relationshipStatus") == "CONTRACTED", f"{context}: delivery approval requires a CONTRACTED relationship.")
    forbidden_fragments = {"contact", "email", "phone", "address", "bank", "credential", "secret", "contractterms"}
    normalized_keys = {re.sub(r"[^a-z]", "", str(key).lower()) for key in partner}
    exposed = sorted(key for key in normalized_keys if any(fragment in key for fragment in forbidden_fragments))
    validation.require(not exposed, f"{context} contains public-registry private-data fields: {', '.join(exposed)}")


def collect_ids(records: Iterable[Any], group: str, global_ids: dict[str, str], validation: Validation) -> set[str]:
    result: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            continue
        record_id = record.get("id")
        validation.require(isinstance(record_id, str) and bool(ID_PATTERN.fullmatch(record_id)), f"{group}[{index}] has malformed id {record_id!r}.")
        if not isinstance(record_id, str):
            continue
        validation.require(record_id not in result, f"Duplicate id {record_id!r} within {group}.")
        if record_id in global_ids:
            validation.errors.append(f"Duplicate id {record_id!r} across {global_ids[record_id]} and {group}.")
        else:
            global_ids[record_id] = group
        result.add(record_id)
    return result


def validate_generated(services_registry: dict[str, Any], validation: Validation) -> None:
    if not GENERATED_PATH.exists():
        validation.errors.append("Missing generated/marketable-services.md. Run the catalogue generator.")
        return
    actual = GENERATED_PATH.read_text(encoding="utf-8")
    validation.require(actual.startswith(GENERATED_MARKER + "\n"), "generated/marketable-services.md lacks the required generated-file marker.")
    try:
        expected = render_catalogue(services_registry)
    except (KeyError, TypeError, ValueError) as exc:
        validation.errors.append(f"Cannot render marketable catalogue from malformed service data: {exc}")
        return
    validation.require(actual == expected, "generated/marketable-services.md is stale; run python scripts/generate_marketable_services.py.")


def main() -> int:
    validation = Validation()

    for relative_path in REQUIRED_PATHS:
        path = ROOT / relative_path
        validation.require(path.is_file(), f"Missing required file: {relative_path}")
        if path.is_file():
            validation.require(path.stat().st_size > 0, f"Required file is empty: {relative_path}")

    registries: dict[str, dict[str, Any]] = {}
    for name, path in REQUIRED_REGISTRIES.items():
        registry = load_json(path, validation)
        if registry is not None:
            registries[name] = registry
            expected_version = SCHEMA_VERSIONS[name]
            validation.require(registry.get("schemaVersion") == expected_version, f"registry/{name}.json must use schemaVersion {expected_version}.")
            validate_metadata(name, registry, validation)

    if set(registries) != set(REQUIRED_REGISTRIES):
        print("Company OS validation failed:", file=sys.stderr)
        for error in validation.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    collection_names = {
        "services": "services",
        "capabilities": "capabilities",
        "tools": "tools",
        "assets": "assets",
        "partners": "partners",
    }
    collections: dict[str, list[Any]] = {}
    for registry_name, collection_name in collection_names.items():
        value = registries[registry_name].get(collection_name)
        validation.require(isinstance(value, list), f"registry/{registry_name}.json must contain a {collection_name} array.")
        collections[registry_name] = value if isinstance(value, list) else []

    global_ids: dict[str, str] = {}
    known_ids = {
        group: collect_ids(records, group, global_ids, validation)
        for group, records in collections.items()
    }
    records_by_id: dict[str, dict[str, dict[str, Any]]] = {
        group: {
            record["id"]: record
            for record in records
            if isinstance(record, dict) and isinstance(record.get("id"), str)
        }
        for group, records in collections.items()
    }

    services_registry = registries["services"]
    allowed_values = services_registry.get("allowedValues")
    validation.require(isinstance(allowed_values, dict), "registry/services.json allowedValues must be an object.")
    allowed_values = allowed_values if isinstance(allowed_values, dict) else {}
    validation.require(
        declared_string_set(allowed_values.get("lifecycleStatus"), "registry/services.json allowedValues.lifecycleStatus", validation) == LIFECYCLE_STATUSES,
        "registry/services.json lifecycleStatus allowedValues do not match validator constants.",
    )
    validation.require(
        declared_string_set(allowed_values.get("deliveryMode"), "registry/services.json allowedValues.deliveryMode", validation) == DELIVERY_MODES,
        "registry/services.json deliveryMode allowedValues do not match validator constants.",
    )
    validation.require(
        declared_string_set(allowed_values.get("gateStatus"), "registry/services.json allowedValues.gateStatus", validation) == GATE_STATUSES,
        "registry/services.json gateStatus allowedValues do not match validator constants.",
    )
    gate_definitions = services_registry.get("readinessGateDefinitions")
    validation.require(isinstance(gate_definitions, dict), "registry/services.json readinessGateDefinitions must be an object.")
    validation.require(
        set(gate_definitions) == GATE_IDS if isinstance(gate_definitions, dict) else False,
        "registry/services.json must define exactly readiness gates G1 through G13.",
    )

    validation.require(
        declared_string_set(registries["capabilities"].get("allowedStatuses"), "registry/capabilities.json allowedStatuses", validation) == CAPABILITY_STATUSES,
        "registry/capabilities.json allowedStatuses do not match validator constants.",
    )
    validation.require(
        declared_string_set(registries["capabilities"].get("allowedOwnerDeclarations"), "registry/capabilities.json allowedOwnerDeclarations", validation) == OWNER_DECLARATION_STATUSES,
        "registry/capabilities.json allowedOwnerDeclarations do not match validator constants.",
    )
    owner_declarations = registries["capabilities"].get("ownerDeclarations")
    validation.require(isinstance(owner_declarations, list), "registry/capabilities.json ownerDeclarations must be an array.")
    owner_declarations = owner_declarations if isinstance(owner_declarations, list) else []
    declaration_ids: set[str] = set()
    declaration_families: dict[str, str] = {}
    for index, declaration in enumerate(owner_declarations):
        validate_owner_declaration(declaration, index, validation)
        if isinstance(declaration, dict) and isinstance(declaration.get("id"), str):
            declaration_id = declaration["id"]
            validation.require(declaration_id not in declaration_ids, f"Duplicate owner declaration id {declaration_id!r}.")
            validation.require(declaration_id not in global_ids, f"Owner declaration id {declaration_id!r} collides with a registry record id.")
            declaration_ids.add(declaration_id)
            if isinstance(declaration.get("capabilityFamily"), str):
                declaration_families[declaration_id] = declaration["capabilityFamily"]
    validation.require(
        declaration_families == EXPECTED_OWNER_DECLARATIONS,
        "Owner declarations must cover exactly Web Development, Business Systems, Automation, and Mobile Applications with stable IDs.",
    )
    validation.require(
        declared_string_set(registries["tools"].get("allowedResourceStatuses"), "registry/tools.json allowedResourceStatuses", validation) == RESOURCE_STATUSES,
        "registry/tools.json allowedResourceStatuses do not match validator constants.",
    )
    validation.require(
        declared_string_set(registries["tools"].get("allowedAdoptionStates"), "registry/tools.json allowedAdoptionStates", validation) == ADOPTION_STATES,
        "registry/tools.json allowedAdoptionStates do not match validator constants.",
    )
    validation.require(
        declared_string_set(registries["assets"].get("allowedStatuses"), "registry/assets.json allowedStatuses", validation) == RESOURCE_STATUSES,
        "registry/assets.json allowedStatuses do not match validator constants.",
    )
    partner_allowed = registries["partners"].get("allowedValues")
    validation.require(isinstance(partner_allowed, dict), "registry/partners.json allowedValues must be an object.")
    partner_allowed = partner_allowed if isinstance(partner_allowed, dict) else {}
    validation.require(
        declared_string_set(partner_allowed.get("status"), "registry/partners.json allowedValues.status", validation) == PARTNER_STATUSES,
        "registry/partners.json status allowedValues do not match validator constants.",
    )
    validation.require(
        declared_string_set(partner_allowed.get("relationshipStatus"), "registry/partners.json allowedValues.relationshipStatus", validation) == RELATIONSHIP_STATUSES,
        "registry/partners.json relationshipStatus allowedValues do not match validator constants.",
    )
    validation.require(
        declared_string_set(partner_allowed.get("dueDiligenceStatus"), "registry/partners.json allowedValues.dueDiligenceStatus", validation) == DUE_DILIGENCE_STATUSES,
        "registry/partners.json dueDiligenceStatus allowedValues do not match validator constants.",
    )

    for index, service in enumerate(collections["services"]):
        validate_service(service, index, known_ids, records_by_id, validation)
    for index, capability in enumerate(collections["capabilities"]):
        validate_capability(capability, index, validation)
    for index, tool in enumerate(collections["tools"]):
        validate_tool(tool, index, validation)
    for index, asset in enumerate(collections["assets"]):
        validate_asset(asset, index, validation)
    for index, partner in enumerate(collections["partners"]):
        validate_partner(partner, index, validation)

    for partner in collections["partners"]:
        if isinstance(partner, dict):
            validation.require(
                partner.get("requiredCapability") in known_ids["capabilities"],
                f"partner {partner.get('id', 'UNKNOWN')} references unknown requiredCapability {partner.get('requiredCapability')!r}.",
            )

    approved_partner_capabilities = {
        partner.get("requiredCapability")
        for partner in collections["partners"]
        if isinstance(partner, dict)
        and partner.get("approvedForDelivery") is True
        and partner.get("status") == "VALIDATED"
        and partner.get("dueDiligenceStatus") == "PASSED"
        and partner.get("relationshipStatus") == "CONTRACTED"
    }
    for capability in collections["capabilities"]:
        if isinstance(capability, dict) and capability.get("status") == "PARTNER_DEPENDENT":
            validation.require(
                capability.get("id") in approved_partner_capabilities,
                f"capability {capability.get('id', 'UNKNOWN')} cannot be PARTNER_DEPENDENT without an approved partner for that exact capability.",
            )

    priorities = [record.get("priority") for record in collections["services"] if isinstance(record, dict) and type(record.get("priority")) is int]
    validation.require(len(priorities) == len(set(priorities)), "Service priorities must be unique.")
    active_productization_states = {
        "BUILDING_CAPABILITY",
        "INTERNAL_READY",
        "PILOT_READY",
        "PILOTING",
        "DELIVERY_READY",
        "MARKET_APPROVED",
    }
    productizing = [
        record.get("id")
        for record in collections["services"]
        if isinstance(record, dict) and record.get("lifecycleStatus") in active_productization_states
    ]
    by_id = {record.get("id"): record for record in collections["services"] if isinstance(record, dict) and isinstance(record.get("id"), str)}
    governance = services_registry.get("governance")
    validation.require(isinstance(governance, dict), "registry/services.json governance must be an object.")
    governance = governance if isinstance(governance, dict) else {}
    validation.require(governance.get("currentStage") == "STAGE_1", "Service governance must record currentStage STAGE_1.")
    build_order = governance.get("commercialBuildOrder")
    validation.require(
        isinstance(build_order, list) and tuple(build_order) == ACCEPTED_SERVICE_ORDER,
        "Service governance commercialBuildOrder must match the accepted seven-family sequence.",
    )
    validation.require(
        governance.get("publicationPredicate") == "lifecycleStatus == ACTIVE && marketingApproved == true",
        "Service governance publicationPredicate must preserve the accepted two-condition rule.",
    )
    validation.require(
        governance.get("evidenceReferenceFormat") == "repo:<relative-path>[#anchor] or private:<public-safe-id>",
        "Service governance must declare the validator's traceable evidence-reference format.",
    )

    for expected_priority, service_id in enumerate(ACCEPTED_SERVICE_ORDER, start=1):
        service = by_id.get(service_id)
        validation.require(service is not None, f"Missing accepted commercial-sequence service {service_id}.")
        if service is not None:
            validation.require(
                service.get("priority") == expected_priority,
                f"{service_id} must remain priority {expected_priority} in the accepted commercial sequence.",
            )

    wip = governance.get("wipAllocation")
    validation.require(isinstance(wip, dict), "Service governance wipAllocation must be an object.")
    wip = wip if isinstance(wip, dict) else {}
    primary = wip.get("primaryCommercialTrack")
    secondary = wip.get("secondaryCapabilityTrack")
    validation.require(isinstance(primary, dict), "wipAllocation.primaryCommercialTrack must be an object.")
    validation.require(isinstance(secondary, dict), "wipAllocation.secondaryCapabilityTrack must be an object.")
    primary = primary if isinstance(primary, dict) else {}
    secondary = secondary if isinstance(secondary, dict) else {}
    primary_service_id = primary.get("serviceId")
    validation.require(primary_service_id == "TECH-WEB-001", "The current primary commercial track must remain TECH-WEB-001.")
    validation.require(primary.get("status") == "ACTIVE_PRODUCTIZATION", "The current primary commercial track must be ACTIVE_PRODUCTIZATION.")
    validation.require(
        productizing == [primary_service_id],
        "WIP violation: the sole active productization record must be the allocated primary track; found "
        + ", ".join(str(item) for item in productizing),
    )
    validation.require(secondary.get("status") in {"UNALLOCATED", "ACTIVE", "PAUSED"}, "Secondary capability track has invalid status.")
    if secondary.get("status") == "UNALLOCATED":
        validation.require(secondary.get("subjectId") is None, "An unallocated secondary capability track must have subjectId=null.")
        validation.require(secondary.get("ownerDecision") == "NONE", "An unallocated secondary capability track must have ownerDecision=NONE.")
    else:
        validation.require(isinstance(secondary.get("subjectId"), str) and bool(secondary["subjectId"].strip()), "An allocated secondary capability track requires one subjectId.")
        validation.require(
            is_traceable_reference(secondary.get("ownerDecision"), repository_only=True),
            "An allocated secondary capability track requires a repository-backed owner decision.",
        )

    validate_generated(services_registry, validation)

    if validation.errors:
        print(f"Company OS validation failed with {len(validation.errors)} error(s):", file=sys.stderr)
        for error in validation.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    marketable_count = sum(
        1
        for record in collections["services"]
        if isinstance(record, dict) and record.get("publiclyMarketable") is True
    )
    print(
        "Company OS validation passed: "
        f"{len(collections['services'])} services, "
        f"{len(collections['capabilities'])} capabilities, "
        f"{len(collections['tools'])} tools, "
        f"{len(collections['assets'])} assets, "
        f"{len(collections['partners'])} partners, "
        f"{marketable_count} marketable services."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
