from st_pages import Page, Section, add_page_title, show_pages

add_page_title()

show_pages(
    [
        # Section(name="Início", icon=":books:"),
        Page("pages/statHome.py", "Início", ":school:"),
        # Section(name="Tópicos", icon=":books:"),
        # Section(name="Section2", icon=":bar_chart:"),
        Page("pages/statDescriptive.py", "Estatísticas descritivas", ":pencil:"),
        Page("pages/statDistribution.py", "Distribuições", ":bar_chart:"),
    ]
)
