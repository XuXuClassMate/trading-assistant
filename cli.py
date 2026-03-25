#!/usr/bin/env python3
"""
OpenClaw Trading Assistant CLI
命令行交互界面

Usage:
    openclaw-trading-assistant [command] [options]
    
Commands:
    interactive, interact, cli    Start interactive mode / 交互模式
    support-resistance            Analyze support/resistance levels / 分析支撑阻力位
    signals                       Generate trading signals / 生成交易信号
    position                      Calculate position size / 计算仓位大小
    alerts                        Manage price alerts / 管理价格提醒
    all                           Run all analysis / 运行所有分析
    version                       Show version / 显示版本
    help                          Show help / 显示帮助
"""

import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
from i18n import t
from support_resistance import SupportResistanceAnalyzer
from trading_signals import SignalGenerator
from position_calculator import PositionCalculator
from stop_loss_alerts import StopLossAlert

VERSION = "1.3.1"


def print_banner():
    """Print welcome banner"""
    print("=" * 60)
    print("  OpenClaw Trading Assistant CLI")
    print(f"  Version: {VERSION}")
    print(f"  {t('timestamp')}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()


def print_help():
    """Print help message"""
    help_text = """
OpenClaw Trading Assistant CLI - Help

Commands:
  interactive, interact, cli    Start interactive mode / 交互模式
  support-resistance            Analyze support/resistance levels
  signals                       Generate trading signals
  position                      Calculate position size
  alerts                        Manage price alerts
  all                           Run all analysis
  version                       Show version
  help                          Show this help

Examples:
  openclaw-trading-assistant
  openclaw-trading-assistant interactive
  openclaw-trading-assistant signals --symbol NVDA
  openclaw-trading-assistant position --symbol NVDA --price 175.64 --capital 10000
  openclaw-trading-assistant alerts check

Use --help after any command for detailed options.
"""
    print(help_text)


def run_support_resistance(args):
    """Run support/resistance analysis"""
    print(f"\n📊 {t('analyzing_support_resistance')}...")
    analyzer = SupportResistanceAnalyzer()
    
    if '--symbol' in args:
        idx = args.index('--symbol')
        symbol = args[idx + 1] if idx + 1 < len(args) else None
        if symbol:
            print(f"Symbol: {symbol}")
            # TODO: Add symbol-specific analysis
    else:
        # Analyze watchlist
        analyzer.analyze_watchlist()
    
    print("✅ Done!")


def run_signals(args):
    """Generate trading signals"""
    print(f"\n📈 {t('generating_signals')}...")
    generator = SignalGenerator()
    
    if '--symbol' in args:
        idx = args.index('--symbol')
        symbol = args[idx + 1] if idx + 1 < len(args) else None
        if symbol:
            print(f"Symbol: {symbol}")
            # TODO: Add symbol-specific signals
    else:
        # Generate for watchlist
        generator.generate_all()
    
    print("✅ Done!")


def run_position(args):
    """Calculate position size"""
    print(f"\n💰 {t('calculating_position')}...")
    calculator = PositionCalculator()
    
    # Parse arguments
    symbol = None
    price = None
    capital = None
    risk = None
    
    i = 0
    while i < len(args):
        if args[i] == '--symbol' and i + 1 < len(args):
            symbol = args[i + 1]
            i += 2
        elif args[i] == '--price' and i + 1 < len(args):
            price = float(args[i + 1])
            i += 2
        elif args[i] == '--capital' and i + 1 < len(args):
            capital = float(args[i + 1])
            i += 2
        elif args[i] == '--risk' and i + 1 < len(args):
            risk = float(args[i + 1])
            i += 2
        else:
            i += 1
    
    if symbol and price and capital:
        result = calculator.calculate(symbol, price, capital, risk)
        print(f"\n{t('symbol')}: {symbol}")
        print(f"{t('entry_price')}: ${price:.2f}")
        print(f"{t('total_capital')}: ${capital:.2f}")
        print(f"{t('position_size')}: {result.get('shares', 0)} shares")
        print(f"{t('position_value')}: ${result.get('position_value', 0):.2f}")
        print(f"{t('risk_amount')}: ${result.get('risk_amount', 0):.2f}")
    else:
        print("Missing required arguments: --symbol, --price, --capital")
        print("Example: openclaw-trading-assistant position --symbol NVDA --price 175.64 --capital 10000")


def run_alerts(args):
    """Manage price alerts"""
    print(f"\n🔔 {t('managing_alerts')}...")
    alerts = StopLossAlert()
    
    if not args or args[0] == 'check':
        alerts.check_all_alerts()
    elif args[0] == 'list':
        alerts.list_alerts()
    elif args[0] == 'create':
        # Parse create arguments
        symbol = None
        entry = None
        stop = None
        target = None
        
        i = 1
        while i < len(args):
            if args[i] == '--symbol' and i + 1 < len(args):
                symbol = args[i + 1]
                i += 2
            elif args[i] == '--entry' and i + 1 < len(args):
                entry = float(args[i + 1])
                i += 2
            elif args[i] == '--stop' and i + 1 < len(args):
                stop = float(args[i + 1])
                i += 2
            elif args[i] == '--target' and i + 1 < len(args):
                target = float(args[i + 1])
                i += 2
            else:
                i += 1
        
        if symbol and entry and stop:
            alerts.create_alert(symbol, entry, stop, target)
            print(f"✅ Alert created for {symbol}")
        else:
            print("Missing required arguments: --symbol, --entry, --stop")
            print("Example: openclaw-trading-assistant alerts create --symbol NVDA --entry 175 --stop 170 --target 185")
    else:
        print("Unknown alerts command. Use: check, list, create")


def run_all(args):
    """Run all analysis"""
    print("\n🚀 Running all analysis...\n")
    run_support_resistance(args)
    print()
    run_signals(args)
    print()
    run_alerts(['check'])
    print("\n✅ All analysis complete!")


def interactive_mode():
    """Start interactive CLI mode"""
    print_banner()
    print("Welcome to OpenClaw Trading Assistant Interactive CLI")
    print("Type 'help' for available commands, 'exit' to quit\n")
    
    while True:
        try:
            user_input = input("ta> ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye! 👋")
                break
            
            if user_input.lower() in ['help', 'h', '?']:
                print_help()
                continue
            
            if user_input.lower() in ['version', 'v']:
                print(f"OpenClaw Trading Assistant v{VERSION}")
                continue
            
            # Parse command
            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]
            
            if command in ['interactive', 'interact', 'cli']:
                print("Already in interactive mode!")
            elif command in ['support', 'support-resistance', 'sr']:
                run_support_resistance(args)
            elif command in ['signals', 'signal', 'sig']:
                run_signals(args)
            elif command in ['position', 'pos', 'calc']:
                run_position(args)
            elif command in ['alerts', 'alert', 'alarm']:
                run_alerts(args)
            elif command in ['all', 'full', 'analyze']:
                run_all(args)
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands")
        
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit")
        except Exception as e:
            print(f"Error: {e}")


def main():
    """Main entry point"""
    args = sys.argv[1:]
    
    # No arguments: start interactive mode
    if not args:
        interactive_mode()
        return
    
    command = args[0].lower()
    command_args = args[1:]
    
    # Handle help
    if command in ['help', 'h', '-h', '--help']:
        print_help()
        return
    
    # Handle version
    if command in ['version', 'v', '-v', '--version']:
        print(f"OpenClaw Trading Assistant v{VERSION}")
        return
    
    # Handle interactive mode
    if command in ['interactive', 'interact', 'cli']:
        interactive_mode()
        return
    
    # Handle commands
    if command in ['support', 'support-resistance', 'sr']:
        run_support_resistance(command_args)
    elif command in ['signals', 'signal', 'sig']:
        run_signals(command_args)
    elif command in ['position', 'pos', 'calc']:
        run_position(command_args)
    elif command in ['alerts', 'alert', 'alarm']:
        run_alerts(command_args)
    elif command in ['all', 'full', 'analyze']:
        run_all(command_args)
    else:
        print(f"Unknown command: {command}")
        print("Type 'openclaw-trading-assistant help' for available commands")
        sys.exit(1)


if __name__ == '__main__':
    main()
