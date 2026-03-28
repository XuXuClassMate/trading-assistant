"""
单元测试 - 支撑/阻力位计算模块
"""

import unittest
import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from support_resistance import SupportResistanceCalculator


class TestSupportResistance(unittest.TestCase):
    """支撑/阻力位计算测试"""
    
    def setUp(self):
        """测试前准备"""
        self.calculator = SupportResistanceCalculator()
        
        # 测试数据：上涨趋势
        self.uptrend_data = [
            {'datetime': '2024-01-01', 'high': 100, 'low': 95, 'close': 98, 'volume': 1000},
            {'datetime': '2024-01-02', 'high': 105, 'low': 98, 'close': 103, 'volume': 1200},
            {'datetime': '2024-01-03', 'high': 110, 'low': 103, 'close': 108, 'volume': 1500},
            {'datetime': '2024-01-04', 'high': 115, 'low': 108, 'close': 112, 'volume': 1300},
            {'datetime': '2024-01-05', 'high': 120, 'low': 112, 'close': 118, 'volume': 1600},
        ]
        
        # 测试数据：震荡趋势
        self.ranging_data = [
            {'datetime': '2024-01-01', 'high': 105, 'low': 95, 'close': 100, 'volume': 1000},
            {'datetime': '2024-01-02', 'high': 103, 'low': 97, 'close': 99, 'volume': 1100},
            {'datetime': '2024-01-03', 'high': 104, 'low': 96, 'close': 101, 'volume': 1200},
            {'datetime': '2024-01-04', 'high': 102, 'low': 98, 'close': 100, 'volume': 1000},
            {'datetime': '2024-01-05', 'high': 105, 'low': 95, 'close': 102, 'volume': 1300},
        ]
    
    def test_pivot_point_calculation(self):
        """测试枢轴点算法"""
        result = self.calculator.calculate_pivot_points(self.uptrend_data)
        
        # 验证结果包含必要的键
        self.assertIn('pivot', result)
        self.assertIn('resistance', result)
        self.assertIn('support', result)
        
        # 验证枢轴点在最高和最低价之间
        prices = [d['close'] for d in self.uptrend_data]
        self.assertGreaterEqual(result['pivot'], min(prices))
        self.assertLessEqual(result['pivot'], max(prices))
    
    def test_high_low_identification(self):
        """测试高低点识别"""
        result = self.calculator.identify_highs_lows(self.uptrend_data)
        
        # 验证结果结构
        self.assertIn('highs', result)
        self.assertIn('lows', result)
        
        # 上涨趋势中，高点应该递增
        if len(result['highs']) > 1:
            for i in range(1, len(result['highs'])):
                self.assertGreaterEqual(
                    result['highs'][i]['price'],
                    result['highs'][i-1]['price']
                )
    
    def test_volume_weighted_levels(self):
        """测试成交量加权支撑阻力位"""
        result = self.calculator.calculate_volume_weighted_levels(self.uptrend_data)
        
        # 验证结果结构
        self.assertIn('levels', result)
        self.assertIsInstance(result['levels'], list)
        
        # 每个级别应该有价格和成交量
        for level in result['levels']:
            self.assertIn('price', level)
            self.assertIn('volume', level)
    
    def test_ranging_market(self):
        """测试震荡市场支撑阻力位"""
        result = self.calculator.calculate_pivot_points(self.ranging_data)
        
        # 震荡市场中，枢轴点应该接近中间值
        self.assertGreater(result['pivot'], 95)
        self.assertLess(result['pivot'], 105)
    
    def test_empty_data(self):
        """测试空数据"""
        result = self.calculator.calculate_pivot_points([])
        
        # 空数据应该返回 None 或空结果
        self.assertIsNone(result)
    
    def test_insufficient_data(self):
        """测试数据不足"""
        insufficient_data = [
            {'datetime': '2024-01-01', 'high': 100, 'low': 95, 'close': 98, 'volume': 1000},
        ]
        result = self.calculator.calculate_pivot_points(insufficient_data)
        
        # 单条数据无法计算枢轴点
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
