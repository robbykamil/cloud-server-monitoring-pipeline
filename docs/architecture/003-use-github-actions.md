# Use GitHub Actions for CI Pipeline

## Status

Accepted

## Date

2026-09-27

## Deciders

Robby Kamil

## Context

Every code change needs to be verified (tests, linting, build checks) before it is merged or deployed. As the project grows and commits become more frequent, relying on manual verification increases the risk of human error, such as forgetting to run tests before merging.

## Alternatives

### Manual Testing

Pros:
- Simple, no setup required

Cons:
- Prone to being forgotten or skipped
- Not scalable as the codebase and team grow
- No consistent record of what was tested and when

### Jenkins

Pros:
- Very flexible and highly configurable

Cons:
- Requires a dedicated server to host and maintain
- More complex initial setup compared to SaaS CI tools
- Additional operational overhead (updates, security patches, uptime)

### GitHub Actions

Pros:
- Free for public repositories (and includes free minutes for private repos)
- Natively integrated with GitHub (triggers, pull requests, checks)
- Easy to configure with YAML-based workflows

Cons:
- Usage limits apply (build minutes for private repositories)
- Vendor lock-in to GitHub's ecosystem

## Decision

We chose GitHub Actions.

Manual testing does not scale reliably and introduces the risk of human error, while Jenkins requires maintaining a separate server, adding operational overhead that is unnecessary for a project of this size. GitHub Actions provides automated verification directly integrated with the existing GitHub repository, with no additional infrastructure to manage, making it the most practical choice for this project's current scale and needs.

## Consequences

Positive:
- Automated testing on every push and pull request
- No additional server or infrastructure to maintain

Negative:
- Requires learning YAML-based workflow syntax
- Debugging failed workflows can be less straightforward than running tests locally
- Usage is subject to GitHub's build-minute limits if the project scales significantly# Use GitHub Actions for CI Pipeline

## Status

Accepted

## Date

2026-09-27

## Deciders

Robby Kamil

## Context

Every code change needs to be verified (tests, linting, build checks) before it is merged or deployed. As the project grows and commits become more frequent, relying on manual verification increases the risk of human error, such as forgetting to run tests before merging.

## Alternatives

### Manual Testing

Pros:
- Simple, no setup required

Cons:
- Prone to being forgotten or skipped
- Not scalable as the codebase and team grow
- No consistent record of what was tested and when

### Jenkins

Pros:
- Very flexible and highly configurable

Cons:
- Requires a dedicated server to host and maintain
- More complex initial setup compared to SaaS CI tools
- Additional operational overhead (updates, security patches, uptime)

### GitHub Actions

Pros:
- Free for public repositories (and includes free minutes for private repos)
- Natively integrated with GitHub (triggers, pull requests, checks)
- Easy to configure with YAML-based workflows

Cons:
- Usage limits apply (build minutes for private repositories)
- Vendor lock-in to GitHub's ecosystem

## Decision

We chose GitHub Actions.

Manual testing does not scale reliably and introduces the risk of human error, while Jenkins requires maintaining a separate server, adding operational overhead that is unnecessary for a project of this size. GitHub Actions provides automated verification directly integrated with the existing GitHub repository, with no additional infrastructure to manage, making it the most practical choice for this project's current scale and needs.

## Consequences

Positive:
- Automated testing on every push and pull request
- No additional server or infrastructure to maintain

Negative:
- Requires learning YAML-based workflow syntax
- Debugging failed workflows can be less straightforward than running tests locally
- Usage is subject to GitHub's build-minute limits if the project scales significantly
