# MVP Scope

## Date

2026-09-29

## Deciders

Robby Kamil

## Overview

This document defines what is included in the current MVP (MVP 1), what is planned for later MVPs, and what is explicitly out of scope for the project as a whole. It complements the architecture diagrams ([v1](system-architecture-v1.md), [v2](system-architecture-v2.md), [v3](system-architecture-v3.md)) by giving a single, quick-reference view of scope without needing to read through each diagram.

## Included (MVP 1)

- [x] CPU monitoring
- [x] Memory monitoring
- [x] Disk monitoring
- [x] Telegram alerting
- [x] Dockerized application
- [x] CI with GitHub Actions (test and build)

See [Architecture v1](system-architecture-v1.md) for details.

## Planned for Later MVPs

These are not part of MVP 1, but are already planned in the project roadmap:

- [ ] SQLite (persistence) — planned for MVP 2, see [Architecture v2](system-architecture-v2.md)
- [ ] Log parsing — planned for MVP 2, see [Architecture v2](system-architecture-v2.md)
- [ ] Alert cooldown — planned for MVP 2, see [Architecture v2](system-architecture-v2.md)
- [ ] Docker Hub image publishing — planned for MVP 3, see [Architecture v3](system-architecture-v3.md)
- [ ] Auto deployment to Oracle Cloud — planned for MVP 3, see [Architecture v3](system-architecture-v3.md)

## Out of Scope (No Current Plan)

These are not part of the roadmap for MVP 1–3. They may be considered in the future, but there is no committed plan yet:

- [ ] Slack integration
- [ ] PostgreSQL
- [ ] Grafana
- [ ] Prometheus
- [ ] Kubernetes

## Rationale

Keeping "Planned for Later MVPs" separate from "Out of Scope" makes it clear which exclusions are temporary (already scheduled in the roadmap) versus which are open-ended decisions with no current commitment. This avoids the risk of a reader assuming SQLite or Auto Deployment were rejected, when in fact they are simply sequenced into MVP 2 and MVP 3.

