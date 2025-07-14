# Rootly Python SDK

This is a Python SDK for the Rootly API v1.

## Project Structure

- `rootly_sdk/` - Main SDK package
  - `client.py` - HTTP client implementation
  - `errors.py` - Error definitions
  - `models/` - Generated API models
  - `api/` - API endpoints
  - `types.py` - Type definitions

## Dependencies

- Python 3.9+
- httpx (HTTP client)
- attrs (data classes)
- python-dateutil (date parsing)

## Development

- Uses Poetry for dependency management
- Follows Ruff linting rules (line length 120, select F/I/UP)
- Generated from OpenAPI specification

## Testing

To test the SDK imports correctly:
```bash
python -c "import rootly_sdk; print('SDK imports successfully')"
```

## Building

Uses Poetry build system with `poetry-core` backend.