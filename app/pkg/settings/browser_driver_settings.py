from undetected_chromedriver import ChromeOptions as Options

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:84.0) Gecko/20100101 Firefox/84.0 '
chrome_options = Options()
chrome_options.add_experimental_option('prefs',
                                       {'intl.accept_languages': 'en,en_US',
                                        'profile.managed_default_content_settings.images': 100,
                                        'credentials_enable_service': False,
                                        'profile.password_manager_enabled': False,
                                        })
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-first-run')
chrome_options.add_argument(f'--user-agent={user_agent}')
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument('--disable-dev-shm-usage')  # essential options for use in docker containers
