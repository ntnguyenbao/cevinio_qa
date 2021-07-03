class CompanySettingsPage:
    box_info = "xpath://div[@class = 'infobox']"
    page_description = "This is the \"Company Settings\" menu of the Cockpit. Here you can alter various settings of your company."
    lnk_menu = "xpath://div[@id='page_menu_extended']//a[text()='?']//following::a[text() = '?']"
    box_notice = "xpath://div[@class='noticebox']//descendant-or-self::*"
