import jsonschema
from jsonschema import validate, ValidationError

# schema_validator.py
# Validates data schema for incoming data
class SchemaValidator:
    def __init__(self, schema: dict):
        if not isinstance(schema, dict):
            raise TypeError("Schema must be a dictionary.")
        self.schema = schema

    def validate(self, data: dict) -> bool:
        if not isinstance(data, dict):
            raise TypeError("Data to validate must be a dictionary.")
        try:
            validate(instance=data, schema=self.schema)
            return True
        except ValidationError as e:
            # Optionally log the error with details for debugging
            # logger.error(f"Schema validation error: {e.message}")
            return False
        except jsonschema.SchemaError as e:
            # Handle invalid schema definitions
            # logger.error(f"Invalid schema: {e.message}")
            return False