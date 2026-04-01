// 语言切换功能
// Language Switcher

(function() {
  // 默认语言
  let currentLang = 'en';
  
  // 翻译内容
  const translations = {
    en: {
      // Hero Section
      'hero_title': 'OpenClaw Trading Assistant',
      'hero_subtitle': 'Your AI-Powered Trading Decision Support System',
      'hero_description': 'Professional technical analysis, real-time trading signals, and intelligent position management. Everything you need to make informed trading decisions.',
      
      // Features
      'feature_signals_title': 'Trading Signals',
      'feature_signals_desc': 'AI-powered buy/sell signals based on RSI, support/resistance levels, and market trends.',
      
      'feature_position_title': 'Position Calculator',
      'feature_position_desc': 'Calculate optimal position size based on your risk tolerance and stop-loss distance.',
      
      'feature_stop_title': 'Stop Loss & Take Profit',
      'feature_stop_desc': 'Smart alerts for 5 profit-taking levels and stop-loss protection.',
      
      'feature_monitor_title': 'Real-time Monitor',
      'feature_monitor_desc': '24/7 price monitoring with volatility alerts and breakout detection.',
      
      'feature_backtest_title': 'Backtest Engine',
      'feature_backtest_desc': 'Test your strategies with historical data. SMA crossover, RSI strategies, and more.',
      
      'feature_cli_title': 'CLI Interface',
      'feature_cli_desc': 'Fast, intuitive command-line interface. Get signals and analysis in seconds.',
      
      // CTA Buttons
      'btn_get_started': 'Get Started',
      'btn_view_docs': 'View Documentation',
      'btn_install': 'Install Now',
      
      // Stats Section
      'stats_title': 'Project Stats',
      'stats_downloads': 'Downloads & Usage',
      'stats_community': 'Community',
      'stats_version': 'Latest Version',
      'stats_just_launched': '🆕 Just Launched!',
      'stats_be_first': 'Be the first!',
      
      // Footer
      'footer_made_with': 'Made with ❤️ by',
      'footer_license': 'MIT License',
    },
    zh: {
      // Hero Section
      'hero_title': 'OpenClaw 交易助手',
      'hero_subtitle': 'AI 驱动的交易决策支持系统',
      'hero_description': '专业技术分析、实时交易信号、智能仓位管理。您需要的一切交易决策工具。',
      
      // Features
      'feature_signals_title': '交易信号',
      'feature_signals_desc': '基于 RSI、支撑/阻力位和市场趋势的 AI 驱动买卖信号。',
      
      'feature_position_title': '仓位计算器',
      'feature_position_desc': '根据您的风险承受能力和止损距离计算最佳仓位。',
      
      'feature_stop_title': '止盈止损',
      'feature_stop_desc': '5 级止盈提醒和止损保护智能预警。',
      
      'feature_monitor_title': '实时监控',
      'feature_monitor_desc': '24/7 价格监控，大波动预警和突破检测。',
      
      'feature_backtest_title': '回测引擎',
      'feature_backtest_desc': '使用历史数据测试策略。SMA 交叉、RSI 策略等。',
      
      'feature_cli_title': '命令行界面',
      'feature_cli_desc': '快速直观的命令行界面。秒级获取信号和分析。',
      
      // CTA Buttons
      'btn_get_started': '开始使用',
      'btn_view_docs': '查看文档',
      'btn_install': '立即安装',
      
      // Stats Section
      'stats_title': '项目统计',
      'stats_downloads': '下载与使用',
      'stats_community': '社区',
      'stats_version': '最新版本',
      'stats_just_launched': '🆕 刚发布！',
      'stats_be_first': '成为第一个！',
      
      // Footer
      'footer_made_with': 'Made with ❤️ by',
      'footer_license': 'MIT 许可',
    }
  };
  
  // 设置语言
  function setLang(lang) {
    currentLang = lang;
    localStorage.setItem('preferred_lang', lang);
    document.documentElement.setAttribute('lang', lang);
    
    // 更新按钮状态
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.lang === lang) {
        btn.classList.add('active');
      }
    });
    
    // 更新内容
    updateContent();
    
    // 更新 URL（不刷新页面）
    const basePath = window.location.pathname.includes('/trading-assistant/') 
      ? '/trading-assistant/' 
      : '/';
    const newPath = lang === 'zh' ? basePath + 'zh/' : basePath;
    window.history.pushState({lang}, '', newPath);
  }
  
  // 更新内容
  function updateContent() {
    const t = translations[currentLang];
    if (!t) return;
    
    // 遍历所有翻译键
    Object.keys(t).forEach(key => {
      const el = document.querySelector(`[data-i18n="${key}"]`);
      if (el) {
        el.textContent = t[key];
      }
    });
  }
  
  // 初始化
  function init() {
    // 检查保存的语言偏好
    const saved = localStorage.getItem('preferred_lang');
    const preferred = saved || 'en'; // 默认英文
    
    setLang(preferred);
    
    // 添加语言切换按钮事件
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        setLang(btn.dataset.lang);
      });
    });
  }
  
  // 页面加载后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  
  // 暴露全局函数
  window.setLang = setLang;
})();
