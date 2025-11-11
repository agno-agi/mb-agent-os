from pathlib import Path

from agno.os import AgentOS

from agents.agno_mcp_agent import agno_mcp_agent

# ============================================================================
# AgentOS Config
# ============================================================================
os_config_path = str(Path(__file__).parent.joinpath("config.yaml"))

# ============================================================================
# Create AgentOS
# ============================================================================
agent_os = AgentOS(
    id="mb-agent-os",
    agents=[agno_mcp_agent],
    config=os_config_path,
)
app = agent_os.get_app()

# ============================================================================
# Run AgentOS
# ============================================================================
if __name__ == "__main__":
    agent_os.serve(app="main:app", reload=True)
