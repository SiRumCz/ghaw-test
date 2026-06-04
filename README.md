# GitHub Agentic Workflow Playground

Welcome to your GitHub Agentic Workflow (GHAW) testing playground! This repository is designed to help you learn and experiment with automated GitHub Actions workflows that behave like agents, autonomously managing various aspects of your repository.

## What are Agentic Workflows?

Agentic workflows are automated GitHub Actions that act autonomously to:
- Review and analyze pull requests
- Automatically label issues and PRs
- Manage issue lifecycles
- Enforce code quality standards
- Auto-merge approved changes
- Provide feedback and suggestions

Think of them as "agents" that help maintain and improve your repository without constant human intervention.

## Repository Structure

```
ghaw-test/
├── src/                          # Source code
│   ├── __init__.py
│   └── calculator.py             # Calculator module (11 operations)
├── tests/                        # Test files (one file per function)
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_abs.py
│   ├── test_add.py
│   ├── test_clamp.py
│   ├── test_divide.py
│   ├── test_integer_divide.py
│   ├── test_modulo.py
│   ├── test_multiply.py
│   ├── test_power.py
│   ├── test_round_to.py
│   ├── test_sqrt.py
│   └── test_subtract.py
├── .github/
│   ├── workflows/                # GitHub Actions workflows
│   │   ├── ci.yml                # Continuous Integration
│   │   ├── auto-label.yml        # Auto-labeling PRs and issues
│   │   ├── auto-review.yml       # Automated PR reviews
│   │   ├── issue-manager.yml     # Issue lifecycle management
│   │   ├── pr-auto-merge.yml     # Auto-merge approved PRs
│   │   ├── code-quality.yml      # Code quality checks
│   │   ├── daily-repo-status.md  # AI agentic: daily status report (5am ET)
│   │   ├── issue-polisher.md     # AI agentic: structures & labels new issues
│   │   └── issue-resolver.md     # AI agentic: implements fixes and opens PRs
│   └── labeler.yml               # Configuration for auto-labeling
├── pyproject.toml                # Project metadata & dependencies (uv)
├── WORKFLOWS_GUIDE.md            # Advanced agentic workflows guide
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## Calculator Module

The sample `src/calculator.py` module provides 11 arithmetic operations used to
exercise the workflows:

| Function | Description |
| --- | --- |
| `add(a, b)` | Add two numbers |
| `subtract(a, b)` | Subtract `b` from `a` |
| `multiply(a, b)` | Multiply two numbers |
| `divide(a, b)` | Divide `a` by `b` (raises on divide by zero) |
| `power(base, exponent)` | Raise `base` to `exponent` |
| `modulo(a, b)` | Remainder of `a / b` (raises on modulo by zero) |
| `integer_divide(a, b)` | Floor division of `a` by `b` (raises on divide by zero) |
| `sqrt(n)` | Square root of `n` (raises on negatives) |
| `abs(n)` | Absolute value of `n` |
| `clamp(n, min_value, max_value)` | Constrain `n` to `[min_value, max_value]` |
| `round_to(n, decimals)` | Round `n` to `decimals` places (half-up) |

## Workflows Overview

### 1. CI (Continuous Integration)
**File:** `.github/workflows/ci.yml`

Automatically runs tests whenever code is pushed or a PR is opened.

**Features:**
- Tests across multiple Python versions (3.9, 3.10, 3.11)
- Runs test suite with coverage reporting
- Uploads coverage reports to Codecov

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop`

**To test:** Push code or create a PR and watch the tests run!

### 2. Auto Label
**File:** `.github/workflows/auto-label.yml`

Automatically labels PRs and issues based on their content and changed files.

**Features:**
- Labels PRs by file paths (e.g., `python`, `tests`, `documentation`)
- Labels PRs by size (XS, S, M, L, XL)
- Labels issues by keywords (e.g., `bug`, `enhancement`, `question`)

**Triggers:**
- When PRs are opened, edited, or synchronized
- When issues are opened or edited

**To test:**
- Create an issue with "bug" in the title → gets labeled as `bug`
- Create a PR modifying Python files → gets labeled as `python`

### 3. Auto Review
**File:** `.github/workflows/auto-review.yml`

Reviews PRs automatically and provides feedback.

**Features:**
- Checks if new source files have corresponding tests
- Flags large files (>300 lines added)
- Warns when test files are removed
- Provides PR statistics summary

**Triggers:**
- When PRs are opened, synchronized, or reopened

**To test:**
- Create a PR adding a new file in `src/` without tests
- Create a PR with large changes

### 4. Issue Manager
**File:** `.github/workflows/issue-manager.yml`

Manages the lifecycle of issues.

**Features:**
- Greets new issue creators and mentions the issue-polisher will auto-format the issue
- Special greeting for first-time contributors
- Automatically closes stale issues (60 days inactive)
- Warns before closing (7 day grace period)

**Triggers:**
- When issues are opened
- Daily at midnight UTC (for stale check)

**To test:**
- Create an issue and see the greeting
- Issues marked stale after 60 days of inactivity

### 5. PR Auto Merge
**File:** `.github/workflows/pr-auto-merge.yml`

Automatically merges approved PRs under certain conditions.

**Features:**
- Auto-merges Dependabot PRs when checks pass
- Auto-approves minor/patch version updates
- Verifies all checks pass before merging

**Triggers:**
- When PRs are labeled/unlabeled
- When PR reviews are submitted
- When check suites complete

**To test:**
- Wait for Dependabot PRs (if enabled)
- Or modify the script to test with your own PRs

### 6. Code Quality
**File:** `.github/workflows/code-quality.yml`

Checks code quality using linting and formatting tools.

