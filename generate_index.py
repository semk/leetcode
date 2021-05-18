#!/usr/bin/env python
#
# This script iterates through the solutions and automatically
# populates the README.md file with information and links


import glob
from collections import OrderedDict

# Path to README.md file
README = 'README.md'
TEMP_README = 'README.tmp.md'
# Section to be filled in README.md
README_HEADER = "### Problems & Solutions"

PYTHON = 'python'
GOLANG = 'go'

LANGS = (PYTHON, GOLANG)
EXT = {
    PYTHON: ".py",
    GOLANG: ".go"
}
COMMENT_PREFIX = {
    PYTHON: '#',
    GOLANG: '//'
}

EASY = 'easy'
MEDIUM = 'medium'
HARD = 'hard'

LEVELS = (EASY, MEDIUM, HARD)

METADATA_KEYS = {'description', 'difficulty', 'leetcode_num', 'leetcode_url'}


def parse_metadata(path, lang):
    metadata = {}
    with open(path) as f:
        for line in f.readlines():
            if not line.startswith(COMMENT_PREFIX[lang]):
                break
            splits = line.strip(COMMENT_PREFIX[lang]).split(':', 1)
            if len(splits) != 2:
                continue
            key = splits[0].strip()
            value = splits[1].strip()
            if key in METADATA_KEYS:
                metadata[key] = value

    return metadata


def populate_table(metadata, readme):
    readme.append('\n')
    readme.append('| Problem | Solution | Difficulty |\n')
    readme.append('| ------- | -------- | ---------- |\n')

    total = {EASY: 0, MEDIUM: 0, HARD: 0}
    for lang, level_info in metadata.items():
        for level, problems in level_info.items():
            for problem in problems:
                data = '[{}]({}) | [{}]({}) | {} |'.format(
                    problem.get('description', 'undefined'),
                    problem.get('leetcode_url', 'undefined'),
                    lang.title(), problem.get('path', 'undefined'),
                    level.title(),
                )
                readme.append(data + '\n')
                total[level] += 1

    readme.append(
        "\nThis repository currently hosts a total of {} solutions ({} Easy, {} Medium, {} Hard). \n".format(
            sum(total.values()), total[EASY], total[MEDIUM], total[HARD]
        )
    )


def generate():
    readme = []
    with open(README) as f:
        for line in f.readlines():
            readme.append(line)
            if line.startswith(README_HEADER):
                break

    solutions = OrderedDict()
    for lang in LANGS:
        for level in LEVELS:
            for path in glob.glob('./{}/{}/*{}'.format(lang, level, EXT[lang])):
                metadata = parse_metadata(path, lang)
                metadata['path'] = path
                metadata['lang'] = lang
                metadata['difficulty'] = level
                solutions.setdefault(lang, OrderedDict()).setdefault(
                    level, []).append(metadata)

    populate_table(solutions, readme)

    with open(README, 'w') as f:
        f.writelines(readme)


if __name__ == "__main__":
    generate()
