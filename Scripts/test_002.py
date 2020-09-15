import allure


class Test001:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("第一步")
    def test001(self):
        print("\n hello python")

    @allure.severity(allure.severity_level.CRITICAL)
    def test002(self):
        print("\n hello python")

    @allure.severity(allure.severity_level.NORMAL)
    def test003(self):
        print("\n hello python")
        assert False

    @allure.severity(allure.severity_level.MINOR)
    def test004(self):
        print("\n hello python")

    @allure.severity(allure.severity_level.TRIVIAL)
    def test005(self):
        print("\n hello python")
