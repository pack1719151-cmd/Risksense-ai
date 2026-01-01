from enum import Enum, auto

# regulatory_flags.py
# Flags for regulatory compliance
class SeverityLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class RegulatoryFlag:
    """Represents a regulatory compliance flag."""
    def __init__(self, name, description, severity, references=None, impacted_domains=None):
        self.name = name
        self.description = description
        self.severity = severity
        self.references = references or []
        self.impacted_domains = impacted_domains or []

    def __repr__(self):
        return (f"<RegulatoryFlag name={self.name} severity={self.severity.name} "
                f"domains={self.impacted_domains}>")

    def is_critical(self):
        return self.severity == SeverityLevel.CRITICAL

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "severity": self.severity.name,
            "references": self.references,
            "impacted_domains": self.impacted_domains
        }

# Example flags with extended info
GDPR = RegulatoryFlag(
    name="GDPR",
    description="General Data Protection Regulation compliance required.",
    severity=SeverityLevel.HIGH,
    references=["https://gdpr.eu/", "https://ec.europa.eu/info/law/law-topic/data-protection_en"],
    impacted_domains=["Data Privacy", "EU"]
)

HIPAA = RegulatoryFlag(
    name="HIPAA",
    description="Health Insurance Portability and Accountability Act compliance required.",
    severity=SeverityLevel.CRITICAL,
    references=["https://www.hhs.gov/hipaa/index.html"],
    impacted_domains=["Healthcare", "US"]
)

PCI_DSS = RegulatoryFlag(
    name="PCI DSS",
    description="Payment Card Industry Data Security Standard compliance required.",
    severity=SeverityLevel.HIGH,
    references=["https://www.pcisecuritystandards.org/"],
    impacted_domains=["Finance", "Payment Processing"]
)

SOX = RegulatoryFlag(
    name="SOX",
    description="Sarbanes-Oxley Act compliance required.",
    severity=SeverityLevel.MEDIUM,
    references=["https://www.sec.gov/spotlight/sarbanes-oxley.htm"],
    impacted_domains=["Corporate Governance", "US"]
)

CCPA = RegulatoryFlag(
    name="CCPA",
    description="California Consumer Privacy Act compliance required.",
    severity=SeverityLevel.HIGH,
    references=["https://oag.ca.gov/privacy/ccpa"],
    impacted_domains=["Data Privacy", "California"]
)

FISMA = RegulatoryFlag(
    name="FISMA",
    description="Federal Information Security Management Act compliance required.",
    severity=SeverityLevel.CRITICAL,
    references=["https://www.dhs.gov/fisma"],
    impacted_domains=["Federal Agencies", "US"]
)

ISO_27001 = RegulatoryFlag(
    name="ISO 27001",
    description="ISO/IEC 27001 Information Security Management compliance required.",
    severity=SeverityLevel.HIGH,
    references=["https://www.iso.org/isoiec-27001-information-security.html"],
    impacted_domains=["Information Security", "Global"]
)

REGULATORY_FLAGS = [
    GDPR, HIPAA, PCI_DSS, SOX, CCPA, FISMA, ISO_27001
]

def get_flags_by_severity(severity: SeverityLevel):
    return [flag for flag in REGULATORY_FLAGS if flag.severity == severity]

def get_flag_by_name(name: str):
    for flag in REGULATORY_FLAGS:
        if flag.name.lower() == name.lower():
            return flag
    return None