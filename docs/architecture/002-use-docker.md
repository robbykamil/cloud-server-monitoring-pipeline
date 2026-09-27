# Use Docker for Packaging and Deployment

## Status

Accepted

## Date

2026-09-27

## Deciders

Robby Kamil

## Context

The application must run consistently across:

- Local laptop
- Oracle Cloud VM

## Alternatives

### Install Python Directly

Pros:
- Simple

Cons:
- Dependency versions differ between servers

### Docker

Pros:
- Portable
- Reproducible
- Aligned with DevOps best practices

Cons:
- Requires learning containerization concepts (images, containers, volumes, networking)
- Additional Dockerfile maintenance overhead
- Image build time adds to the development/deployment cycle
- Requires a container runtime (Docker daemon) to be available on every environment

## Decision

We chose Docker.

Running the application directly on the host risks dependency mismatches between the local laptop and the Oracle Cloud VM, which can lead to "works on my machine" issues. Docker packages the application and its dependencies into a single reproducible image, so the same artifact runs identically across both environments. The added complexity of learning and maintaining containers is a one-time cost, while the consistency and portability benefits apply to every deployment going forward.

## Consequences

Positive:
- Consistent deployment

Negative:
- Added complexity
