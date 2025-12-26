"""MCP 도구 정의."""

from fastmcp import FastMCP


def register_tools(mcp: FastMCP) -> None:
    """MCP 서버에 도구를 등록합니다."""

    @mcp.tool()
    def echo(query: str) -> str:
        """
        입력된 텍스트를 그대로 반환하는 간단한 도구입니다.

        Args:
            query: 반환할 텍스트

        Returns:
            입력된 텍스트
        """
        return query
