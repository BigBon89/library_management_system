import re

class Command:
    def __init__(self, command: str):
        pattern = r'([\'\"].+?[\'\"])|(\S+)'
        matches = re.findall(pattern, command)

        self._command = matches[0][1]
        self._args = [match[0].strip('\"\'') or match[1] for match in matches[1:]]

    @property
    def command(self) -> str:
        return self._command

    @property
    def args(self) -> list:
        return self._args