# 09 — Model Context Protocol (MCP) Integration Guide

> **Standard:** Model Context Protocol (Anthropic Open Standard)  
> **Target:** Hermes Agent CLI (`~/.hermes/mcp_servers.json`) and Hermes Desktop  
> **Status:** Production-Ready Pre-configured Templates

---

## 1. Overview

The **Model Context Protocol (MCP)** provides standardized client-server interfaces that allow Hermes to securely connect to external development environments, local databases, browsers, and remote APIs without custom ad-hoc tool parsers.

`05-HERMES-Advanced/mcp_servers.json` includes pre-configured declarations for:

| Server | Capability | Runtime Command |
|---|---|---|
| `filesystem` | Sandboxed local file operations | `npx @modelcontextprotocol/server-filesystem` |
| `github` | Issues, PRs, code searches, commits | `npx @modelcontextprotocol/server-github` |
| `brave-search` | High-throughput web indexing | `npx @modelcontextprotocol/server-brave-search` |
| `puppeteer` | Full JS rendering, DOM scraping | `npx @modelcontextprotocol/server-puppeteer` |
| `sqlite` | Structured belief/mission persistence | `uvx mcp-server-sqlite` |
| `memory` | Graph-based knowledge representation | `npx @modelcontextprotocol/server-memory` |

---

## 2. Activation in Hermes Agent

### Step 1: Copy Configuration
```bash
# Automated via installer:
python install.py

# Or manually:
cp 05-HERMES-Advanced/mcp_servers.json ~/.hermes/mcp_servers.json
```

### Step 2: Set Environment Variables
Add your required API keys to `~/.hermes/.env`:
```bash
GITHUB_TOKEN=ghp_your_github_personal_access_token
BRAVE_API_KEY=BSA_your_brave_search_api_key
```

### Step 3: Test MCP Tool Discovery
```bash
hermes tools --mcp
```
Hermes will list all dynamic tools exposed by the configured MCP servers (e.g. `read_file`, `create_issue`, `search`, `puppeteer_navigate`).

---

## 3. Sandboxing & Poka-Yoke Safeguards
When combined with **Skill 05 (Safety & Evaluation)**:
* Filesystem MCP is restricted to explicit workspace subtrees (preventing traversal to root directories).
* Database write operations are evaluated against Risk Level R3+ gating.
* Network and GitHub actions are logged with full provenance trails.
