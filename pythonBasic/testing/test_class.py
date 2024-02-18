class TestClass:
    def test_one(self):
        x = "this"
        assert "s" in x, "ini ga tau kenapa"

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")