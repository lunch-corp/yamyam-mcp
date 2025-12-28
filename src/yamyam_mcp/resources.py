"""MCP 리소스 정의."""

from fastmcp import FastMCP


def register_resources(mcp: FastMCP) -> None:
    """MCP 서버에 리소스를 등록합니다."""

    @mcp.resource("yamyam://info")
    def get_info() -> str:
        """
        Yamyam MCP 서버 정보를 반환합니다.
        """
        return (
            "Yamyam MCP Server v0.1.0\n\n이 서버는 Model Context Protocol을 구현한 예제 서버입니다."
        )
