class CreateUserPage:
    form_new_user = "xpath://form[contains(@action,'newuser.php')]"
    txt_fields = "xpath://label[text() = '?']//following::input"
    li_costcenter = "id:costcenterID"
    chk_is_locked = "id:is_locked"
    btn_submit = "xpath://input[@value = 'Submit']"
