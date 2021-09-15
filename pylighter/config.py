import ipywidgets

from pylighter.shortcut_helper.shortcut_helper import Shortcut

# -----------------------------------------------------------
# Files paths
# -----------------------------------------------------------

ANNOTATION_SAVE_PATH = "annotation.csv"

# -----------------------------------------------------------
# Display
# -----------------------------------------------------------

LABELS_NAMES = [
    "l1",
    "l2",
    "l3",
    "l4",
    "l5",
    "l6",
    "l7",
]
DEFAULT_COLORS = [
    "#2DA9D5",
    "#FFC366",
    "#50C78E",
    "#325B6C",
    "#864E1B",
    "#3B474A",
    "#F97F50",
]

ERASER_COLOR = "#ED6855"
CHECK_COLOR = "#55eded"

CHAR_PARAMS = {
    "min_width_between_chars": "4px",
    "width_white_space": "10px",
    "font_size": "medium",
}

DISPLAY_ELEMENTS = {
    "checkbox": ipywidgets.Checkbox,
    "int_text": ipywidgets.IntText,
    "float_text": ipywidgets.FloatText,
    "text": ipywidgets.Text,
    "text_area": ipywidgets.Textarea,
}

# -----------------------------------------------------------
# Shortcuts
# -----------------------------------------------------------

# Shortcut used to kill all other shortcuts
# Used at the init of the annotation to kill all previous shortcuts
SHORTCUT_CANCEL_SHORTCUTS = Shortcut(
    name="cancel_shortcuts",
    key=",",
    code="KeyR",
    shift_key=True,
    alt_key=True,
    ctrl_key=True,
)

SHORTCUTS = [
    Shortcut(
        name="next",
        key="j",
        code="KeyJ",
        shift_key=False,
        alt_key=True,
        ctrl_key=False,
    ),
    Shortcut(
        name="previous",
        key="k",
        code="KeyK",
        shift_key=False,
        alt_key=True,
        ctrl_key=False,
    ),
    Shortcut(
        name="skip", key="s", code="KeyS", shift_key=False, alt_key=True, ctrl_key=True
    ),
    Shortcut(
        name="save", key="S", code="KeyS", shift_key=True, alt_key=True, ctrl_key=False
    ),
]
