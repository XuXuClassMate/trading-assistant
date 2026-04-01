// Fix logo and home link for GitHub Pages subdirectory deployment
document.addEventListener('DOMContentLoaded', function() {
  // Fix logo link
  const logoLink = document.querySelector('.md-header__button.md-logo');
  if (logoLink) {
    logoLink.href = '/trading-assistant/';
  }
  
  // Fix home link in navigation
  const homeLink = document.querySelector('.md-nav__item a[href="/"]');
  if (homeLink) {
    homeLink.href = '/trading-assistant/';
    homeLink.addEventListener('click', function(e) {
      e.preventDefault();
      window.location.href = '/trading-assistant/';
    });
  }
});
