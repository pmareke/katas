from typing import Dict
import re


class TextProcessing:
    @staticmethod
    def process(input: str) -> str:
        lines = ["Those are the top 10 words used:", ""]
        seen: Dict = dict()

        pattern = re.compile(r"\w+")
        words = re.findall(pattern, input)
        for word in words:
            key = word.lower()
            seen[key] = seen.get(key, 0) + 1

        sort = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        for index, key in enumerate(sort.keys()):
            if index < 10:
                lines.append(f"{index + 1}. {key}")

        lines.append("")
        lines.append(f"The text has in total {len(words)} words")

        return "\n".join(lines)
