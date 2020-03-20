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


def scrape():
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
    return sessions
