# Commonly used useragent string and probability
ua_pct = {'ua': {'0': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', '1': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70', '2': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', '3': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0', '4': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15', '5': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15', '6': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '7': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0', '8': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '9': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15', '10': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61', '11': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76', '12': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69', '13': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0', '14': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55', '15': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36', '16': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0', '17': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0', '18': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', '19': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko', '20': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36', '21': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', '22': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', '23': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0', '24': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70', '25': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', '26': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36', '27': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70', '28': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', '29': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36', '30': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', '31': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36', '32': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42', '33': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67', '34': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko', '35': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0', '36': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62', '37': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36', '38': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47', '39': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}, 'pct': {'0': 37.4193548387, '1': 17.0967741935, '2': 10.3225806452, '3': 7.4193548387, '4': 5.1612903226, '5': 3.4408602151, '6': 2.0430107527, '7': 1.7204301075, '8': 1.7204301075, '9': 1.7204301075, '10': 1.2903225806, '11': 0.9677419355, '12': 0.8602150538, '13': 0.8602150538, '14': 0.5376344086, '15': 0.4301075269, '16': 0.4301075269, '17': 0.4301075269, '18': 0.4301075269, '19': 0.4301075269, '20': 0.3225806452, '21': 0.3225806452, '22': 0.3225806452, '23': 0.3225806452, '24': 0.3225806452, '25': 0.3225806452, '26': 0.3225806452, '27': 0.3225806452, '28': 0.3225806452, '29': 0.2150537634, '30': 0.2150537634, '31': 0.2150537634, '32': 0.2150537634, '33': 0.2150537634, '34': 0.2150537634, '35': 0.2150537634, '36': 0.2150537634, '37': 0.2150537634, '38': 0.2150537634, '39': 0.2150537634}}

# Website paths to use for valid requests
good_paths = [
    "/index.html",
    "/about-us.html",
    "/our-widgets.html",
    "/widget-features.html",
    "/blog/how-to-choose-the-right-widget.html",
    "/blog/widget-maintenance-tips.html",
    "/blog/the-history-of-widgets.html",
    "/contact-us.html",
    "/blog/10-reasons-to-use-widgets.html",
    "/blog/the-future-of-widgets.html",
    "/blog/widgets-in-action.html",
    "/blog/the-science-of-widgets.html",
    "/faq.html",
    "/widget-catalog.html",
    "/widget-types.html",
    "/custom-widgets.html",
    "/custom-widgets.html",
    "/blog/custom-widgets.html",
    "/blog/custom-widgets.html",
    "/blog/custom-widget-design.html",
    "/blog/custom-widget-design.html",
    "/widget-accessories.html",
    "/blog/widget-trends-2023.html",
    "/blog/widget-design-inspiration.html",
    "/blog/the-art-of-widgets.html",
    "/widget-reviews.html",
    "/widget-testimonials.html",
    "/widget-comparison.html",
    "/widget-careers.html",
    "/blog/widget-innovations.html",
    "/blog/widget-myths-debunked.html",
    "/widget-technology.html",
    "/widget-news.html",
    "/blog/widget-stories.html",
    "/blog/widget-success-stories.html",
    "/widget-partners.html",
    "/widget-resources.html",
    "/blog/widget-industry-insights.html",
    "/widget-events.html",
    "/widget-promotions.html",
    "/widget-sponsorships.html",
    "/blog/widget-philanthropy.html",
    "/widget-sustainability.html",
    "/widget-guarantee.html",
    "/blog/widget-tips-and-tricks.html",
    "/blog/widget-industry-predictions.html",
    "/widget-support.html",
    "/blog/widget-education.html",
    "/widget-terms-and-conditions.html",
    "/widget-privacy-policy.html",
    "/widget-return-policy.html",
    "/widget-return-policy.html",
]

# Website paths to use for invalid requests
bad_paths = [
    "/index.html",
    "/admin/login.html",
    "/dashboard/index.html",
    "/register.html",
    "/profile/edit.html",
    "/settings/General.html",
    "/search/results.html",
    "/news/local.html",
    "/index.jsp",
    "/admin/dashboard.jsp",
    "/joomly/admin/users.jsp",
    "/register/form.jsp",
    "/profile/view.jsp",
    "/settings/security.jsp",
    "/news/world.jsp",
    "/download/latest.jsp",
    "/index.php",
    "/druple/home.php",
    "/admin/overview.php",
    "/druple/admin/posts.php",
    "/register/new.php",
    "/profile/edit.php",
    "/druple/profile/view.php",
    "/settings/General.php",
    "/index.asp",
    "/admin/panel.asp",
    "/gravite/admin/plugins.asp",
    "/register/new.asp",
    "/gravite/register/complete.asp",
    "/profile/edit.asp",
    "/gravite/profile/view.asp",
    "/search/results.asp",
    "/index.cgi",
    "/admin/welcome.cgi",
    "/wizpress/admin/pages.cgi",
    "/register/new.cgi",
    "/profile/edit.cgi",
    "/wizpress/profile/view.cgi",
    "/search/results.cgi",
    "/wizpress/search/advanced.cgi",
    "/index.html",
    "/admin/login.html",
    "/cmsx/admin/dashboard.html",
    "/register/form.html",
    "/profile/view.html",
    "/cmsx/profile/edit.html",
    "/news/world.html",
    "/cmsx/news/local.html",
    "/index.php",
    "/admin/overview.php",
    "/blogie/admin/posts.php",
    "/register/new.php",
    "/blogie/register/complete.php",
    "/profile/view.php",
    "/search/results.php",
    "/blogie/search/advanced.php",
    "/index.jsp",
    "/admin/dashboard.jsp",
    "/pulsecms/admin/plugins.jsp",
    "/register/new.jsp",
    "/pulsecms/register/complete.jsp",
    "/profile/edit.jsp",
    "/pulsecms/profile/view.jsp",
    "/search/results.jsp",
    "/pulsecms/search/advanced.jsp"
]

malicious_ips = [
    '172.20.196.56',
    '192.168.158.57',
    '192.168.58.44',
    '172.23.27.116',
    '10.145.167.168',
    '192.168.75.5',
    '10.55.163.21',
    '172.21.114.240',
    '172.18.195.168',
    '10.197.173.241',
    '172.29.131.219',
    '172.19.142.133',
    '192.168.83.206',
    '172.19.199.153',
    '192.168.45.194',
    '192.168.219.29',
    '192.168.116.255',
    '172.20.134.243',
    '192.168.12.88',
    '10.40.217.181'
]