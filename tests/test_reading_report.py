from datetime import UTC, datetime

from goodreads_tools.models import ShelfItem
from goodreads_tools.public.reading_report import build_reading_report


def test_build_reading_report() -> None:
    read_items = [
        ShelfItem(
            title="Read Book",
            link="https://www.goodreads.com/book/show/1",
            book_id="1",
            author="Reader Author",
            rating=5,
            read_at="Mon, 01 Jan 2024 00:00:00 -0700",
            date_added="Sun, 31 Dec 2023 00:00:00 -0700",
        )
    ]
    reading_items = [
        ShelfItem(
            title="Current Book",
            link="https://www.goodreads.com/book/show/2",
            book_id="2",
            author="Reading Author",
            date_started="Tue, 02 Jan 2024 00:00:00 -0700",
            date_added="Tue, 02 Jan 2024 00:00:00 -0700",
        )
    ]
    generated_at = datetime(2024, 1, 3, tzinfo=UTC)

    content = build_reading_report(
        "123",
        read_items,
        reading_items,
        generated_at=generated_at,
    )

    assert "# Goodreads Reading Report" in content
    assert "| User | 123 |" in content
    assert "| Read count | 1 |" in content
    assert "| Currently reading count | 1 |" in content
    assert "## Currently Reading" in content
    assert "[Current Book](https://www.goodreads.com/book/show/2)" in content
    assert "## Read" in content
    assert "[Read Book](https://www.goodreads.com/book/show/1)" in content
