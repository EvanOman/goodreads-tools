from __future__ import annotations

from datetime import UTC, datetime

from goodreads_tools.models import ShelfItem


def _escape_markdown_cell(value: str) -> str:
    cleaned = value.replace("\r", " ").replace("\n", "<br>")
    return cleaned.replace("|", "\\|")


def _format_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("---" for _ in headers) + " |"
    lines = [header_line, separator]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def _title_cell(item: ShelfItem) -> str:
    title = _escape_markdown_cell(item.title)
    if item.link:
        return f"[{title}]({item.link})"
    return title


def _rating_cell(item: ShelfItem) -> str:
    return "" if item.rating is None else str(item.rating)


def _value_cell(value: str | None) -> str:
    return "" if value is None else _escape_markdown_cell(value)


def build_reading_report(
    user_id: str,
    read_items: list[ShelfItem],
    reading_items: list[ShelfItem],
    *,
    read_shelf: str = "read",
    reading_shelf: str = "currently-reading",
    generated_at: datetime | None = None,
) -> str:
    timestamp = (generated_at or datetime.now(UTC)).isoformat()

    lines: list[str] = ["# Goodreads Reading Report", ""]
    lines.append("## Metadata")
    lines.append("")
    metadata_rows = [
        ["User", _escape_markdown_cell(user_id)],
        ["Generated", _escape_markdown_cell(timestamp)],
        ["Read shelf", _escape_markdown_cell(read_shelf)],
        ["Read count", str(len(read_items))],
        ["Currently reading shelf", _escape_markdown_cell(reading_shelf)],
        ["Currently reading count", str(len(reading_items))],
        ["Source", "Public RSS feed"],
    ]
    lines.append(_format_markdown_table(["Field", "Value"], metadata_rows))
    lines.append("")

    lines.append("## Currently Reading")
    lines.append("")
    if reading_items:
        reading_rows: list[list[str]] = []
        for item in reading_items:
            reading_rows.append(
                [
                    _title_cell(item),
                    _value_cell(item.author),
                    _rating_cell(item),
                    _value_cell(item.date_started),
                    _value_cell(item.date_added),
                ]
            )
        lines.append(
            _format_markdown_table(
                ["Title", "Author", "Rating", "Started", "Added"],
                reading_rows,
            )
        )
    else:
        lines.append("_No currently reading items found._")

    lines.append("")
    lines.append("## Read")
    lines.append("")
    if read_items:
        read_rows: list[list[str]] = []
        for item in read_items:
            read_rows.append(
                [
                    _title_cell(item),
                    _value_cell(item.author),
                    _rating_cell(item),
                    _value_cell(item.read_at),
                    _value_cell(item.date_added),
                ]
            )
        lines.append(
            _format_markdown_table(
                ["Title", "Author", "Rating", "Read At", "Added"],
                read_rows,
            )
        )
    else:
        lines.append("_No read items found._")

    lines.append("")
    return "\n".join(lines)
