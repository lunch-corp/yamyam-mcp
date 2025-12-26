# yamyam-mcp

Model Context Protocol (MCP) 서버 구현 (FastMCP 사용)

## 설치

```bash
uv sync
```

또는

```bash
pip install -e .
```

## 실행

### 직접 실행 (테스트용)

서버를 직접 실행하여 테스트할 수 있습니다:

```bash
# 방법 1: 스크립트로 실행
uv run yamyam-mcp

# 방법 2: 모듈로 실행
uv run python -m yamyam_mcp.server
```

> **참고**: MCP 서버는 STDIO 방식으로 동작하므로, 직접 실행하면 입력을 기다립니다. 일반적으로는 MCP 클라이언트에서 실행합니다.

### MCP 클라이언트에서 실행

MCP 서버는 STDIO 방식으로 실행됩니다. MCP 클라이언트(예: Claude Desktop)에서 다음과 같이 설정하세요:

```json
{
  "mcpServers": {
    "yamyam-mcp": {
      "command": "uv",
      "args": ["run", "yamyam-mcp"]
    }
  }
}
```

또는 모듈로 실행:

```json
{
  "mcpServers": {
    "yamyam-mcp": {
      "command": "uv",
      "args": ["run", "python", "-m", "yamyam_mcp.server"]
    }
  }
}
```

## 기능

### Tools

- `echo`: 입력된 텍스트를 그대로 반환하는 간단한 도구

### Resources

- `yamyam://info`: 서버 정보 리소스

## 프로젝트 구조

```
yamyam-mcp/
├── src/
│   └── yamyam_mcp/          # 메인 패키지
│       ├── __init__.py      # 패키지 초기화
│       ├── server.py        # MCP 서버 인스턴스 및 진입점
│       ├── tools.py         # MCP 도구 정의
│       └── resources.py     # MCP 리소스 정의
├── pyproject.toml           # 프로젝트 설정
└── README.md
```

## 개발

프로젝트는 Python 3.11 이상을 요구합니다.

### 개발 의존성 설치

```bash
uv sync --extra dev
```

### 코드 포맷팅

ruff를 사용하여 포맷팅과 린팅을 수행합니다:

```bash
# 포맷팅
uv run ruff format .

# 린팅 및 자동 수정
uv run ruff check --fix .

# 또는 black과 isort 사용
uv run black .
uv run isort .
```
