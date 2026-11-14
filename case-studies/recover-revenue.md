# Recover Revenue — full-stack growth system

**Visibility:** private implementation with a public-facing website at [recoverrevenue.company](https://recoverrevenue.company).

## Product problem

Small businesses need more than a brochure site. They need a coherent path from being discovered, to understanding the offer, to making an inquiry, and then to having that inquiry handled reliably.

## System scope

The implementation combines a public acquisition experience with an internal operating system:

- Public marketing routes for services, industries and educational resources.
- A guided buyer funnel that captures business context, goals and a suitable next step.
- Lead discovery and qualification workflows, evidence-backed website audits, outreach planning and follow-up.
- Owner-facing CRM and pipeline views for leads, opportunities, communications and work status.
- Voice and appointment-related workflows with explicit state, attribution and retry boundaries.
- SEO/search structure, analytics, conversion measurement and operational health checks.
- Human-review gates, idempotency, quotas, logs and audit trails around consequential actions.

## Engineering

The inspected workspace contains a Next.js 16 / React 19 / TypeScript application, SQL and Supabase-related data layers, worker and service modules, and a Vitest-based test suite. The repository build script defines type-checking, tests, linting and a Next.js production build as its quality gates.

## Verification snapshot

On November 14, 2026, the existing local workspace ran `npm test` successfully:

- **173 test files passed**
- **802 tests passed**
- Exit code: **0**

This is a local test result for the inspected workspace. It is not a claim that every external integration or production workflow has been independently revalidated in this profile audit.

## Privacy and boundaries

The source repository remains private. This case study intentionally excludes API keys, environment files, customer records, internal credentials and private operational data. The public website is the externally viewable entry point; the internal owner system and automation code are not published.
