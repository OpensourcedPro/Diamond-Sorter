import random
    
# List of possible components for user agent
browsers = ["Mozilla", "Chrome"]
os_systems = ["Windows NT 10.0", "Windows NT 6.1", "Macintosh", "Linux"]
browser_versions = [f"{random.randint(1, 10)}.0" for _ in range(3)]


class fake:
    def useragent():
        # Randomly choose components
        browser = random.choice(browsers)
        os_system = random.choice(os_systems)
        browser_version = random.choice(browser_versions)

        # Assemble the user agent string
        user_agent = str(f"{browser}/5.0 ({os_system}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version} Safari/537.36")
        
        return user_agent