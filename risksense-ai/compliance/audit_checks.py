from datetime import datetime

# audit_checks.py
# Performs audit checks for compliance
def perform_audit_checks(data):
    """
    Perform audit checks on the provided data.

    Args:
        data (dict): The data to audit.

    Returns:
        dict: Results of the audit checks.
    """
    results = {}
    # Check for required fields
    required_fields = ['user_id', 'timestamp', 'action']
    missing_fields = [field for field in required_fields if field not in data]
    results['missing_fields'] = missing_fields
    results['all_fields_present'] = len(missing_fields) == 0

    # Validate timestamp format and check if it's not in the future
    timestamp_str = data.get('timestamp', '')
    try:
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S')
        results['timestamp_valid'] = True
        results['timestamp_in_future'] = timestamp > datetime.utcnow()
    except (ValueError, TypeError):
        results['timestamp_valid'] = False
        results['timestamp_in_future'] = None

    # Action is allowed and not deprecated
    allowed_actions = ['login', 'logout', 'update', 'delete']
    deprecated_actions = ['delete']
    action = data.get('action')
    results['action_allowed'] = action in allowed_actions
    results['action_deprecated'] = action in deprecated_actions

    # User ID format check (example: must be alphanumeric and at least 5 chars)
    user_id = data.get('user_id', '')
    results['user_id_valid'] = user_id.isalnum() and len(user_id) >= 5

    # Optional: Check for extra fields
    extra_fields = [field for field in data if field not in required_fields]
    results['extra_fields'] = extra_fields

    return results