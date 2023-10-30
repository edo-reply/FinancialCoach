from pathlib import Path

# DB configuration
IN_MEMORY = ":memory:"
db_path = IN_MEMORY
schema_path = Path(__file__).parent.joinpath("schema.sql").resolve()
