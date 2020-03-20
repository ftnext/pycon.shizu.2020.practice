from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Session:
    title: str
    speaker: str
    level: str
    category: str
    url: str
    content: str

    def to_dict(self):
        return asdict(self)


def _get_sessions():
    sessions = [
        Session(
            url="https://shizuoka.pycon.jp/",
            title="title",
            speaker="test",
            level="ALL",
            category="カテゴリ",
            content="セッション内容",
        )
    ]
    for session in sessions:
        yield session


def scrape():
    yield from _get_sessions()
