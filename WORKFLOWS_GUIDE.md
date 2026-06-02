# Advanced Workflows Guide

This guide provides deeper insights into the agentic workflows in this repository and how to create your own.

## Understanding Agentic Patterns

### 1. Event-Driven Automation

Workflows respond to GitHub events automatically:

```yaml
on:
  pull_request:
    types: [opened, synchronize]
  issues:
    types: [opened, edited]
```

### 2. Context-Aware Decision Making

Workflows analyze context and make intelligent decisions:

```javascript
const title = context.payload.issue.title.toLowerCase();
if (title.includes('bug')) {
  // Take action for bugs
}
```

### 3. Feedback and Communication

Workflows provide feedback through comments and labels:

```javascript
await github.rest.issues.createComment({
  owner: context.repo.owner,
  repo: context.repo.repo,
  issue_number: context.issue.number,
  body: 'Your feedback message here'
});
```

## Common Patterns

### Pattern 1: Content Analysis

Analyze PR or issue content to make decisions:

```javascript
const { data: files } = await github.rest.pulls.listFiles({
  owner: context.repo.owner,
  repo: context.repo.repo,
  pull_number: context.issue.number,
});

// Analyze files
const hasTests = files.some(f => f.filename.startsWith('tests/'));
const hasSourceChanges = files.some(f => f.filename.startsWith('src/'));
```

### Pattern 2: State Management

Track and update state using labels:

```javascript
// Add label
await github.rest.issues.addLabels({
  owner: context.repo.owner,
  repo: context.repo.repo,
  issue_number: context.issue.number,
  labels: ['needs-review']
});

// Remove label
await github.rest.issues.removeLabel({
  owner: context.repo.owner,
  repo: context.repo.repo,
  issue_number: context.issue.number,
  name: 'needs-review'
});
```

### Pattern 3: Cross-Workflow Communication

Workflows can trigger other workflows:

```yaml
# Workflow A completes
- name: Trigger another workflow
  uses: peter-evans/repository-dispatch@v2
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
    event-type: custom-event

# Workflow B listens
on:
  repository_dispatch:
    types: [custom-event]
```

### Pattern 4: Conditional Execution

Run workflows based on complex conditions:

```yaml
jobs:
  my-job:
    if: |
      github.event_name == 'pull_request' &&
      contains(github.event.pull_request.labels.*.name, 'ready-for-review')
```

## Advanced Examples

### Example 1: Smart PR Assignment

Automatically assign reviewers based on changed files:

```yaml
name: Auto Assign Reviewers

on:
  pull_request:
    types: [opened, ready_for_review]

jobs:
  assign:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/github-script@v7
      with:
        script: |
          const { data: files } = await github.rest.pulls.listFiles({
            owner: context.repo.owner,
            repo: context.repo.repo,
            pull_number: context.issue.number,
          });

          // Define code owners
          const reviewers = new Set();

          for (const file of files) {
            if (file.filename.startsWith('src/')) {
              reviewers.add('backend-team-lead');
            }
            if (file.filename.startsWith('tests/')) {
              reviewers.add('qa-lead');
            }
            if (file.filename.includes('.yml')) {
              reviewers.add('devops-lead');
            }
          }

          if (reviewers.size > 0) {
            await github.rest.pulls.requestReviewers({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number,
              reviewers: Array.from(reviewers)
            });
          }
```

### Example 2: PR Size Gate

Prevent merging of very large PRs:

```yaml
name: PR Size Gate

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  check-size:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/github-script@v7
      with:
        script: |
          const { data: pr } = await github.rest.pulls.get({
            owner: context.repo.owner,
            repo: context.repo.repo,
            pull_number: context.issue.number,
          });

          const totalChanges = pr.additions + pr.deletions;
          const threshold = 500;

          if (totalChanges > threshold) {
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: `⚠️ This PR has ${totalChanges} changes, which exceeds the recommended limit of ${threshold}. Consider breaking it into smaller PRs for easier review.`
            });

            // Add label
            await github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              labels: ['size/XL']
            });

            // Request changes
            await github.rest.pulls.createReview({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number,
              event: 'REQUEST_CHANGES',
              body: 'Please break this into smaller PRs.'
            });
          }
```

### Example 3: Changelog Generator

Automatically update changelog from merged PRs:

