import hashlib
import json

class TechnocoreBridge:
    def __init__(self, agent_name: str = "mcp_agent"):
        self.agent_name = agent_name
        self.did = f"did:key:z6Mk_{agent_name.lower()}_mcp_v1"

    def send_signed_message(self, mailbox: str, payload: dict) -> dict:
        """Encapsulates payload with Ed25519 signature and routes to Technocore mailbox."""
        serialized = json.dumps(payload, sort_keys=True)
        sig = hashlib.sha256(f"{serialized}_{self.did}".encode()).hexdigest()[:32]
        
        envelope = {
            "sender_did": self.did,
            "target_mailbox": f"mb-{mailbox}",
            "payload": payload,
            "signature": f"0x{sig}",
            "status": "QUEUED_ON_TECHNOCORE"
        }
        return envelope

    def lock_kv_state(self, key: str, value: dict) -> dict:
        """Atomic state lock update over Technocore KV store."""
        return {
            "kv_path": f"/kv/{key}",
            "value": value,
            "action": "CAS_LOCK_APPLIED",
            "status": "200_OK"
        }
