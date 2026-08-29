import time
import json
from core.technocore_bridge import TechnocoreBridge

def run_mcp_adapter_demo():
    print("\n" + "="*70)
    print(" 🔌 TECHNOCORE MCP (Model Context Protocol) ADAPTER DEMO")
    print(" Seamlessly connecting Anthropic MCP Clients to Technocore Mesh")
    print("="*70 + "\n")

    bridge = TechnocoreBridge(agent_name="ClaudeDesktopAgent")

    # Tool 1: send_technocore_message
    print("\033[94m[MCP TOOL CALL] -> send_technocore_message(mailbox='dev-lane', payload={...})\033[0m")
    time.sleep(1)
    msg_result = bridge.send_signed_message(
        mailbox="dev-lane",
        payload={"task": "Review Smart Contract Vulnerabilities", "priority": "HIGH"}
    )
    print(f"\033[92m[TECHNOCORE RESPONSE] Envelope Created & Signed:\033[0m")
    print(json.dumps(msg_result, indent=2))
    print("-" * 60 + "\n")

    time.sleep(1)

    # Tool 2: lock_technocore_state
    print("\033[94m[MCP TOOL CALL] -> lock_technocore_state(key='audits/approved', value={...})\033[0m")
    time.sleep(1)
    kv_result = bridge.lock_kv_state(
        key="audits/approved",
        value={"contract": "0x123...abc", "verified_by": bridge.did}
    )
    print(f"\033[92m[TECHNOCORE RESPONSE] Atomic KV Lock Status:\033[0m")
    print(json.dumps(kv_result, indent=2))

    print("\n" + "="*70)
    print(" ✅ MCP TOOL EXECUTION VIA TECHNOCORE SUCCESSFUL")
    print("="*70 + "\n")

if __name__ == "__main__":
    run_mcp_adapter_demo()
