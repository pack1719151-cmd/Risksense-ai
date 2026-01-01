from enum import Enum, auto

# reason_mapper.py
# Maps reasons for risk and anomaly detection
class ReasonType(Enum):
    RISK = auto()
    ANOMALY = auto()

class ReasonMapper:
    _reason_map = {
        ReasonType.RISK: "Identified risk based on predefined thresholds and patterns.",
        ReasonType.ANOMALY: "Detected anomaly due to deviation from normal behavior."
    }

    @classmethod
    def get_reason(cls, reason_type: ReasonType) -> str:
        return cls._reason_map.get(reason_type, "Unknown reason type.")

# Example usage:
# reason = ReasonMapper.get_reason(ReasonType.RISK)