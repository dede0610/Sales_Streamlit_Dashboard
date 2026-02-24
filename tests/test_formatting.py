"""Tests for formatting utilities."""

from src.utils.formatting import format_currency, format_number, format_percentage


class TestFormatNumber:
    """Tests for format_number function."""

    def test_small_number(self):
        """Test formatting small numbers."""
        assert format_number(123) == "123"
        assert format_number(123.45, decimals=2) == "123.45"

    def test_thousands(self):
        """Test formatting thousands."""
        result = format_number(5000)
        assert "K" in result

    def test_none(self):
        """Test formatting None."""
        assert format_number(None) == "-"


class TestFormatCurrency:
    """Tests for format_currency function."""

    def test_euro(self):
        """Test euro currency."""
        result = format_currency(1234.56)
        assert "€" in result

    def test_custom_symbol(self):
        """Test custom symbol."""
        result = format_currency(100, symbol="$")
        assert "$" in result

    def test_none(self):
        """Test formatting None."""
        assert format_currency(None) == "-"


class TestFormatPercentage:
    """Tests for format_percentage function."""

    def test_positive(self):
        """Test positive percentage."""
        result = format_percentage(0.15)
        assert "+15" in result
        assert "%" in result

    def test_negative(self):
        """Test negative percentage."""
        result = format_percentage(-0.1)
        assert "-10" in result

    def test_none(self):
        """Test formatting None."""
        assert format_percentage(None) == "-"
