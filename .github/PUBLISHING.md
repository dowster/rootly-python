# Publishing to PyPI

This repository uses GitHub Actions to automatically publish packages to PyPI when a new version tag is pushed.

## Setup Instructions

### 1. PyPI API Token

1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Scroll to "API tokens" section
3. Click "Add API token"
4. Set the token name (e.g., "rootly-python-github-actions")
5. Set the scope to "Entire account" or specific to this project
6. Copy the generated token (starts with `pypi-`)

### 2. GitHub Repository Secrets

1. Go to your GitHub repository
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add the following secret:
   - **Name**: `PYPI_API_TOKEN`
   - **Value**: The PyPI API token from step 1

### 3. Publishing a New Version

To publish a new version:

1. **Update the changelog** (if not already done):
   ```bash
   # Edit CHANGELOG.md to add new version details
   ```

2. **Create and push a version tag**:
   ```bash
   # Create a new version tag (e.g., v1.2.3)
   git tag v1.2.3
   
   # Push the tag to trigger the workflow
   git push origin v1.2.3
   ```

3. **Monitor the workflow**:
   - Go to the "Actions" tab in your GitHub repository
   - Watch the "Publish Python 🐍 distribution 📦 to PyPI on tag" workflow run
   - The workflow will:
     - Install build tools (uv, build, twine)
     - Test the SDK imports
     - Build the package using Python build
     - Publish to PyPI using twine

### 4. Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes (e.g., `v2.0.0`)
- **MINOR**: New functionality, backward compatible (e.g., `v1.1.0`)
- **PATCH**: Bug fixes, backward compatible (e.g., `v1.0.1`)

### 5. Workflow Details

The GitHub Action workflow (`.github/workflows/publish.yml`) will:

1. **Trigger**: On any tag push (pattern `*`)
2. **Environment**: Ubuntu latest with Python 3.12
3. **Dependencies**: Install uv, build, and twine
4. **Testing**: Verify SDK imports correctly
5. **Build**: Create distribution packages using Python build
6. **Publish**: Upload to PyPI using twine with API token

### 6. Manual Publishing (Alternative)

If you need to publish manually:

```bash
# Install dependencies
poetry install

# Update version in pyproject.toml
poetry version 1.2.3

# Build the package
poetry build

# Publish to PyPI
poetry publish
```

### 7. Testing on Test PyPI

For testing the publishing process, you can use Test PyPI:

1. Create a Test PyPI account and API token
2. Add `PYPI_TEST_TOKEN` to GitHub secrets
3. Modify the workflow to use `--repository testpypi` flag

### 8. Troubleshooting

**Common Issues:**

- **Permission denied**: Ensure the `PYPI_TOKEN` secret is correctly set
- **Version conflict**: Make sure the version tag doesn't already exist on PyPI
- **Import errors**: Check that all dependencies are correctly specified in `pyproject.toml`
- **Build failures**: Verify the package structure and ensure all required files are included

**Workflow Monitoring:**
- Check the Actions tab for detailed logs
- Review the workflow output for specific error messages
- Ensure the tag format matches the expected pattern (`v*`)

## Security Notes

- Never commit PyPI tokens to the repository
- Use repository secrets for sensitive information
- Consider using environment-specific tokens for different deployment stages
- Regularly rotate API tokens for security