# Use Oracle Cloud Free Tier

## Status

Accepted

## Date

2026-09-27

## Deciders

Robby Kamil

## Context

The project needs a publicly accessible server for deployment. As this is a personal portfolio project with no operational budget, any recurring monthly cost is not an option.

## Alternatives

### AWS

Pros:
- Popular, widely documented, large community support

Cons:
- Free tier is limited to 12 months, after which charges apply
- Easy to accidentally incur costs if usage exceeds free tier limits

### GCP

Pros:
- Comprehensive suite of services

Cons:
- Requires a credit card even for the free trial/credit
- Free credit expires after a limited period, then billing begins

### Oracle Cloud Free Tier

Pros:
- Free indefinitely (no time limit, unlike AWS/GCP free tiers)
- Includes "Always Free" VM instances at no cost

Cons:
- Limited compute resources (constrained CPU/RAM on Always Free VMs)
- Always Free VM capacity is not always available in every region, which can require retrying provisioning or choosing a different region

## Decision

We chose Oracle Cloud Free Tier.

Since this is a personal portfolio project without a budget for ongoing infrastructure costs, avoiding recurring charges is a priority. AWS and GCP free offerings are time-limited and can lead to unexpected billing, whereas Oracle Cloud's Always Free tier has no expiration. The trade-off of limited compute resources is acceptable, since the project's workload is a lightweight monitoring application rather than a resource-intensive service.

## Consequences

Positive:
- No monthly hosting cost
- Server remains free indefinitely under current Oracle Cloud policy

Negative:
- Limited CPU and RAM restrict the application to lightweight workloads
- May require careful resource optimization (e.g., avoiding heavy background processes) to stay within Always Free limits
- Provisioning a new Always Free VM may occasionally fail due to regional capacity constraints
