"""
OpenClaw Trading Assistant
交易辅助决策系统

Technical Analysis & Trading Signals
技术分析与交易信号
"""

__version__ = "1.0.0"
__author__ = "OpenClaw Community"
__email__ = "community@openclaw.ai"

from . import config
from . import i18n

# Main modules
from .support_resistance import calculate_support_resistance
from .trading_signals import generate_trading_signal
from .position_calculator import calculate_position_size

__all__ = [
    "calculate_support_resistance",
    "generate_trading_signal",
    "calculate_position_size",
    "config",
    "i18n",
]
