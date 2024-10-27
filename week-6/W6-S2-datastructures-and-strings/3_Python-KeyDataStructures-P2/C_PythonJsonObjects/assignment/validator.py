import jsonschema

# Define a schema with nested objects
global_schema = {
    # we validate an object
    "type": "object",
    # these are our keys
    "properties": {
        "company": {
            # we validate an object
            "type": "object",
            # keys to validate inside company
            "properties": {
                "name": {"type": "string"}, # company name
                "location": {"type": "string"}, # company location
                "departments": {
                    "type": "array",
                    "items": {
                        # our depts are objects themselves
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}, # dept name
                            "employees": {
                                "type": "array", # employees is an array
                                "items": {
                                    "type": "object", # each employee is an object
                                    "properties": {
                                        "name": {"type": "string"},
                                        "age": {"type": "integer"},
                                        "role": {"type": "string"},
                                    },
                                    # "additionalProperties": False,
                                    # name, age and role are required for a person
                                    "required": ["name", "age", "role"],
                                },
                            },
                        },
                        "additionalProperties": False,
                        # a dept must have a name and employees
                        "required": ["name", "employees"],
                    },
                }, # company dept - array
            },
            # can't add more properties
            "additionalProperties": False,
            # company must have a name, location and depts
            "required": ["name", "location", "departments"],
        },
        
        "products": {
            "type": "array",
            "items": {
                # each item is an object
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "category": {"type": "string"},
                    "price": {"type": "number"},
                    # features of a product are contained in an object
                    "features": {
                        "type": "object",
                        # each feature has a battery, water resistance rating, health tracking
                        "properties": {
                            # as some features have different values, I don't type validate here
                        },
                    },
                },
                "additionalProperties": False,
                # product properties must have id, name, categ, price but maybe no features
                "required": ["id", "name", "category", "price"],
            }
        },
        
        "financials": {
            "properties": {
                "revenue": {"type": "number"},
                "expenses": {"type": "number"},
                "profit": {"type": "number"},
                "year": {"type": "number"},
            },
            "additionalProperties": False,
            # financials will have the below
            "required": ["revenue", "expenses", "profit", "year"],
        },
    },
    "additionalProperties": False,
    # must specify the company
    "required": ["company"],
}

def valid_data(data, schema=global_schema):
    try:
        jsonschema.validate(data, schema=schema)
    except jsonschema.exceptions.ValidationError:
        raise Exception("[FATAL] Invalid JSON data")
    except jsonschema.exceptions.SchemaError:
        raise Exception("[FATAL] Invalid JSON Schema definition")
