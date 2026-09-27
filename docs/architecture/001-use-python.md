# Use Python as Primary Programming Language

## Status

Accepted

## Date

2026-09-27

## Deciders

Robby Kamil

## Context

The project requires CPU, memory, and disk monitoring, log parsing, and notification delivery.

The chosen language must be:

- Easy to learn
- Well-supported by monitoring libraries
- Capable of integrating with notification services
- Suitable for automation

## Alternatives

### Python

Pros:
- `psutil` is available
- `requests` is available
- Simple syntax

Cons:
- Slower compared to Go
- Global Interpreter Lock (GIL) limits true multi-threaded concurrency
- Higher memory overhead when running multiple monitoring processes
- Requires careful dependency/environment management (virtualenv, requirement pinning)

### Go

Pros:
- Lightweight binary
- High performance

Cons:
- Not yet familiar to the team
- Steeper learning curve

## Decision

We chose Python.

Monitoring tasks in this project are interval-based (periodic polling of CPU, memory, and disk metrics) rather than real-time or latency-critical, so Python's performance overhead compared to Go is acceptable. The availability of mature libraries (`psutil`, `requests`) and the team's familiarity with Python significantly reduce development time and maintenance effort, which outweighs the raw performance advantage Go would offer.

## Consequences

Positive:
- Faster development
- Easier to learn

Negative:
- Performance not as strong as Go
