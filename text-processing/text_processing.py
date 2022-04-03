from typing import Dict
import re


class TextProcessing:
    @staticmethod
    def process(input: str, escape=None) -> str:
        result = ["Those are the top 10 words used:", ""]
        seen: Dict = dict()

        number_of_words = 0
        lines = input.split("\n")
        indices = []
        for index, line in enumerate(lines):
            if "```" in line:
                indices.append(index)

        if len(indices) > 0:
            lines = lines[0 : indices[0]] + lines[indices[1] + 1 :]

        for line in lines:
            pattern = re.compile(r"\w+")
            words = re.findall(pattern, line)
            number_of_words += len(words)
            for word in words:
                key = word.lower()
                seen[key] = seen.get(key, 0) + 1

        sort = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        for index, key in enumerate(sort.keys()):
            if index < 10:
                result.append(f"{index + 1}. {key}")

        result.append("")
        result.append(f"The text has in total {number_of_words} words")

        return "\n".join(result)
