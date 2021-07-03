class ManageUsersPage:
    tbl_user_browser = "xpath://div[@id='users_browser']/table"
    page_description = "The 'Manage users' overview displays all users currently available in your company."
    box_info = "xpath://div[@class = 'infobox']"
    lnk_add_user = "xpath://div[@id='quicklinks']/a[text()='Add User']"
    form_new_user = "xpath://form[contains(@action,'newuser.php')]"
    txt_fields = "xpath://label[text() = '?']//following::input"
    li_costcenter = "id:costcenterID"

