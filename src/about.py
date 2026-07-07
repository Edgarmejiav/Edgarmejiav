ABOUT_NAME_FILE = "about"
SO_TEMPLATE_VARIABLE = "@ABOUT_HEADER"
WM_TEMPLATE_VARIABLE = "@ABOUT_COLLABORATIONS"
TERM_TEMPLATE_VARIABLE = "@ABOUT_COLLDES"
SHELL_TEMPLATE_VARIABLE = "@ABOUT_SKILL"


def replace_about(data, lang: str, raw_temp: str) -> str:
    d = data[ABOUT_NAME_FILE]
    if len(lang) == 0:
        lang = "ES"
    if lang in d:
        d = d[lang]
    s = raw_temp.replace(SO_TEMPLATE_VARIABLE, d['header'])
    s = s.replace(WM_TEMPLATE_VARIABLE, d['collaborations'])
    s = s.replace(TERM_TEMPLATE_VARIABLE, d['colDes'])
    s = s.replace(SHELL_TEMPLATE_VARIABLE, d['skill'])
    s = s.replace("@ABOUT_BIO", d.get('bio', ''))
    s = s.replace("@EXPERIENCE_TITLE", d.get('exp_title', ''))
    s = s.replace("@EXPERIENCE_CONTENT", d.get('exp_content', ''))
    s = s.replace("@PROJECTS_TITLE", d.get('projects_title', ''))
    return s
