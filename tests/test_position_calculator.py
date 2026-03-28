"""
单元测试 - 仓位计算器模块
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from position_calculator import PositionCalculator


class TestPositionCalculator(unittest.TestCase):
    """仓位计算器测试"""
    
    def setUp(self):
        """测试前准备"""
        self.calculator = PositionCalculator()
    
    def test_basic_position_calculation(self):
        """测试基础仓位计算"""
        result = self.calculator.calculate(
            entry_price=100.0,
            stop_loss=95.0,
            capital=10000.0,
            risk_percent=2.0
        )
        
        # 验证结果包含必要字段
        self.assertIn('shares', result)
        self.assertIn('position_size', result)
        self.assertIn('risk_amount', result)
        
        # 验证股数为正整数
        self.assertGreater(result['shares'], 0)
        self.assertIsInstance(result['shares'], int)
    
    def test_risk_amount_calculation(self):
        """测试风险金额计算"""
        capital = 10000.0
        risk_percent = 2.0
        expected_risk = capital * (risk_percent / 100)  # $200
        
        result = self.calculator.calculate(
            entry_price=100.0,
            stop_loss=95.0,
            capital=capital,
            risk_percent=risk_percent
        )
        
        # 风险金额应该是资本的 2%
        self.assertAlmostEqual(result['risk_amount'], expected_risk, places=2)
    
    def test_stop_loss_distance(self):
        """测试止损距离计算"""
        entry_price = 100.0
        stop_loss = 95.0
        expected_distance = entry_price - stop_loss  # $5
        
        result = self.calculator.calculate(
            entry_price=entry_price,
            stop_loss=stop_loss,
            capital=10000.0,
            risk_percent=2.0
        )
        
        # 止损距离应该是$5
        self.assertAlmostEqual(result['stop_loss_distance'], expected_distance, places=2)
    
    def test_high_risk_percent(self):
        """测试高风险百分比"""
        result = self.calculator.calculate(
            entry_price=100.0,
            stop_loss=95.0,
            capital=10000.0,
            risk_percent=10.0  # 10% 高风险
        )
        
        # 高风险应该导致更大的仓位
        self.assertGreater(result['shares'], 40)  # 比 2% 风险时大
    
    def test_tight_stop_loss(self):
        """测试紧密止损"""
        result = self.calculator.calculate(
            entry_price=100.0,
            stop_loss=99.0,  # 只有$1 止损空间
            capital=10000.0,
            risk_percent=2.0
        )
        
        # 紧密止损应该允许更大的仓位
        self.assertGreater(result['shares'], 100)
    
    def test_invalid_input_negative_price(self):
        """测试无效输入：负价格"""
        result = self.calculator.calculate(
            entry_price=-100.0,
            stop_loss=95.0,
            capital=10000.0,
            risk_percent=2.0
        )
        
        # 负价格应该返回错误或 None
        self.assertIsNone(result)
    
    def test_invalid_input_stop_above_entry(self):
        """测试无效输入：止损高于入场价"""
        result = self.calculator.calculate(
            entry_price=100.0,
            stop_loss=105.0,  # 止损高于入场价
            capital=10000.0,
            risk_percent=2.0
        )
        
        # 对于多头仓位，止损高于入场价是无效的
        self.assertIsNone(result)
    
    def test_zero_capital(self):
        """测试零资金"""
        result = self.calculator.calculate(
            entry_price=100.0,
            stop_loss=95.0,
            capital=0.0,
            risk_percent=2.0
        )
        
        # 零资金应该返回 0 股
        self.assertEqual(result['shares'], 0)


if __name__ == '__main__':
    unittest.main()
