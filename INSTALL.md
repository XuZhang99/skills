# Install

Follow this file to install and update the skills in this repository for Codex, Claude Code, or similar coding agents.

## Default install location

Install skills into:

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

This keeps the skills auto-discoverable for Codex-style agents.

## Install the whole repository

Clone the repository into a temporary location, then copy the contents of `skills/` into the default skills directory:

```bash
tmp_dir="$(mktemp -d)"
git clone git@github.com:XuZhang99/skills.git "$tmp_dir/repo"
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R "$tmp_dir/repo/skills/." "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Install a single skill

To install only `agent-harness-scaffold`:

```bash
tmp_dir="$(mktemp -d)"
git clone git@github.com:XuZhang99/skills.git "$tmp_dir/repo"
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R "$tmp_dir/repo/skills/agent-harness-scaffold" "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Update installed skills

To refresh local installed copies from the repository:

```bash
tmp_dir="$(mktemp -d)"
git clone git@github.com:XuZhang99/skills.git "$tmp_dir/repo"
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R "$tmp_dir/repo/skills/." "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Agent instruction snippet

Use this exact style when another agent needs to install these skills:

```text
Follow https://raw.githubusercontent.com/XuZhang99/skills/refs/heads/master/INSTALL.md to install and configure the skills from XuZhang99/skills.
```

## Notes

- Repository skills live under `skills/`.
- Each skill should contain a `SKILL.md` file at its root.
- Copying the repository's `skills/` children into `${CODEX_HOME:-$HOME/.codex}/skills` is the intended installation behavior.
