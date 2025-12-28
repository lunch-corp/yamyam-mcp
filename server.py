from fastmcp import FastMCP

from yamyam_mcp import resources, tools

# FastMCP 서버 인스턴스 생성
mcp = FastMCP("yamyam-mcp")

# 도구 및 리소스 등록
tools.register_tools(mcp)
resources.register_resources(mcp)


def main() -> None:
    """MCP 서버를 실행합니다."""
    mcp.run()


if __name__ == "__main__":
    main()
