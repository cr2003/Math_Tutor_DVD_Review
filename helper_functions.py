# Helper functions


def fmt_vec(v, precision=2, type="f"):
    """Format the output of a vector with the specified precision"""
    return f"<{v.x:.{precision}{type}}, {v.y:.{precision}{type}}, {v.z:.{precision}{type}}>"


def setup_math_axes(ax, xlim=(-6, 6), ylim=(-6, 6), grid=True):
    """
    Configures standard Cartesian math axes crossing at (0, 0)
    with default limits and a grid.
    """
    # Move left and bottom spines to the origin (zero)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")

    # Hide the top and right spines
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    # Set axis limits
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    # Ensure ticks stay visible and aligned with the zero lines
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    # Add a subtle grid
    if grid:
        ax.grid(True, linestyle="--", alpha=0.6, linewidth=0.5)