**Features:**
- Black: Code formatting checker
- isort: Import sorting checker
- Flake8: Python linting
- Comments on PR with results and fix instructions

**Triggers:**
- Pull requests to `main` or `develop`

**To test:**
- Create a PR with poorly formatted code
- See automated comments with fix suggestions

### AI Agentic Workflows

In addition to the script-based workflows above, this repository includes
AI-powered agentic workflows built with [gh-aw](https://github.com/githubnext/gh-aw)
and Claude. Each is defined by a Markdown spec (`*.md`) that is compiled into a
generated `*.lock.yml` workflow.

- **Daily Repo Status** (`daily-repo-status.md`) — posts a daily digest issue
  at 5am Toronto time (9am UTC) summarizing PRs, commits, open issues, and
  suggested next steps.
- **Issue Polisher** (`issue-polisher.md`) — triggers on every new issue;
  restructures the body into a bug/feature/question template, adds an expected
  unit test section, and applies a `bug` or `feature` label.
- **Issue Resolver** (`issue-resolver.md`) — runs hourly; picks an open
  `bug` or `feature` issue, implements a complete fix with tests, and opens a
  pull request that closes it.

See [`WORKFLOWS_GUIDE.md`](WORKFLOWS_GUIDE.md) for a deeper dive into agentic
patterns and how to build your own.

## Getting Started

### 1. Clone and Set Up Locally

This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies and
the virtual environment.

```bash
# Clone the repository
git clone https://github.com/SiRumCz/ghaw-test.git
cd ghaw-test

# Install dependencies (creates a managed virtual environment)
uv sync
```

### 2. Run Tests Locally

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=term-missing
```

### 3. Test Workflows

#### Method 1: Create Issues
1. Go to the Issues tab on GitHub
2. Create a new issue with different keywords:
   - Include "bug" → auto-labeled as `bug`
   - Include "feature" → auto-labeled as `enhancement`
   - Include "help" → auto-labeled as `question`

#### Method 2: Create Pull Requests
1. Create a new branch:
   ```bash
   git checkout -b test-workflow
   ```

2. Make some changes:
   ```bash
   # Add a new function to src/calculator.py
   # Or modify existing code
   ```

3. Commit and push:
   ```bash
   git add .
   git commit -m "Test: adding new feature"
   git push origin test-workflow
   ```

4. Create a PR on GitHub and watch the workflows run!

#### Method 3: Test Different Scenarios

**Scenario A: Missing Tests**
- Add a new file `src/new_module.py`
- Create PR without adding `tests/test_new_module.py`
- Auto-review will flag this

**Scenario B: Large Changes**
- Make a file with >300 line additions
- Auto-review will flag it as too large

**Scenario C: Code Quality Issues**
- Write poorly formatted code
- Code quality workflow will comment with fixes

## Workflow Permissions

Some workflows require specific permissions to function. If you encounter issues:

1. Go to Settings → Actions → General
2. Under "Workflow permissions", select:
   - "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"

## Customization

### Modify Workflow Behavior

All workflows are in `.github/workflows/`. You can:
- Adjust triggers (on push, PR, schedule, etc.)
- Modify conditions and logic
- Add new checks or features
- Change notification messages

### Example: Modify Auto-Label Logic

Edit `.github/workflows/auto-label.yml`:

```yaml
# Add new keyword detection
if (text.includes('security')) {
  labels.push('security');
}
```

### Example: Change Stale Issue Duration

Edit `.github/workflows/issue-manager.yml`:

```yaml
days-before-stale: 30  # Changed from 60
days-before-close: 3   # Changed from 7
```

## Learning Resources

### GitHub Actions Basics
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [GitHub Script Action](https://github.com/actions/github-script)

### Agentic Patterns
- **Event-driven**: Workflows trigger on specific events
- **Autonomous decision-making**: Scripts analyze and make decisions
- **Feedback loops**: Workflows provide comments and suggestions
- **State management**: Track and manage issue/PR lifecycle

### Advanced Topics
- [Creating custom actions](https://docs.github.com/en/actions/creating-actions)
- [Using secrets and variables](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Workflow artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)

## Troubleshooting

### Workflows Not Running?
1. Check if Actions are enabled: Settings → Actions → General
2. Verify branch protection rules don't block workflows
3. Check workflow file syntax with yamllint

### Permission Errors?
1. Update workflow permissions in repository settings
2. Check GITHUB_TOKEN permissions in workflow files

### Debugging Workflows
1. Add debug output:
   ```yaml
   - run: echo "Debug: ${{ toJson(github.event) }}"
   ```
2. Use `actions/github-script` to inspect context:
   ```javascript
   console.log(JSON.stringify(context, null, 2));
   ```

## Contributing

This is your playground! Feel free to:
- Experiment with workflow modifications
- Add new agentic patterns
- Break things and learn from them
- Share interesting discoveries

## Next Steps

1. **Explore existing workflows**: Read through each workflow file to understand how they work
2. **Create test issues/PRs**: Trigger the workflows and observe their behavior
3. **Modify workflows**: Experiment with changes and see the results
4. **Create new workflows**: Implement your own agentic patterns
5. **Combine workflows**: Make workflows interact with each other

## Example Use Cases to Try

1. **Auto-assign reviewers** based on changed files
2. **Track PR review time** and comment if reviews are slow
3. **Auto-close PRs** that haven't been updated in X days
4. **Create issues** from failing CI runs
5. **Generate release notes** automatically from merged PRs
6. **Welcome new contributors** with a custom message
7. **Request more info** on incomplete bug reports

## Questions?

This is a learning environment - experiment freely! Check the [GitHub Actions documentation](https://docs.github.com/en/actions) for more information.

Happy learning! 🚀
