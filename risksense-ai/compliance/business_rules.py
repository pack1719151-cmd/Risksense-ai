from typing import List, Dict, Optional

# business_rules.py
# Contains business rules for compliance
def is_compliant(control_status: str) -> bool:
    """
    Determines if a control is compliant based on its status.

    Args:
        control_status (str): The status of the control (e.g., 'passed', 'failed', 'not applicable').

    Returns:
        bool: True if compliant, False otherwise.
    """
    return control_status.lower() == 'passed'


def calculate_compliance_score(passed: int, total: int) -> float:
    """
    Calculates the compliance score as a percentage.

    Args:
        passed (int): Number of controls passed.
        total (int): Total number of controls.

    Returns:
        float: Compliance score as a percentage (0.0 to 100.0).
    """
    if total == 0:
        return 0.0
    return (passed / total) * 100.0


def get_control_summary(controls: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Summarizes the number of passed, failed, and not applicable controls.

    Args:
        controls (List[Dict[str, str]]): List of controls with 'status' key.

    Returns:
        Dict[str, int]: Summary with counts for 'passed', 'failed', 'not_applicable'.
    """
    summary = {'passed': 0, 'failed': 0, 'not_applicable': 0}
    for control in controls:
        status = control.get('status', '').lower()
        if status == 'passed':
            summary['passed'] += 1
        elif status == 'failed':
            summary['failed'] += 1
        elif status == 'not applicable':
            summary['not_applicable'] += 1
    return summary


def overall_compliance(controls: List[Dict[str, str]]) -> float:
    """
    Calculates overall compliance score from a list of controls.

    Args:
        controls (List[Dict[str, str]]): List of controls with 'status' key.

    Returns:
        float: Compliance score as a percentage.
    """
    summary = get_control_summary(controls)
    total = summary['passed'] + summary['failed']
    return calculate_compliance_score(summary['passed'], total)


def get_non_compliant_controls(controls: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Returns a list of controls that are not compliant.

    Args:
        controls (List[Dict[str, str]]): List of controls with 'status' key.

    Returns:
        List[Dict[str, str]]: List of non-compliant controls.
    """
    return [control for control in controls if not is_compliant(control.get('status', ''))]


def compliance_report(controls: List[Dict[str, str]]) -> Dict[str, Optional[float]]:
    """
    Generates a compliance report with score and summary.

    Args:
        controls (List[Dict[str, str]]): List of controls with 'status' key.

    Returns:
        Dict[str, Optional[float]]: Report with 'score' and summary counts.
    """
    summary = get_control_summary(controls)
    score = overall_compliance(controls)
    return {
        'score': score,
        'passed': summary['passed'],
        'failed': summary['failed'],
        'not_applicable': summary['not_applicable'],
        'total': len(controls)
    }