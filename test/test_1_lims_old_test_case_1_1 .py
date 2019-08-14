# Login and logout

def test_1_lims_old_test_case_1_1(app):
    app.session.login(name="adm_tadejeva", password="29092007")
    app.session.logout()
