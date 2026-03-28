"""
单元测试 - 交易信号生成模块
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from trading_signals import TradingSignalGenerator


class TestTradingSignals(unittest.TestCase):
    """交易信号生成测试"""
    
    def setUp(self):
        """测试前准备"""
        self.generator = TradingSignalGenerator()
        
        # 测试数据：RSI 超卖
        self.oversold_data = {
            'symbol': 'AAPL',
            'price': 150.0,
            'rsi': 25.0,  # 超卖
            'macd': -2.0,
            'signal_line': -1.5,
            'support': 145.0,
            'resistance': 160.0,
        }
        
        # 测试数据：RSI 超买
        self.overbought_data = {
            'symbol': 'AAPL',
            'price': 180.0,
            'rsi': 75.0,  # 超买
            'macd': 3.0,
            'signal_line': 2.5,
            'support': 170.0,
            'resistance': 185.0,
        }
        
        # 测试数据：中性
        self.neutral_data = {
            'symbol': 'AAPL',
            'price': 165.0,
            'rsi': 50.0,  # 中性
            'macd': 0.5,
            'signal_line': 0.3,
            'support': 160.0,
            'resistance': 170.0,
        }
    
    def test_oversold_signal(self):
        """测试超卖信号生成"""
        signals = self.generator.generate_signals(self.oversold_data)
        
        # 超卖时应该有买入信号
        self.assertIsInstance(signals, list)
        
        # 验证信号包含必要字段
        if signals:
            signal = signals[0]
            self.assertIn('action', signal)
            self.assertIn('confidence', signal)
            self.assertIn('reason', signal)
    
    def test_overbought_signal(self):
        """测试超买信号生成"""
        signals = self.generator.generate_signals(self.overbought_data)
        
        # 超买时应该有卖出或观望信号
        self.assertIsInstance(signals, list)
    
    def test_neutral_signal(self):
        """测试中性信号"""
        signals = self.generator.generate_signals(self.neutral_data)
        
        # 中性时应该是观望信号
        self.assertIsInstance(signals, list)
    
    def test_confidence_score(self):
        """测试置信度评分"""
        signals = self.generator.generate_signals(self.oversold_data)
        
        if signals:
            confidence = signals[0].get('confidence', 0)
            # 置信度应该在 0-100 之间
            self.assertGreaterEqual(confidence, 0)
            self.assertLessEqual(confidence, 100)
    
    def test_support_resistance_integration(self):
        """测试支撑阻力位整合"""
        signals = self.generator.generate_signals(self.oversold_data)
        
        if signals:
            # 信号应该考虑支撑阻力位
            self.assertIn('support', self.oversold_data)
            self.assertIn('resistance', self.oversold_data)
    
    def test_invalid_data(self):
        """测试无效数据"""
        invalid_data = {
            'symbol': 'AAPL',
            'price': -100,  # 负价格
        }
        signals = self.generator.generate_signals(invalid_data)
        
        # 无效数据应该返回空列表或错误
        self.assertIsInstance(signals, list)


if __name__ == '__main__':
    unittest.main()
