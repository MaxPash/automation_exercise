"""Utility to close advertisement popups using multiple possible close button locators."""

from playwright.sync_api import Page


def _close_button_locators(page: Page):
    """Yield locators for ad close buttons in order of preference."""
    # Two iframe variants for "Close ad" button (e.g. Google ad)
    yield page.locator('iframe[name="aswift_2"]').content_frame.locator(
        'iframe[name="ad_iframe"]'
    ).content_frame.get_by_role("button", name="Close ad")
    yield page.locator('iframe[name="aswift_2"]').content_frame.get_by_role(
        "button", name="Close ad"
    )


def close_ad_popup(page: Page, timeout_ms: int = 1500) -> None:
    """
    Try to close an ad popup by clicking the first visible close button.

    Tries several known locators in order. Does nothing if no popup is present.
    """
    for locator in _close_button_locators(page):
        try:
            locator.click(timeout=timeout_ms)
            return
        except Exception:
            continue
