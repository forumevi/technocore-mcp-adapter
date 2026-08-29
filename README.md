# 🔌 Technocore WebMCP Adapter (`technocore-mcp-adapter`)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-1.0%20Ready-green)](https://modelcontextprotocol.io)
[![Technocore Infrastructure](https://img.shields.io/badge/Technocore-DID%20Signed-blue)](https://github.com/flop-labs/technocore-chat)

> **Unlocking Technocore Infrastructure for Anthropic MCP Clients, Claude Desktop, and Autonomous Agent Frameworks.**

`technocore-mcp-adapter` bridges the **Model Context Protocol (MCP)** with **Technocore Signed Infrastructure**. It exposes Technocore mailboxes (`mb-`) and KV state stores (`/kv/`) as native MCP tools, allowing any LLM agent to send cryptographically signed messages without custom code integrations.

---

## ⚡ Features

* **🔌 Native MCP Compatibility:** Connects directly with Claude Desktop, Cursor, or custom MCP hosts.
* **🔑 Automatic `did:key` Signing:** Every tool call automatically signs payloads with Ed25519 identities.
* **📬 Mailbox Routing (`mb-`):** Dispatch tasks to specialized agent lanes directly via prompt commands.
* **🔒 Atomic State Locking (`/kv/`):** Lock state across agent swarms using Technocore CAS updates.

---

## 🏗️ Architecture
┌─────────────────────────┐          JSON-RPC          ┌─────────────────────────┐
│  Claude / MCP Host      │ ─────────────────────────► │  Technocore MCP Adapter │
│  (Desktop / Cursor)     │ ◄───────────────────────── │  (Local Bridge)         │
└─────────────────────────┘                            └────────────┬────────────┘
│
Signed DID Payload
│
▼
┌─────────────────────────┐
│ Technocore Mesh         │
│ (mb- /kv/ Stores)       │
└─────────────────────────┘


---

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/forumevi/technocore-mcp-adapter.git](https://github.com/forumevi/technocore-mcp-adapter.git)
cd technocore-mcp-adapter

# Run standalone CLI demo
python demo.py
🤝 Ecosystem Integration
Built for @CryptoHayes and @flop_labs to expand Technocore adoption across the broader AI developer ecosystem.

License: MIT
