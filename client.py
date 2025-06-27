from fastmcp import Client
from fastmcp.client.auth import OAuth
import asyncio

# Configure the OAuth helper with your MCP server URL
MCP_URL = "http://localhost:8000/mcp/sse"
# MCP_URL = "https://mcp.asana.com/sse"

oauth = OAuth(
    mcp_url=MCP_URL,
)


async def main():
    # Create the client with OAuth authentication
    async with Client(MCP_URL, auth=oauth) as client:
        # Example: ping the server
        is_alive = await client.ping()
        print(f"Ping successful: {is_alive}")

        # Example: list available tools
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"- {tool.name}: {tool.description}")


if __name__ == "__main__":
    asyncio.run(main())
