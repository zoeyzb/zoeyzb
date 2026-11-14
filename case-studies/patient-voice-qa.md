# Patient Voice QA — synthetic voice-workflow test harness

**Visibility:** private implementation; this case study describes the engineering design without publishing telephony credentials, test destinations or any real patient information.

## Purpose

The harness evaluates how a voice workflow handles repeatable, fictional clinic scenarios. It is designed to produce reviewable evidence rather than treating a completed phone call or an AI-generated summary as proof of correctness.

## Architecture

- A scenario library defines ten fictional-patient workflows.
- A LiveKit Agents worker runs a synthetic patient using Deepgram speech-to-text, a text-only Groq model and Deepgram text-to-speech.
- A controller validates explicit live-call settings and waits for both the agent and a receive-only recorder before initiating a test call.
- The recorder captures the two audio sides separately and exports aligned audio artifacts.
- Transcript and session metrics are retained with timestamps and speaker roles.
- A deterministic evaluator checks selected high-risk behaviors and accepts findings only when an exact quote, speaker and timestamp can be traced to the source transcript.

## Engineering emphasis

The project focuses on trust boundaries, safe failure handling, repeatable scenarios, artifact integrity, transcript provenance and avoiding unsupported QA claims. Live calls are opt-in and may incur provider charges; uncertain calls are not automatically retried.

## Verification boundary

The repository documents local/offline validation and an automated test suite. Its own completion criteria explicitly separate that work from live-call validation: ten real calls with valid recordings and transcripts are required before the live assessment is considered complete. This case study does not claim that live-call milestone has been met.