```yaml
name: Update Changelog

on:
  pull_request:
    types: [closed]
    branches: [main]

jobs:
  update-changelog:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Update CHANGELOG
      uses: actions/github-script@v7
      with:
        script: |
          const fs = require('fs');
          const pr = context.payload.pull_request;

          // Determine change type from labels
          let changeType = 'Changed';
          const labels = pr.labels.map(l => l.name);

          if (labels.includes('bug')) changeType = 'Fixed';
          else if (labels.includes('enhancement')) changeType = 'Added';
          else if (labels.includes('breaking')) changeType = 'Breaking';

          // Read current changelog
          let changelog = fs.readFileSync('CHANGELOG.md', 'utf8');

          // Get date
          const date = new Date().toISOString().split('T')[0];

          // Create entry
          const entry = `- ${changeType}: ${pr.title} (#${pr.number})\n`;

          // Insert at top of changelog (after header)
          const lines = changelog.split('\n');
          const insertIndex = lines.findIndex(l => l.startsWith('## ')) || 2;
          lines.splice(insertIndex, 0, entry);

          // Write back
          fs.writeFileSync('CHANGELOG.md', lines.join('\n'));

          console.log('Changelog updated');
```

### Example 4: Issue Triage Bot

Automatically triage issues based on content:

```yaml
name: Issue Triage

on:
  issues:
    types: [opened]

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/github-script@v7
      with:
        script: |
          const issue = context.payload.issue;
          const body = (issue.body || '').toLowerCase();
          const title = (issue.title || '').toLowerCase();
          const text = title + ' ' + body;

          const actions = [];

          // Check for required information
          const hasSteps = body.includes('steps to reproduce');
          const hasExpected = body.includes('expected') || body.includes('should');
          const hasActual = body.includes('actual') || body.includes('instead');

          if (text.includes('bug') && (!hasSteps || !hasExpected || !hasActual)) {
            actions.push({
              type: 'comment',
              body: `👋 Thanks for the bug report! To help us resolve this quickly, please provide:\n\n- [ ] Steps to reproduce\n- [ ] Expected behavior\n- [ ] Actual behavior\n- [ ] Your environment (OS, Python version, etc.)`
            });
            actions.push({
              type: 'label',
              labels: ['needs-more-info']
            });
          }

          // Check for feature requests
          if (text.includes('feature') || text.includes('enhancement')) {
            actions.push({
              type: 'comment',
              body: `💡 Thanks for the feature request! We'll review this and consider it for future releases.`
            });
            actions.push({
              type: 'label',
              labels: ['enhancement', 'needs-triage']
            });
          }

          // Check for questions
          if (text.includes('how') || text.includes('question')) {
            actions.push({
              type: 'comment',
              body: `❓ This looks like a question. Have you checked our [documentation](link) and [FAQ](link)?`
            });
            actions.push({
              type: 'label',
              labels: ['question']
            });
          }

          // Execute actions
          for (const action of actions) {
            if (action.type === 'comment') {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                body: action.body
              });
            } else if (action.type === 'label') {
              await github.rest.issues.addLabels({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                labels: action.labels
              });
            }
          }
```

## Best Practices

### 1. Use Permissions Wisely

Always specify minimum required permissions:

```yaml
jobs:
  my-job:
    permissions:
      issues: write
      pull-requests: read
      contents: read
```

### 2. Handle Errors Gracefully

```javascript
try {
  await github.rest.issues.createComment({...});
} catch (error) {
  console.error('Failed to create comment:', error);
  // Don't fail the workflow for non-critical errors
}
```

### 3. Avoid Rate Limits

```javascript
// Batch operations when possible
const labels = ['bug', 'priority-high'];
await github.rest.issues.addLabels({
  labels: labels  // Add multiple at once
});

// Add delays for multiple operations
await new Promise(resolve => setTimeout(resolve, 1000));
```

### 4. Test Workflows Locally

Use [act](https://github.com/nektos/act) to test workflows locally:

```bash
# Install act
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Test a workflow
act pull_request -e test-event.json
```

### 5. Use Concurrency Controls

Prevent multiple workflow runs from interfering:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### 6. Cache Dependencies

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

## Debugging Tips

### 1. Enable Debug Logging

Set repository secrets:
- `ACTIONS_RUNNER_DEBUG`: true
- `ACTIONS_STEP_DEBUG`: true

### 2. Inspect Context

```javascript
console.log('Event:', JSON.stringify(context.payload, null, 2));
console.log('Actor:', context.actor);
console.log('Repo:', context.repo);
```

### 3. Use Step Outputs

```yaml
- id: check-files
  run: echo "has_tests=true" >> $GITHUB_OUTPUT

- name: Use output
  if: steps.check-files.outputs.has_tests == 'true'
  run: echo "Tests found!"
```

## Security Considerations

### 1. Don't Trust User Input

```javascript
// BAD: Directly using user input
const command = `echo ${issue.title}`;

// GOOD: Sanitize or validate first
const title = issue.title.replace(/[^a-zA-Z0-9 ]/g, '');
```

### 2. Limit Permissions

Use fine-grained permissions, not `write-all`.

### 3. Protect Secrets

Never log secrets or tokens.

### 4. Validate Webhook Signatures

For custom webhooks, always validate signatures.

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub REST API](https://docs.github.com/en/rest)
- [Octokit.js Documentation](https://octokit.github.io/rest.js/)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [GitHub Script Action](https://github.com/actions/github-script)

## Contributing Patterns

Share your own agentic patterns! Create an issue or PR with:
1. Pattern name and description
2. Use case / problem it solves
3. Implementation code
4. Example output / behavior

Happy automating! 🤖
