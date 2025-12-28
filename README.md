# PolicySentinel

PolicySentinel is a system that continuously monitors policy documents, detects meaningful changes over time, and keeps AI systems aligned with the latest policy rules.

The project focuses on solving **Policy Memory Drift** — a situation where AI systems continue to reason using outdated policy information even after policies have changed.

---

## Problem

Policies in enterprises, governments, and institutions change frequently.  
Most AI systems ingest these policies once and treat them as static knowledge.

This leads to:
- Enforcement of outdated rules  
- Compliance and financial risk  
- Incorrect decisions affecting real users  

Small textual changes in policies can have large real-world impact, but static RAG-based systems fail to detect them.

---

## Solution

PolicySentinel treats policies as **live data**, not static documents.

The system:
- Tracks policy documents continuously
- Detects semantic changes between versions
- Updates internal memory in real time
- Triggers AI agents to analyze the impact of change

This ensures AI systems always reason using the current policy state.

---

## System Overview

The system works as a continuous pipeline:

1. **Continuous Policy Ingestion**  
   Policy documents are monitored in real time. Any update or replacement is detected immediately.

2. **Semantic Policy Representation**  
   Policies are parsed and converted into semantic representations that preserve intent, not just text.

3. **Policy Drift Detection**  
   New policy versions are compared with previous versions using stateful memory and semantic similarity.  
   Only meaningful changes are flagged.

4. **Agentic Impact Analysis**  
   When drift is detected, AI agents automatically assess who or what is affected and suggest actions.

This is an event-driven system, not a chatbot.

---

## Why Pathway

PolicySentinel is built on Pathway to enable:
- Streaming-first data processing
- Stateful comparison of document versions
- Incremental updates instead of full reprocessing
- Real-time vector indexing for always-fresh memory

Pathway makes continuous reasoning over changing data possible.

---

## Use Cases

- Enterprise policy compliance
- Finance and insurance rule enforcement
- Government and public service policies
- AI governance and guardrails

---

## Key Characteristics

- Real-time
- Stateful
- Agent-driven
- Enterprise-focused
- Policy-centric

---

## Scope

Included:
- Policy change monitoring
- Semantic drift detection
- Agent-triggered impact analysis

Not included:
- Chatbot interfaces
- Static document search
- Manual review tools

---

## Status

Prototype-level implementation focused on system design and core logic.
