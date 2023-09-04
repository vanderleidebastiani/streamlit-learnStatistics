from st_pages import Page, Section, add_page_title, show_pages

add_page_title()

show_pages(
    [
        # Section(name="Início", icon=":books:"),
        Page("pages/statHome.py", "Início", ":school:"),
        Page("pages/statDescriptive.py", "Estatísticas descritivas", ":pencil:"),
        Page("pages/statDistribution.py", "Distribuições", ":bar_chart:"),
    ]
)
