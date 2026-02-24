"""Utility functions for formatting."""

from datetime import date, datetime


def format_number(value: float | int | None, decimals: int = 0) -> str:
    """Format a number with thousands separators.

    Args:
        value: Number to format.
        decimals: Number of decimal places.

    Returns:
        Formatted string.
    """
    if value is None:
        return "-"

    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.{decimals}f}M"
    elif abs(value) >= 1_000:
        return f"{value / 1_000:.{decimals}f}K"
    else:
        return f"{value:,.{decimals}f}".replace(",", " ")


def format_currency(value: float | int | None, symbol: str = "€", decimals: int = 0) -> str:
    """Format a number as currency.

    Args:
        value: Number to format.
        symbol: Currency symbol.
        decimals: Number of decimal places.

    Returns:
        Formatted currency string.
    """
    if value is None:
        return "-"

    formatted = f"{value:,.{decimals}f}".replace(",", " ")
    return f"{formatted} {symbol}"


def format_percentage(value: float | None, decimals: int = 1) -> str:
    """Format a decimal as percentage.

    Args:
        value: Decimal value (0.15 = 15%).
        decimals: Number of decimal places.

    Returns:
        Formatted percentage string.
    """
    if value is None:
        return "-"

    sign = "+" if value > 0 else ""
    return f"{sign}{value * 100:.{decimals}f}%"


def format_date(d: date | datetime | str | None, fmt: str = "%d/%m/%Y") -> str:
    """Format a date.

    Args:
        d: Date to format.
        fmt: strftime format string.

    Returns:
        Formatted date string.
    """
    if d is None:
        return "-"

    if isinstance(d, str):
        try:
            d = datetime.strptime(d, "%Y-%m-%d").date()
        except ValueError:
            return d

    if isinstance(d, (date, datetime)):
        return d.strftime(fmt)

    return str(d)


def get_delta_color(value: float | None) -> str:
    """Get color for delta display.

    Args:
        value: Delta value.

    Returns:
        Color name for st.metric ("normal", "inverse", "off").
    """
    if value is None or value == 0:
        return "off"

    return "normal"
