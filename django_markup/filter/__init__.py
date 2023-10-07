from typing import Any, Self


class MarkupFilter:
    """
    Abstract your new filters from this class. This is the most simplest way of
    a filter, it accepts the text in it's render method and returns it, as is.
    """

    title = "BaseFilter"

    def render(
        self: Self,
        text: str,
        **kwargs: Any,  # noqa: ARG002 Unused argument
    ) -> str:
        return text
