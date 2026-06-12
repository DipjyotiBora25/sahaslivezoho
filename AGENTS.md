# AGENTS

## Purpose
This file gives AI coding agents a quick starting point for the `SaahasInsightsHub` repository.

## Repository summary
- Likely a Node.js / JavaScript project, based on `package-lock.json` in the root.
- Primary work should be centered on the root `package.json`, source directories, and package scripts.

## Startup behavior
1. Inspect the root `package.json` first.
2. Run `npm install` before making any changes.
3. Use `npm run` scripts for build/test commands only after confirming them from `package.json`.

## Recommended workflow for AI agents
- Identify the framework and runtime by examining `package.json` dependencies:
  - look for React, Next.js, Express, NestJS, or other major packages.
- Locate source files in `src/`, `app/`, `server/`, or `components/`.
- Prefer making minimal, well-scoped changes.
- When uncertain, ask the user for the relevant project area instead of guessing.

## Helpful notes
- If `package.json` contains scripts like `build`, `start`, or `test`, use those exact commands.
- Avoid hardcoding assumptions about the tech stack without checking the repository files.
- Keep documentation linked rather than duplicated.

## When in doubt
- Search the repository for `package.json`, `tsconfig.json`, `next.config.js`, or `README.md`.
- Use the existing documentation files instead of adding duplicate architecture descriptions.
