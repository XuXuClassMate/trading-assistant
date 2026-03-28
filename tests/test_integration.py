#!/usr/bin/env python3
"""
集成测试
Integration Tests

测试整个交易助手系统的端到端功能。
"""

import unittest
import sys
import os
import subprocess
import json
from datetime import datetime, timedelta

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCLIIntegration(unittest.TestCase):
    """CLI 集成测试"""
    
    def test_cli_version(self):
        """测试 CLI 版本命令"""
        result = subprocess.run(
            ['python3', 'cli.py', 'version'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('OpenClaw Trading Assistant', result.stdout)
    
    def test_cli_help(self):
        """测试 CLI 帮助命令"""
        result = subprocess.run(
            ['python3', 'cli.py', 'help'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('Commands:', result.stdout)
        self.assertIn('support-resistance', result.stdout)
        self.assertIn('signals', result.stdout)
        self.assertIn('position', result.stdout)
    
    def test_cli_monitor_command(self):
        """测试监控命令（不实际运行）"""
        result = subprocess.run(
            ['python3', 'cli.py', 'monitor', '--help'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('--watchlist', result.stdout)
        self.assertIn('--interval', result.stdout)
    
    def test_cli_backtest_command(self):
        """测试回测命令（不实际运行）"""
        result = subprocess.run(
            ['python3', 'cli.py', 'backtest', '--help'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('SYMBOL', result.stdout)
        self.assertIn('START_DATE', result.stdout)
        self.assertIn('END_DATE', result.stdout)
    
    def test_cli_cost_command(self):
        """测试成本分析命令"""
        result = subprocess.run(
            ['python3', 'cli.py', 'cost', '--help'],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('--type', result.stdout)


class TestModuleIntegration(unittest.TestCase):
    """模块集成测试"""
    
    def test_import_all_modules(self):
        """测试所有模块可导入"""
        modules = [
            'config',
            'support_resistance',
            'trading_signals',
            'position_calculator',
            'stop_loss_alerts',
            'realtime_monitor',
            'backtest_engine',
            'optimizer',
            'position_cost_analyzer',
        ]
        
        for module_name in modules:
            try:
                __import__(module_name)
            except ImportError as e:
                self.fail(f"无法导入模块 {module_name}: {e}")
    
    def test_config_loading(self):
        """测试配置加载"""
        from config import Config
        
        config = Config()
        
        # 验证配置对象存在
        self.assertIsNotNone(config)
        
        # 验证 API Keys 字典存在
        self.assertTrue(hasattr(config, 'api_keys'))
    
    def test_data_flow(self):
        """测试数据流：支撑阻力位 → 交易信号"""
        from support_resistance import SupportResistanceCalculator
        from trading_signals import TradingSignalGenerator
        
        # 1. 计算支撑阻力位
        sr_calc = SupportResistanceCalculator()
        
        # 模拟数据
        test_data = [
            {'datetime': '2024-01-01', 'high': 100, 'low': 95, 'close': 98, 'volume': 1000},
            {'datetime': '2024-01-02', 'high': 105, 'low': 98, 'close': 103, 'volume': 1200},
            {'datetime': '2024-01-03', 'high': 110, 'low': 103, 'close': 108, 'volume': 1500},
        ]
        
        sr_result = sr_calc.calculate_pivot_points(test_data)
        
        # 2. 生成交易信号
        signal_gen = TradingSignalGenerator()
        
        signal_data = {
            'symbol': 'TEST',
            'price': 108,
            'rsi': 50,
            'macd': 0.5,
            'signal_line': 0.3,
            'support': sr_result.get('support', [95])[0] if sr_result else 95,
            'resistance': sr_result.get('resistance', [110])[0] if sr_result else 110,
        }
        
        signals = signal_gen.generate_signals(signal_data)
        
        # 验证信号生成
        self.assertIsInstance(signals, list)
    
    def test_position_calculation_flow(self):
        """测试仓位计算流程"""
        from position_calculator import PositionCalculator
        
        calc = PositionCalculator()
        
        result = calc.calculate(
            entry_price=100.0,
            stop_loss=95.0,
            capital=10000.0,
            risk_percent=2.0
        )
        
        # 验证结果完整
        self.assertIn('shares', result)
        self.assertIn('position_size', result)
        self.assertIn('risk_amount', result)
        self.assertIn('stop_loss_distance', result)
        
        # 验证计算正确
        self.assertEqual(result['risk_amount'], 200.0)  # 10000 * 2%
    
    def test_optimizer_cache(self):
        """测试优化器缓存功能"""
        from optimizer import APICache
        
        cache = APICache(ttl_seconds=60)
        
        # 设置缓存
        cache.set('test', {'key': 'value'}, {'data': 'test_data'})
        
        # 获取缓存
        result = cache.get('test', {'key': 'value'})
        
        self.assertIsNotNone(result)
        self.assertEqual(result['data'], 'test_data')
        
        # 清理
        cache.clear()
    
    def test_optimizer_rate_limiter(self):
        """测试速率限制器"""
        from optimizer import RateLimiter
        
        limiter = RateLimiter(calls_per_day=100, calls_per_minute=10)
        
        # 检查初始状态
        can_call, msg = limiter.can_call()
        
        self.assertTrue(can_call)
        
        # 记录调用
        limiter.record_call()
        
        # 验证统计
        stats = limiter.stats()
        self.assertGreaterEqual(stats['calls_today'], 1)


class TestEndToEnd(unittest.TestCase):
    """端到端测试"""
    
    def test_full_analysis_pipeline(self):
        """测试完整分析流程"""
        from support_resistance import SupportResistanceCalculator
        from trading_signals import TradingSignalGenerator
        from position_calculator import PositionCalculator
        
        # 1. 准备数据
        test_data = [
            {'datetime': '2024-01-01', 'high': 100, 'low': 95, 'close': 98, 'volume': 1000},
            {'datetime': '2024-01-02', 'high': 105, 'low': 98, 'close': 103, 'volume': 1200},
            {'datetime': '2024-01-03', 'high': 110, 'low': 103, 'close': 108, 'volume': 1500},
        ]
        
        # 2. 计算支撑阻力位
        sr_calc = SupportResistanceCalculator()
        sr_result = sr_calc.calculate_pivot_points(test_data)
        
        # 3. 生成交易信号
        signal_gen = TradingSignalGenerator()
        signal_data = {
            'symbol': 'TEST',
            'price': 108,
            'rsi': 50,
            'support': sr_result.get('pivot', 100) if sr_result else 100,
            'resistance': sr_result.get('resistance', [110])[0] if sr_result else 110,
        }
        signals = signal_gen.generate_signals(signal_data)
        
        # 4. 计算仓位
        pos_calc = PositionCalculator()
        position = pos_calc.calculate(
            entry_price=108,
            stop_loss=sr_result.get('support', [95])[0] if sr_result else 95,
            capital=10000,
            risk_percent=2
        )
        
        # 验证流程完整
        self.assertIsNotNone(sr_result)
        self.assertIsInstance(signals, list)
        self.assertIsNotNone(position)
        self.assertIn('shares', position)


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 添加测试
    suite.addTests(loader.loadTestsFromTestCase(TestCLIIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestModuleIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestEndToEnd))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回结果
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
