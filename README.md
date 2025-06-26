# MCP OAuth Server Example

This project demonstrates FastMCP server with Bearer token authentication mounted on FastAPI, including OAuth 2.1 endpoints for dynamic client registration and metadata discovery.

## Features

- FastMCP server mounted on FastAPI
- Bearer token (JWT) authentication using RSA public key validation
- OAuth 2.1 Authorization Server metadata endpoints
- Dynamic client registration endpoint
- OpenID Connect discovery endpoint
- CORS middleware for cross-origin requests
- Structured logging with loguru
- Development token generation endpoint
- Health check endpoint
- Multiple MCP tools (hello, add_numbers)

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python server.py
```

eg.

```bash
python server.py --transport sse --host 0.0.0.0 --port 8000 --log-level info
```

### Command Line Options

```bash
python server.py --help
```

- `--transport`: Transport type (`sse` or `http`, default: `sse`)
- `--host`: Host address (default: `127.0.0.1`)
- `--port`: Port number (default: `8000`)
- `--log-level`: Logging level (default: `info`)

## Server Endpoints

### Core Endpoints

- **MCP Server**: `http://127.0.0.1:8000/mcp` - Main MCP endpoint
- **Health Check**: `http://127.0.0.1:8000/mcp/health` - Server health status
- **API Documentation**: `http://127.0.0.1:8000/docs` - FastAPI auto-generated docs

### OAuth 2.1 Endpoints

- **Authorization Server Metadata**: `http://127.0.0.1:8000/.well-known/oauth-authorization-server`
- **OpenID Connect Discovery**: `http://127.0.0.1:8000/.well-known/openid-configuration`
- **Protected Resource Metadata**: `http://127.0.0.1:8000/.well-known/oauth-protected-resource`
- **Dynamic Client Registration**: `POST http://127.0.0.1:8000/register`

### Development Endpoints

- **Development Token**: `http://127.0.0.1:8000/dev/token` - Generate test tokens

## Environment Variables

You can configure the server using environment variables:

- `ISSUER`: JWT issuer (default: `https://dev.example.com`)
- `AUDIENCE`: JWT audience (default: `my-mcp-server`)
- `CLIENT_SECRET`: OAuth client secret (default: auto-generated UUID)
- `BASE_URL`: Base URL for the server (default: `http://127.0.0.1:8000`)

## Example MCP Tools

- `hello(name: str) -> str`: Returns a greeting message
- `add_numbers(a: int, b: int) -> int`: Adds two numbers together

Both tools require valid authentication.

## OAuth 2.1 Compliance

This server implements key OAuth 2.1 endpoints:

- Authorization Server Metadata Discovery
- Dynamic Client Registration (RFC 7591)
- Protected Resource Metadata (RFC 8705)

Note: This is a development/demonstration server. For production use, integrate with a proper OAuth 2.1 Authorization Server or Identity Provider.

## References

- [FastMCP Bearer Auth Documentation](https://gofastmcp.com/servers/auth/bearer)
- [fastmcp GitHub](https://github.com/jlowin/fastmcp)
- [OAuth 2.1 Specification](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1)
- [RFC 7591 - OAuth 2.0 Dynamic Client Registration](https://tools.ietf.org/html/rfc7591)
