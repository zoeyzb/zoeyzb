# NextRole — job-search and application workspace

**Visibility:** private source; a deployed product preview is available at [next-role-web-nine.vercel.app](https://next-role-web-nine.vercel.app/).

## Product problem

A serious job search spans job discovery, résumé tailoring, application preparation, follow-ups and interview tracking. NextRole brings those steps into one workspace rather than treating each application as a disconnected form.

## Product scope

- Import and organize job postings.
- Search and evaluate roles against a candidate's goals and experience.
- Prepare role-specific résumés, cover letters and application materials.
- Track each opportunity from first review through application and follow-up.
- Keep automated steps review-first, with the candidate retaining control over external submissions.
- Support browser-based workflows, document handling and provider configuration.
- Keep user data, authentication, storage and application state separated by account.

## Engineering

The inspected codebase combines a Python application/API layer with a React and TypeScript web client. Its dependency manifests and deployment documentation show PostgreSQL-backed services, Neon and Supabase integrations, object storage, authentication, browser automation and AI-provider adapters.

The repository contains a substantial automated test suite and dedicated deployment, integration, reliability and production-acceptance documentation. Those documents also distinguish implemented behavior from external services that still require credentials or operational setup.

## Status and boundaries

NextRole is in active development. A deployed preview does not mean every external job board, AI provider or browser workflow is universally available; those capabilities depend on configured services and their current access policies. The source remains private, so this public case study describes architecture and product behavior without exposing implementation details, credentials or user data.
