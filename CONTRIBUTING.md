# Contributing to Security Lab Pro

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## How to Contribute

### Reporting Bugs
- Use GitHub Issues
- Include system information (OS, version)
- Provide reproduction steps
- Include relevant logs

### Suggesting Features
- Open a GitHub Discussion
- Explain the use case
- Describe expected behavior

### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Add tests if applicable
5. Run tests: `pytest tests/`
6. Commit: `git commit -m 'Add feature: description'`
7. Push: `git push origin feature/your-feature`
8. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/yourusername/security-lab-pro.git
cd security-lab-pro
pip3 install -r requirements-dev.txt
```

## Coding Standards
- Follow PEP 8 for Python
- Use shellcheck for bash scripts
- Write descriptive commit messages
- Add comments for complex logic
- Update documentation

## Testing
- Add unit tests for new features
- Run full test suite before PR
- Test on Ubuntu 22.04 LTS

## Questions?
Join our Discord or open a GitHub Discussion.
